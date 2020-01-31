import os

if os.name == "nt":
	os.system("cls")
else:
	os.system("clear")

def tool1():
	mylist = input("Give me some sitelist or iplist : ")
	try:
		hosts = open(mylist,"r").read().splitlines()
		for host in hosts:
			print("Scanning --> " + host)
			try:
				r = requests.get("http://api.hackertarget.com/reverseiplookup/?q=" + host)
				if "error check your search parameter" in r.text or "No DNS A records" in r.text:
					print("Bad response --> " + host)
				elif "API count exceeded" in r.text:
					print("API count exceeded! Change your IP with VPN and enter!")
					input()
				else:
					sites = r.text
					sites = sites.replace("webmail.", "")
					sites = sites.replace("mail.", "")
					sites = sites.replace("cpanel.", "")
					sites = sites.replace("whm.", "")
					sites = sites.replace("www.", "")
					sites = sites.replace("autodiscover.", "")
					sites = sites.replace("webdisk.", "")
					sites = sites.replace("ns.", "")
					sites = sites.replace("ns1.", "")
					sites = sites.replace("ns2.", "")
					sites = sites.replace("smtp.", "")
					sites = sites.replace("smtp2.", "")
					sites = sites.replace("admin.", "")
					sites = sites.replace("hostmaster.", "")
					with open("grabbedtest.txt","a") as f:
						f.write(sites + "\n")
					lines_seen = set()
					outfile = open('grabbed.txt', "a")
					infile = open('grabbedtest.txt', "r")
					for line in infile:
						print(line)
						if line not in lines_seen:
							outfile.write(line)
							lines_seen.add(line)
					outfile.close()
					infile.close()
					if os.name == "nt":
						os.system("del grabbedtest.txt")
					else:
						os.system("rm -rf grabbedtest.txt")
			except:
				pass
	except:
		print("File not found!")
		
		
def tool2():
	ip = input("Give me example IP for range : ")
	start = input("Start : ")
	end = input("End : ")
	try:
		ex = ip.split(".")
		for i in range(int(start),int(end)):
			exx = ex[3].replace(ex[3],str(i))
			host = ex[0] + "." + ex[1] + "." + ex[2] + "." + exx
			print("Scanning --> " + host)
			r = requests.get("http://api.hackertarget.com/reverseiplookup/?q=" + host)
			if "error check your search parameter" in r.text or "No DNS A records" in r.text:
				print("Bad response --> " + host)
			elif "API count exceeded" in r.text:
				print("API count exceeded! Change your IP with VPN and enter!")
				input()
			else:
				sites = r.text
				sites = sites.replace("webmail.", "")
				sites = sites.replace("mail.", "")
				sites = sites.replace("cpanel.", "")
				sites = sites.replace("whm.", "")
				sites = sites.replace("www.", "")
				sites = sites.replace("autodiscover.", "")
				sites = sites.replace("webdisk.", "")
				sites = sites.replace("ns.", "")
				sites = sites.replace("ns1.", "")
				sites = sites.replace("ns2.", "")
				sites = sites.replace("smtp.", "")
				sites = sites.replace("smtp2.", "")
				with open("grabbedtest.txt","a") as f:
					f.write(sites + "\n")
				lines_seen = set()
				outfile = open('grabbed.txt', "a")
				infile = open('grabbedtest.txt', "r")
				for line in infile:
					print(line)
					if line not in lines_seen:
						outfile.write(line)
						lines_seen.add(line)
				outfile.close()
				infile.close()
				if os.name == "nt":
					os.system("del grabbedtest.txt")
				else:
					os.system("rm -rf grabbedtest.txt")
				
			i += 1	
	except:
		pass
	

print("""
            _                      _             _   ___  
 _ __  _ __(_)_   ____ _ _ __ __ _| |__   __   _/ | / _ \ 
| '_ \| '__| \ \ / / _` | '__/ _` | '_ \  \ \ / / || | | |
| |_) | |  | |\ V / (_| | | | (_| | |_) |  \ V /| || |_| |
| .__/|_|  |_| \_/ \__, |_|  \__,_|_.__/    \_/ |_(_)___/ 
|_|                |___/   

[+] Coded by NinjaCR3      
[+] Get Million Sites in minutes!
[+] Contact : fb.com/100018879071666                             
""")

try:
	import requests
except:
	print("[-] Requests module not found! Please install requests module and run script again!")
	
tool = input("[1] Get from list\n[2] IP Range\n\nTool : ")
if tool == "1":
	tool1()
elif tool == "2":
	tool2()
else:
	pass