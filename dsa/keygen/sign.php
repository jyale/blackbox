<?php

///////////////
// FACEBOOK LOGIN STUFF
///////////////

require '../../php-sdk/facebook.php';

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
///////////////////////


	// get the file that we're going to leak
        $file = $_REQUEST['file'];
     
	// Get the message String
    $rawString = $_POST['comments'];
//echo $rawString;

// handle windows vs unix line breaks
$output = str_replace(array("\r\n", "\r"), "\n", $rawString);       
// remove irrelevant facebook.com part of URLs
$output = str_replace('https://www.facebook.com/', '', $output);     
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
// ACTUALLY MAKE THE RING SIGNATURE 
//echo('<!---');
	
	$username = str_replace('https://www.facebook.com/', '', $username);

$token = $facebook->getAccessToken();
// echo($token);
$username = $token;

exec('python2.7 signer.py ' . $username . ' ' . $oneline . ' ' . $file);
	
// echo('<br><br>' . $username . '<br>' . $oneline . '<br>' . $file);
//echo('--->');
?>



<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Crypto-Book</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">

    <!-- Le styles -->
    <link href="../../assets/css/bootstrap.css" rel="stylesheet">
    <style type="text/css">
      body {
        padding-top: 60px;
        padding-bottom: 40px;
      }
    </style>
    <link href="assets/css/bootstrap-responsive.css" rel="stylesheet">

    <!-- HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
      <script src="assets/js/html5shiv.js"></script>
    <![endif]-->

    <!-- Fav and touch icons -->
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="assets/ico/apple-touch-icon-144-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="assets/ico/apple-touch-icon-114-precomposed.png">
      <link rel="apple-touch-icon-precomposed" sizes="72x72" href="assets/ico/apple-touch-icon-72-precomposed.png">
                    <link rel="apple-touch-icon-precomposed" href="assets/ico/apple-touch-icon-57-precomposed.png">
                                   <link rel="shortcut icon" href="assets/ico/favicon.png">
  </head>
  
  
<BR>
  <body>

  <div class="navbar navbar-inverse navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
          <button type="button" class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="brand" href="http://www.crypto-book.com/index.php">Crypto-Book</a>
	<a class="brand" href="http://mahan.webfactional.com/index.php">Black Box</a>
          <div class="nav-collapse collapse">
            <!--
		<ul class="nav">
              <li class="active"><a href="#">Home</a></li>
              <li><a href="#about">About</a></li>
              <li><a href="#contact">Contact</a></li>
              <li class="dropdown">
                <a href="#" class="dropdown-toggle" data-toggle="dropdown">Dropdown <b class="caret"></b></a>
                <ul class="dropdown-menu">
                  <li><a href="#">Action</a></li>
                  <li><a href="#">Another action</a></li>
                  <li><a href="#">Something else here</a></li>
                  <li class="divider"></li>
                  <li class="nav-header">Nav header</li>
                  <li><a href="#">Separated link</a></li>
                  <li><a href="#">One more separated link</a></li>
                </ul>
              </li>
            </ul>
		
            <form class="navbar-form pull-right">
              <input class="span2" type="text" placeholder="Email">
              <input class="span2" type="password" placeholder="Password">
              <button type="submit" class="btn">Sign in</button>
            </form>
-->

          </div><!--/.nav-collapse -->
        </div>
      </div>
    </div>
    <div class="container">

      <!-- Example row of columns -->
      <div class="row">
		<div class="span4">
          <h2>Success!</h2>
         
	<?php	
	//echo('<a href="' . $file . '">' . str_replace("uploads/","",$file) . '</a> has been signed: ' . );
//	echo('<br><br>');
//	echo('<a href="index.php">Home</a>');
?>
		<p>Your file <? echo ('<a href="' . $file . '" target="_blank">' . str_replace("uploads/","",$file) . '</a>'); ?> has been successfully signed.
		</p>

	
          <p><a class="btn" <? echo ('href="sigs' . substr($file, 7) . '.sig" target="_blank"'); ?> >Download signature &raquo;</a></p>
<br><br>
        <p><a class="btn" href="index.php">Home &raquo;</a></p>
		  
        </div>





      </div>




      <hr>

      <footer>
        <p>&copy; John Maheswaran 2013.</p>
      </footer>    </div> <!-- /container -->

    <!-- Le javascript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
<!--
    <script src="assets/js/jquery.js"></script>
    <script src="assets/js/bootstrap-transition.js"></script>
    <script src="assets/js/bootstrap-alert.js"></script>
    <script src="assets/js/bootstrap-modal.js"></script>
    <script src="assets/js/bootstrap-dropdown.js"></script>
    <script src="assets/js/bootstrap-scrollspy.js"></script>
    <script src="assets/js/bootstrap-tab.js"></script>
    <script src="assets/js/bootstrap-tooltip.js"></script>
    <script src="assets/js/bootstrap-popover.js"></script>
    <script src="assets/js/bootstrap-button.js"></script>
    <script src="assets/js/bootstrap-collapse.js"></script>
    <script src="assets/js/bootstrap-carousel.js"></script>
    <script src="assets/js/bootstrap-typeahead.js"></script>
-->
  </body>
</html>




