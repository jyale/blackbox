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

?>


<!doctype html> 
<html xmlns:fb="http://www.facebook.com/2008/fbml" lang="en">

<head>
 </head>

  <body>
	<!--<h1>php-sdk</h1>
	-->
    <?php if ($user): ?>
      <!--
	  <a href="<?php echo $logoutUrl; ?>">Logout</a>
	  -->
    <?php else: ?>
      <div>
        <!--Login using OAuth 2.0 handled by the PHP SDK:
        <a href="<?php echo $loginUrl; ?>">Login with Facebook</a>
		-->
		<?php
		echo("<script> top.location.href='" . $loginUrl . "'</script>");
		?>
      </div>
    <?php endif ?>



<?php
	$token = $facebook->getAccessToken();;
	echo $token;

	$_REDIRURL = 'upload.php?token=' . $token;
	echo("<script> top.location.href='" . $_REDIRURL . "'</script>");
	

?>

 
  </body>

</html>
