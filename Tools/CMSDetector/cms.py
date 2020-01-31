import requests
from multiprocessing.dummy import Pool
import sys, os

if os.name == "nt":
	os.system("cls")
else:
	os.system("clear")
	
print("""
 [#] Simple CMS Detector v1.0
 [#] Coded by NinjaCR3
 [#] www.spyhackerz.org
""")

def scan(site):
	try:
		if "http" in site:
			url = site
		else:
			url = "http://" + site
		r = requests.get(url,timeout=20)
		if "/wp-content/" in r.text:
			print("WordPress ---> " + url)
			with open("wordpress.txt","a") as f:
				f.write(url + "\n")
		elif "Joomla!" in r.text or "index.php?option=com_" in r.text:
			print("Joomla ---> " + url)
			with open("joomla.txt","a") as f:
				f.write(url + "\n")			
		elif "index.php?route=common/home" in r.text:
			print("OpenCart ---> " + url)
			with open("opencart.txt","a") as f:
				f.write(url + "\n")
		elif "sites/default" in r.text:
			print("Drupal ---> " + url)
			with open("drupal.txt","a") as f:
				f.write(url + "\n")
		elif "prestashop" in r.text or "PrestaShop" in r.text:
			print("PrestaShop ---> " + url)
			with open("prestashop.txt","a") as f:
				f.write(url + "\n")
		elif "osCommerce" in r.text:
			print("osCommerce ---> " + url)
			with open("oscommerce.txt","a") as f:
				f.write(url + "\n")
		elif "vBulletin" in r.text:
			print("vBulletin ---> " + url)
			with open("vbulletin.txt","a") as f:
				f.write(url + "\n")
		elif "Mage.Cookies" in r.text:
			print("Magento ---> " + url)
			with open("magento.txt","a") as f:
				f.write(url + "\n")
		else:
			print("Not found ---> " + url)
			with open("othercms.txt","a") as f:
				f.write(url + "\n")
	except:
		print("Not working ---> " + site)

sitelist = input("Sitelist : ")
print("")

try:
	sites = open(sitelist,"r").read().splitlines()
	pp = Pool(50)
	pr = pp.map(scan,sites)
except:
	print("Sites not found!")
	sys.exit()