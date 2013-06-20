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
		  <h2>Step 1</h2>
		  <p>First you need to download the desktop signing app.
		  </p>
		  <p><a class='btn' href='dsa/keygen/signer.zip'>Download app &raquo;</a></p>
        </div>

        <div class="span4">
		  <h2>Step 2</h2>
		  <p>Unzip the app. To run the app you will need <a href="http://www.python.org/">Python 2.7</a> installed.</p>
			<p>To sign your file run the following from command line:</p>
		<p><code>python2.7 signer.py [token] [other IDs] [file]</code></p>
		<p><code>[token]</code> is your <a href="gettoken.php">unique personal access token</a></p>
<!--		<p><? echo $token ?></p>
-->
		<p><code>[other IDs]</code> is a list of Facebook IDs (from their Facebook homepage eg. https://www.facebook.com/avi.silberschatz.7 ) of other people you want in your anonymity set, for example: avi.silberschatz.7</p>
		<p><code>[file]</code> is the filename that you want to sign.</p>
		<p><b>Example usage:</b></p>
		<p><code>python2.7 signer.py CAAB3xIlFqK0BAJQ22FsdvHZABnUZCRpyc<br>
		DZsVbOI4yEj3iARai6PUZAZAnXMFT1mZAVmkOXPbS9VD8RfuDTMDhf<br>
		wZAnjzT4rrSxKdt5pVriAjZBO9DINs7I5V99EFeQ7mCY0b2z0uVKfZ<br>
		BykP5NLXkt66HLUZCIJ6xwI0ZD avi.silberschatz.7 <br>vladimir.rokhlin joan.feigenbaum document.pdf</code></p>
        </div>

	 <div class="span4">
		  <h2>Step 3</h2>
		  <p>After you run the app, a signature file will be generated, for example <code>document.pdf.sig</code> and saved in the same directory as the original file.<p>
		<p>The signature along with the original file can now be <a href="http://mahan.webfactional.com/dsa/keygen/verify.php">verified</a> by a third party as having been signed by a member of your anonymity set, but they will not be able to unmask who specifically signed it.</p>
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
