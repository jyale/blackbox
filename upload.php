

<!DOCTYPE html>   
<html lang="en">   
<head>   
<meta charset="utf-8">   
<title>Upload</title>   
<meta name="description" content="weak">   
<link href="assets/css/bootstrap.css" rel="stylesheet">  

</head>  
<body>  

<form class='form-horizontal' enctype="multipart/form-data" action="upload-backend.php" method="POST">
        <fieldset>  
 <legend>Please choose a file: </legend>

	   <div class="control-group">  
            <label class="control-label" for="area">File [filename cannot contain spaces]:</label>  
            <div class="controls">  
		<input name="uploaded" type="file" /><br />
            </div>  
          </div>  



<!--		  
          <div class="control-group">  
		
	     <label class="control-label" for="area">Enter your message:</label>  
            <div class="controls">  
              <input class="input-xlarge" id="area" rows="5" name="age"></input>  
            </div>  
          </div>  
-->

          <div class="form-actions">  
		 <!--<input type="submit" value="Upload" />-->


		<button type="submit" class="btn btn-primary">Upload</button>  

            <!--<button class="btn">Cancel</button>  
			-->
          </div>  
        </fieldset> 

</form>  
</body>  
</html>  