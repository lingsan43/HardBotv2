#~ HardBot v2
#~ Coded by NinjaCR3 & Monzera
#~ 2020 New Priv8 Bot :)
#~ 2020 New Priv8 and Best Exploits :)
#~ We don't accept any responsibility for any illegal usage!

import requests,os
from colorama import Fore,init

init(autoreset=True)

g = Fore.GREEN
r = Fore.RED
b = Fore.BLUE
w = Fore.WHITE

if os.name == "nt":
	os.system("cls")
else:
	os.system("clear")

banner = """
{}
  _   _               _ ____        _           ____  
 | | | | __ _ _ __ __| | __ )  ___ | |_  __   _|___ \    HardBot v2
 | |_| |/ _` | '__/ _` |  _ \ / _ \| __| \ \ / / __) |  {} Coders : {}NinjaCR3 {}&{} Monzera
 |  _  | (_| | | | (_| | |_) | (_) | |_   \ V / / __/   {} 2020 New Priv8 Tool
 |_| |_|\__,_|_|  \__,_|____/ \___/ \__|   \_/ |_____|
                    
 {}[{}+{}] Welcome to the BOT !
 [{}+{}] Available Exploits:   
 {}=============================={}
 [{}1{}] Subdomain Scanner
 [{}2{}] Best Google Dorker
 [{}3{}] Auto Exploiter Shell Upload Bot
 [{}4{}] WebDAV Exploiter
 [{}5{}] xFastBing
 [{}6{}] Multi CMS Brute Force
 [{}7{}] ServerScan
 [{}8{}] Drupal Exploiter Bot
 [{}9{}] JaguarV3 Bot
 [{}10{}] X4PriV8 Bot
 [{}11{}] LiteSpeed Config Grabber
 [{}12{}] Combo MD5 Decoder
 [{}13{}] Zombi Bot V11
 [{}14{}] Raiz0WorM Bot
 [{}15{}] PayPal Valid Email Checker
 [{}16{}] KingBoT [ JexBot New Update Edition ]
 [{}17{}] Very Fast CMS Detector
 [{}18{}] PrestaShop Auto Exploitor Bot
 [{}19{}] Laravel PHPUnit Shell Upload Bot
 [{}20{}] Priv Site Grabber 
"""

print(banner.format(g,b,g,w,r,b,g,r,g,r,g,r,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g))

tool = raw_input(g + "["+r+"*"+g+"] Choose tool : ")

if tool == "1":
	os.chdir("Tools/SubdomainScanner")
	os.system("python3 subdomain.py")
	
elif tool == "2":
	os.chdir("Tools/BestGoogleDorker")
	os.system("python priv8.py")
	
elif tool == "3":
	os.chdir("Tools/ICGAutoExploiterv2.5")
	scantype = raw_input("\n[1] Single Target\n[2] List Scan\n[3] Thread List Scan\n\n[*] Choose scan type : ")
	if scantype == "1":
		os.system("python icgAutoExploiter.py 1")
	elif scantype == "2":
		os.system("python icgAutoExploiter.py 2")
	elif scantype == "3":
		os.system("python icgAutoExploiter.py 3")
	else:
		pass
		
elif tool == "4":
	os.chdir("Tools/c4webdav")
	os.system("python3 c4webdav.py")
	
elif tool == "5":
	os.chdir("Tools/xFastBing")
	scantype = raw_input("\n[1] Grab fresh sites \n[2] Grab sites for scan SQL Injection\n\n[*] Choose scan type : ")
	if scantype == "1":
		os.system("python3 xfastbing1.py")
	elif scantype == "2":
		os.system("python3 xfastbing2.py")
	else:
		pass
		
elif tool == "6":
	os.chdir("Tools/Multi CMS Brute Force")
	os.system("python3 multi.py")
	
elif tool == "7":
	os.chdir("Tools/ServerScanPriv")
	os.system("python3 helper.py")
	raw_input("\n[*] Please enter...")
	os.system("python3 priv.py")
	
elif tool == "8":
	os.chdir("Tools/DrupalBot")
	sitelist = raw_input("\n[*] Sitelist  ==>  ")
	os.system("python drupalbot.py " + sitelist)
	
elif tool == "9":
	os.chdir("Tools/JaguarV3")
	os.system("python end.py")
	
elif tool == "10":
	os.chdir("Tools/X4PriV8")
	os.system("python X4PriV8.py")
	
elif tool == "11":
	os.chdir("Tools/LiteSpeedConfigGrabber")
	if os.name == "nt":
		os.system("cls")
		os.system("dir")
	else:
		os.system("clear")
		os.system("ls -la")		
	print("\n\n[!] Upload 'liteconfgrab.py' to server and run!\n    Usage : python liteconfgrab.py")
	
elif tool == "12":
	os.chdir("Tools/MD5Decode")
	os.system("python3 md5decode.py")
	
elif tool == "13":
	os.chdir("Tools/ZombiBotV11")
	os.system("python v11.py")
	
elif tool == "14":
	os.chdir("Tools/Raiz0WorM")
	sitelist = raw_input("\n[*] Sitelist  ==>  ")
	os.system("python bot.py " + sitelist)
	
elif tool == "15":
	os.chdir("Tools/PayPalChecker")
	os.system("python check.py")
	
elif tool == "16":
	os.chdir("Tools/KingBoT")
	sitelist = raw_input("\n[*] Sitelist  ==>  ")
	os.system("python3 KingBoT.py " + sitelist)
	
elif tool == "17":
	os.chdir("Tools/CMSDetector")
	os.system("python3 cms.py")
	
elif tool == "18":
	os.chdir("Tools/presta0day")
	os.system("python3 presta0day.py")
	
elif tool == "19":
	os.chdir("Tools/PHPUnitExploiter")
	os.system("python3 phpunit.py")
	
elif tool == "20":
	os.chdir("Tools/PrivGrab")
	os.system("python3 privgrab.py")	
else:
	pass
