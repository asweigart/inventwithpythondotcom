<?php
include "config.php";

@mysql_connect($sql_host, $sql_user, $sql_pass); 
@mysql_select_db($sql_name);

// read the post from PayPal system and add 'cmd'
$req = 'cmd=_notify-validate';

foreach ($_POST as $key => $value) {
	$value = urlencode(stripslashes($value));
	$req .= "&$key=$value";
}

// post back to PayPal system to validate
$header .= "POST /cgi-bin/webscr HTTP/1.0\r\n";
$header .= "Host: {$GLOBALS['PAYPAL_URL']}:80\r\n";
$header .= "Content-Type: application/x-www-form-urlencoded\r\n";
$header .= "Content-Length: " . strlen($req) . "\r\n\r\n";

$fp = fsockopen ("{$GLOBALS['PAYPAL_URL']}", 80, $errno, $errstr, 30);

if (!$fp) {
	die("error");
} 
else {
	$result = fputs ($fp, $header . $req);

	while (!feof($fp)) {
		$res = fgets ($fp, 1024); // get something

		if (strcmp ($res, "VERIFIED") == 0) {
			$itemid = mysql_escape_string($_POST['item_number']);
			$amount = mysql_escape_string($_POST['payment_gross']);
			$comment = mysql_escape_string($_POST['custom']);
			$buyer_email = mysql_escape_string($_POST['payer_email']);
			$buyer_name = mysql_escape_string($_POST['first_name'] . ' ' . $_POST['last_name']);
			$txn_id = mysql_escape_string($_POST['txn_id']);
			$buyer_id = mysql_escape_string($_POST['payer_id']);

			$sql = mysql_query("INSERT INTO {$GLOBALS['PURCHASE_TABLE']} (itemid, amount, comment, buyer_email, buyer_name, buy_date, txn_id, buyer_id, id) VALUES('$itemid', '$amount', '$comment', '$buyer_email', '$buyer_name', NOW(), '$txn_id', '$buyer_id', NULL)");
		}
		else if (strcmp ($res, "INVALID") == 0) {
			// invalid, do nothing
		}
	}
	fclose ($fp);
}
?>