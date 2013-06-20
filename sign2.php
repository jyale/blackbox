<?php

///////////////
// FACEBOOK LOGIN STUFF
///////////////

require 'php-sdk/facebook.php';

// Create our Application instance (replace this with your appId and secret).
$facebook = new Facebook(array(
  'appId'  => '131686000339117',
  'secret' => 'bda3a9ca0d385c804d42ecd7beb91c65',
));

// Get User ID
$user = $facebook->getUser();

$info = $facebook->api('/me');
$username = $info['username'];
$username = "https://www.facebook.com/" . $username;

///////////////////////
// End of Facebook stuff
///////////////////


	// get the file that we're going to leak
        $file = $_REQUEST['file'];
     
	// Get the message String
    $rawString = $_POST['comments'];

// handle windows vs unix line breaks
$output = str_replace(array("\r\n", "\r"), "\n", $rawString);          
$rawString = $output;

    // Split the string into pieces for processing
    $pieces = explode("\n", $rawString);
     

    // First element is the subject line
    //$subject = $pieces[0];
     
    // Take the array, delete the first entry, So we can pass it to $message
    $messagePieces = array_slice($pieces, 0);
     
    // Replace the \n or add a <br /> if you like.
    $message = implode("<br />", $messagePieces);

    $oneline = implode(" ", $messagePieces);
/*
    echo $message;
	echo('<br>');
	echo $oneline;
	echo exec('python2.7 signer.py ' . $username . ' ' . $oneline . ' ' . $file);

	echo('<br>');
*/
	echo('<a href="' . $file . '">' . str_replace("uploads/","",$file) . '</a> has been signed: ' . '<a href="sigs' . substr($file, 7) . '-sig">download signature</a>');
	echo('<br><br>');
	echo('<a href="index.php">Home</a>');
?>

