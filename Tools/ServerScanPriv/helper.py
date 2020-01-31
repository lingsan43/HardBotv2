import os
if os.name == "nt":
	os.system("cls")
else:
	os.system("clear")
print("""
  ____                           ____                  
 / ___|  ___ _ ____   _____ _ __/ ___|  ___ __ _ _ __  
 \___ \ / _ \ '__\ \ / / _ \ '__\___ \ / __/ _` | '_ \ 
  ___) |  __/ |   \ V /  __/ |   ___) | (_| (_| | | | |
 |____/ \___|_|    \_/ \___|_|  |____/ \___\__,_|_| |_|

 Simple Helper
 Coded by NinjaCR3
""")
sitelistesi = input("[*] Site list : ")
siteler = open(sitelistesi, 'r').read().splitlines()
adminler = open("pages.txt", 'r').read().splitlines()
if os.name == "nt":
	os.system("del " + (str(sitelistesi)))
else:
	os.system("rm -rf " + (str(sitelistesi)))
for site in siteler:
	for admin in adminler:
		with open((str(sitelistesi)),"a") as f:
			f.write(site + "/" + admin + "\n")
print("[+] Complete :) -- " + (str(sitelistesi)))
