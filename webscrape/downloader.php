<?php
if($_GET[get]){
	exec("./downloader.sh");
}


?>

<!DOCTYPE html>
<html>
<head>
	<title>Download Ming Downloader</title>
</head>
<style>
	input{
		
	}
</style>
<body>
	<h1>Download Any Song Here</h1>
	<form action="downloader.php">
		<label for="songlink">Enter the Link</label>
		<input type="text" placeholder="Enter The Link For Download Ming">
		<input type="submit" value="Get Songs" name="get">
	</form>
	

</body>
</html>