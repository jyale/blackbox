<?php

require 'php-sdk/facebook.php';

// Create our Application instance (replace this with your appId and secret).
$facebook = new Facebook(array(
  'appId'  => '131686000339117',
  'secret' => 'bda3a9ca0d385c804d42ecd7beb91c65',
));

// Get User ID
$user = $facebook->getUser();

// We may or may not have this data based on whether the user is logged in.
//
// If we have a $user id here, it means we know the user is logged into
// Facebook, but we don't know if the access token is valid. An access
// token is invalid if the user logged out of Facebook.

if ($user) {
  try {
    // Proceed knowing you have a logged in user who's authenticated.
    $user_profile = $facebook->api('/me');
  } catch (FacebookApiException $e) {
    error_log($e);
    $user = null;
  }
}

// Login or logout url will be needed depending on current user state.
if ($user) {
  $logoutUrl = $facebook->getLogoutUrl();
} else {
$params = array(
  'scope' => 'email,offline_access,user_website,friends_website,publish_stream'
);
  $loginUrl = $facebook->getLoginUrl($params);

}

// This call will always work since we are fetching public data.
$naitik = $facebook->api('/naitik');
	$token = $facebook->getAccessToken();;

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
    <link href="assets/css/bootstrap.css" rel="stylesheet">
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

  <body>
<?php
include("header.html");
?>
    <div class="container">
      <div class="row">
        <div class="span4">
		  <h2>Access token</h2>
		  <p>Your unique personal access token is:</p>
		  <p><code><? echo $token ?></code></p>
<p><br></p>
 <p><a class='btn' href='desktop.php'>Back &raquo;</a></p>
        </div>

     


	
 <div class="span4">
	<h2></h2>
	<p></p>
<!--
<p><iframe src="http://www.slideshare.net/slideshow/embed_code/20273654" width="427" height="356" frameborder="0" marginwidth="0" marginheight="0" scrolling="no"></iframe><p>
<div style="margin-bottom:5px"> <strong> <a href="slides2.pdf" target="_blank">Download slides [pdf]</a> </strong> </div>
-->
<!--
<p><iframe src="http://www.slideshare.net/slideshow/embed_code/17114013" width="427" height="356" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC;border-width:1px 1px 0;margin-bottom:5px" allowfullscreen webkitallowfullscreen mozallowfullscreen> </iframe> 
<div style="margin-bottom:5px"> <strong> <a href="slides1.pdf" target="_blank">Download slides [pdf]</a> </strong> </div>
-->

<p></p>		  

        </div>

      </div>

      <hr>

<?php
include("footer.html");
?>

    </div> <!-- /container -->

    <!-- Le javascript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
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

  </body>
</html>
