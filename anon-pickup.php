<!DOCTYPE html>   
<html lang="en">   
<head>   
<meta charset="utf-8">   
<title>Crypto-Book Black Box</title>   
<meta name="description" content="weak">   
<link href="assets/css/bootstrap.css" rel="stylesheet">  

</head>  
<body>  

<?php
//include("header.html");
?>

<form class='form-horizontal' enctype="multipart/form-data" action="email/distribute-keys.php" method="POST">
        <fieldset>  

<legend>
<!--
Anonymous key pickup

<br>-->
Enter email addresses of everyone you want in your anonymity set (remember to include your email). <!--(does not have to be the same as ring signature publication anonymity set).-->
<br>
</legend>

 <div class="control-group">  
		
	     <label class="control-label" for="area">Enter email addresses:</label>  
            <div class="controls">  
		<textarea id="comments" name="comments" rows="10" cols="100"></textarea>


            </div>  
          </div>  


          <div class="form-actions">  
		<button name="send" type="submit" class="btn btn-primary">Distribute keys &raquo</button>  

          </div>  
        </fieldset>  
</form>

<!--
<?php
include("footer.html");
?>
-->

</body>
