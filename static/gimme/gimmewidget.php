<?

include "config.php";

@mysql_connect($sql_host, $sql_user, $sql_pass);
@mysql_select_db($sql_name);

$sql = mysql_query("SELECT * FROM {$GLOBALS['PURCHASE_TABLE']} ORDER BY id DESC LIMIT {$GLOBALS['WIDGET_ITEMS']}") or die(mysql_error());
$info = mysql_fetch_array($sql);

$headertext = "<h3>Like the book? Buy the author a star, heart, or python and leave a message!</h3>";

if($_GET['headertext']) {
	$headertext = addslashes($_GET['headertext']);
}

print <<<HTML
	document.write('<div id="gimme-main"><p><a href="{$GLOBALS['ROOT']}" target="_top">$headertext</a></p>');
HTML;

$i=0;
while($info) {

$info[comment] = addslashes($info[comment]);


print <<<HTML
	document.write("<img id=\"{$info[itemid]}\" style=\"\" onmouseover=\"document.getElementById('gimme-message').innerHTML = '{$info['comment']}';\" onmouseout=\"document.getElementById('gimme-message').innerHTML = '{$defaultText}';\" src=\"/gimmie/images/icon{$info[itemid]}-small.png\" />");
HTML;

$info = mysql_fetch_array($sql);
$i++;

if($i == ($GLOBALS['WIDGET_ITEMS_PER_LINE'])) {
	echo 'document.write("<br />");';
	$i=0;
}

}
?>
	document.write('<div id="gimme-message"><?php echo $defaultText; ?></div></div>');
<?

die();
?>