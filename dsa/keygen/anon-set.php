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
// print_r($info['username']);

$file = $_REQUEST['file'];
//echo 'File uploaded: <a href="' . $file . '">' . $file . '</a>'; 

?>

<!DOCTYPE html>   
<html lang="en">   
<head>   
<meta charset="utf-8">   
<title>Crypto-Book Black Box</title>   
<meta name="description" content="weak">   
<link href="../../assets/css/bootstrap.css" rel="stylesheet">  

</head>  
<body>  

<form class='form-horizontal' enctype="multipart/form-data" action="sign.php?file=<? echo $file ?>" method="POST">
        <fieldset>  
 <legend>Enter Facebook homepages of people you want to be in your anonymity set (one per line).
<br>
For example: <br>
<i>

<a href="https://www.facebook.com/avi.silberschatz.7">https://www.facebook.com/avi.silberschatz.7</a>
<br>
<a href="https://www.facebook.com/vladimir.rokhlin">https://www.facebook.com/vladimir.rokhlin</a>
<br><!--
<a href="https://www.facebook.com/baford">https://www.facebook.com/baford</a>
<br>-->
<a href="https://www.facebook.com/joan.feigenbaum">https://www.facebook.com/joan.feigenbaum</a>
</i>

</legend>

<!--
	   <div class="control-group">  
            <label class="control-label" for="area">File:</label>  
            <div class="controls">  
		<input name="uploaded" type="file" /><br />
            </div>  
          </div>  
-->
       


          <div class="control-group">  
		
	     <label class="control-label" for="area">Enter Facebook homepages:</label>  
            <div class="controls">  
		<textarea id="comments" name="comments" rows="10" cols="700"></textarea>

<!--
              <input class="input-xlarge" id="area" rows="5" name="age"></input>  
-->
            </div>  
          </div>  


          <div class="form-actions">  
		 <!--<input type="submit" value="Upload" />-->


		<button name="send" type="submit" class="btn btn-primary">Sign file <? echo str_replace('uploads/', '', $file) ?> &raquo</button>  
<!--   <input  type="submit" value="" />-->
            <!--<button class="btn">Cancel</button>  
			-->
          </div>  
        </fieldset> 

</form>  
</body>  
</html>  




<!--
Uncomment to display user profile pic
<img src="https://graph.facebook.com/<?php echo $user; ?>/picture">
-->
