<?php
$sig = $_REQUEST['sig'];
$file = $_REQUEST['file'];
$weak = exec('python2.7 verifier.py ' . $sig . ' ' . $file);


$weak = str_replace("file was signed by one of the following: ","", $weak);
$weak = str_replace("[","", $weak);
$weak = str_replace("]","", $weak);
$weak = str_replace(",","", $weak);
//echo $weak;
 $pieces = explode("' '", $weak);

for($i = 0; $i < count($pieces); $i++){
	//if(strlen($pieces[$i]) > 1){
		$pieces[$i] = '<a href="http://www.facebook.com/' . $pieces[$i] . '">' . $pieces[$i] . '</a>';
	//}
}
$weak = implode("<br>", $pieces);
$weak = str_replace(" '","", $weak);
$weak = str_replace("'","", $weak);

?>

<br><br>


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
    <link href="../../assets/css/bootstrap-responsive.css" rel="stylesheet">

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

<?php
include("../../header.html");
?>
  
    <div class="container">

      <!-- Example row of columns -->
      <div class="row">
		<div class="span8">
          <h3>Document was leaked by one of the following people</h3>
<br>
<p><? echo($weak); ?></p>
<br>
           <p><a class="btn" href="index.php">Home &raquo;</a></p>
        </div>
      </div>
      <hr>

    <?php
include("../../footer.html");
?>
  
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




