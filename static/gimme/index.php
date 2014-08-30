<?

include "config.php";

print <<<HTML
<html>
<head>
<script src="{$GLOBALS['ROOT']}js/jquery-1.2.1.min.js" type="text/javascript"></script>

<style>
body, td {
	text-align: center;
	font-family: arial;
	color: #888;
	font-size: 16px;
}

td {
	padding: 0px 10px 0px 10px;
	font-size: 13px;
	font-weight: bold;
}
#choose img {
	border: 2px solid #ccc;
	padding: 10px;
}
#choose img:hover {
	border: 2px solid #aaa;
}
img {
	border: 0;	
}
li {
	display: inline;
	margin: 0;
	text-align: center;
	padding-top: 20px;
}
#entermessage {
	display: none;
}
#preview {
	display: none;
}
#pay {
	display: none;
}

#messagepreview {
	font-size: 11px;
}
</style>

<script>
var message;
var item;
var amount;

itemPrices = new Array();
itemNames = new Array();
HTML;

$count = 1;
foreach($GLOBALS['ITEMS'] as $name => $price) {

print <<<HTML
	itemPrices[{$count}] = "$price";
	itemNames[{$count}] = "$name";
HTML;

$count++;
}

print <<<HTML

function aclick(i) {
	$('#entermessage').show();
	$('#item_number').attr({value: i});
	$('#amount').attr({value: itemPrices[i]});
	document.messageform.message.focus();
	item = i;
}

function escapeHtmlEntities(s) {
	s = s.replace(new RegExp("<", "gm"), '');
	s = s.replace(new RegExp(">", "gm"), '');
	s = s.replace(new RegExp("&", "gm"), '');
	s = s.replace(new RegExp("\"", "gm"), '');
	s = s.replace(new RegExp("\'", "gm"), '');
	return s
}


function preview() {
	$('#iconpreview').attr({src: '{$GLOBALS['ROOT']}/images/icon' + item + '-small.png'});

	if(escapeHtmlEntities($('#message').attr('value'))) {
		message = escapeHtmlEntities($('#message').attr('value'));
	}
	else {
		message = '';
	}
	
	$('#item_name').attr({value: "[{$GLOBALS['ARTIST']} sponsorship] " + itemNames[item] + " - " + message});
	$('#custom').attr({value: message});
	$('#choose').hide();
	$('#entermessage').hide();
	$('#preview').show();
}

function pay() {
	$('#pay').show();
}

function what() {
	alert('what');
}

function startover() {
	$('#pay').hide();
	$('#preview').hide();
	$('#entermessage').hide();
	$('#choose').show();
	$('#message').val("");
}


function setmessage() {
	var previewmessage = escapeHtmlEntities($('#message').attr('value'));
}

</script>
</head>

<body>
HTML;

// display items


print <<<HTML
<h1>{$GLOBALS['ARTIST']}</h1>

<div id="choose">
<!-- <h2>gimme some money</h2> -->
<h3>choose your sponsorship level</h3>

<table align="center" cellspacing="10">
	<tr>
HTML;

$i=1;
foreach($GLOBALS['ITEMS'] as $name => $price) {
print <<<HTML
		<td><a href="#" onclick="aclick($i);"><img src="{$GLOBALS['ROOT']}/images/icon{$i}.png" /></a><p>$name \$$price</p></td>
HTML;
$i++;
}
		
print <<<HTML
	</tr>
</table>
</div>
HTML;


print <<<HTML

<div id="entermessage">
<h3>enter your message</h3>
<form id="messageform" name="messageform">
<p><input type="text" id="message" size=40 onblur="setmessage();" /></p>
<input type="button" value="preview & pay" onclick="preview();">
</form>
</div>
HTML;

print <<<HTML

<div id="preview">
<h3>test and click your sponsorship to continue</h3>

<p><a href="#" onmouseover="document.getElementById('messagepreview').innerHTML = message;" onmouseout="document.getElementById('messagepreview').innerHTML = '&nbsp;';" onclick="pay();"><img id="iconpreview" src="/images/icon1.gif" /></a>
<div id="messagepreview">&nbsp;</div>
</p>
<br />
</div>
HTML;


print <<<HTML
<div id="pay">
<h3>now gimme some money!</h3>

<p>want to make changes? <a href="#" onclick="startover();">start over</a></p>

<p>click the PayPal Checkout button to pay</p>

<form action="https://{$GLOBALS['PAYPAL_URL']}/cgi-bin/webscr" method="post">
<input type="hidden" name="cmd" value="_xclick">
<input type="hidden" name="business" value="{$GLOBALS['PAYPAL_EMAIL']}">
<input type="hidden" name="item_name" id="item_name" value="">
<input type="hidden" name="amount" id="amount" value="">
<input type="hidden" name="custom" id="custom" value="">
<input type="hidden" name="item_number" id="item_number" value="">
<input type="hidden" name="no_shipping" value="1">
<input type="hidden" name="notify_url" value="{$GLOBALS['ROOT']}notify.php">
<input type="hidden" name="return" value="{$GLOBALS['ROOT']}completed/">
<input type="hidden" name="no_note" value="1">
<input type="hidden" name="currency_code" value="{$GLOBALS['CURRENCY']}">
<input type="hidden" name="tax" value="0">
<input type="hidden" name="lc" value="US">
<input type="hidden" name="bn" value="PP-DonationsBF">
<input type="image" src="{$GLOBALS['ROOT']}images/btn_xpressCheckout2.gif" border="0" name="submit" alt="Make payments with PayPal - it's fast, free and secure!">

</form>
</div>
HTML;

print <<<HTML

</body>
</html>


HTML;

?>