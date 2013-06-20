<?php

// get the facebook id
$id = $_REQUEST["id"];


// run the python script to make the public keys
// save the output in $op
$out = exec('python2.7 dsapubgen.py ' . $id, $op);
//echo '<big><code>';

for($i = 0; $i < count($op); $i++){
	echo $op[$i];
//	echo '<br>';
}
//echo '</code></big>'; 
?>
