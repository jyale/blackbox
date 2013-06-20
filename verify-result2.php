<?php

$sig = $_REQUEST['sig'];
$file = $_REQUEST['file'];

$weak = exec('python2.7 verifier-file.py ' . $sig . ' ' . $file);
echo $weak;

?>
<br><br>
<a href="index.php">Home</a>