import os,sys
try:
	import requests
except:
	print("[-] Requests module not found! Please install requests module and run script again!")
	sys.exit()
if os.name == "nt":
	os.system("cls")
else:
	os.system("clear")
print("""
	SubDomain Scanner
	Coded by NinjaCR3
	Twitter --> @Ninja3Sec
""")
ip = input("Target Server/Site : ")
kaydet = input("Save results? (E - yes / H - no) : ")
print("")
print("Searching...")
print("")
r = requests.get("https://api.hackertarget.com/hostsearch/?q=" + ip)
data = r.text
data = data.replace(",","  |  IP  ==>  ")
print(data)
if kaydet == "E":
	try:
		with open(ip + "_result.txt","a") as f:
			f.write(data)
		print("Saved as " + ip + "_result.txt")
	except:
		print("Save process failed!")
else:
	pass