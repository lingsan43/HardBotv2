import threading
from queue import Queue
import requests
import os

type1 = 'type="text"'
type2 = 'type="password"'
type3 = 'type="email"'
type4 = 'type=email'
type5 = "Index of /"
type6 = 'type="file"'
type7 = 'type=file'
type8 = 'type=text'
type9 = 'type=password'
hata1 = 'input[type="password"]'
hata2 = 'input[type="email"]'
hata3 = 'input[type="text"]'
hata4 = 'input[type="file"]'
hata5 = 'input[type=password]'
hata6 = 'input[type=email]'
hata7 = 'input[type=text]'
hata8 = 'input[type=file]'
hata9 = '[type="password"]'
hata10 = '[type="email"]'
hata11 = '[type="text"]'
hata12 = '[type="file"]'
hata13 = '[type=password]'
hata14 = '[type=email]'
hata15 = '[type=text]'
hata16 = '[type=file]'

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

 Priv8 Tool 2018 with threads :)
 Coded by NinjaCR3
""")
sitelistesi = input("[*] Site list : ")
threadsayi = input("[*] Threads : ")
kaydet = input("[*] Save results ? (E - yes / H - no) : ")
print("""
""")

print_lock = threading.Lock()

def sitescan(domain):
	try:
		try:
			r = requests.get(domain, timeout=80)
		except:
			pass
		document = r.text
		document = document.replace(hata1,"")
		document = document.replace(hata2,"")
		document = document.replace(hata3,"")
		document = document.replace(hata4,"")
		document = document.replace(hata5,"")
		document = document.replace(hata6,"")
		document = document.replace(hata7,"")
		document = document.replace(hata8,"")	
		document = document.replace(hata9,"")
		document = document.replace(hata10,"")
		document = document.replace(hata11,"")
		document = document.replace(hata12,"")
		document = document.replace(hata13,"")
		document = document.replace(hata14,"")
		document = document.replace(hata15,"")
		document = document.replace(hata16,"")					
		document = document.replace("admin/index.php?route=common/dashboard","")
		if type2 in document or type3 in document or type4 in document or type5 in document or type6 in document or type7 in document or type8 in document or type9 in document:
			if "login login-action-login wp-core-ui" in r.text:
				if "http://" in str(r.url):
					print(domain + " [ WordPress ]")
				else:
					url = domain.replace("http://","https://")
					print(url + " [ WordPress ]")
				if kaydet == "E":
					with open("wpjoomla.txt","a") as f:
						if "http://" in str(r.url):
							f.write(domain + " [ WordPress ]" + "\n")
						else:
							url = domain.replace("http://","https://")
							f.write(url + " [ WordPress ]" + "\n")
				else:
					pass
			elif "admin/index.php?route=common/login" in document:
				if "http://" in str(r.url):
					print(domain + " [ OpenCart ]")
				else:
					url = domain.replace("http://","https://")
					print(url + " [ OpenCart ]")
				if kaydet == "E":
					with open("opencart.txt","a") as f:
						if "http://" in str(r.url):
							f.write(domain + " [ OpenCart ]" + "\n")
						else:
							url = domain.replace("http://","https://")
							f.write(url + " [ OpenCart ]" + "\n")
				else:
					pass
			elif "Joomla!" in document:
				if "http://" in str(r.url):
					print(domain + " [ Joomla ]")
				else:
					url = domain.replace("http://","https://")
					print(url + " [ Joomla ]")
				if kaydet == "E":
					with open("wpjoomla.txt","a") as f:
						if "http://" in str(r.url):
							f.write(domain + " [ Joomla ]" + "\n")
						else:
							url = domain.replace("http://","https://")
							f.write(url + " [ Joomla ]" + "\n")
				else:
					pass
			elif type1 in document and type2 in document:
				if "<title>Page not found" in document or "Nothing found" in document or "<title>Sayfa bulunamadı" in document or "bir şey bulunamadı</title>" in document:
					pass
				else:
					if "http://" in str(r.url):
						print(domain)
					else:
						url = domain.replace("http://","https://")
						print(url)
					if kaydet == "E":
						with open(str(sitelistesi) + "_results.txt","a") as f:
							if "http://" in str(r.url):
								f.write(domain + "\n")
							else:
								url = domain.replace("http://","https://")
								f.write(url + "\n")
					else:
						pass
			elif type8 in document and type9 in document:
				if "<title>Page not found" in document or "Nothing found" in document or "<title>Sayfa bulunamadı" in document or "bir şey bulunamadı</title>" in document:
					pass
				else:
					if "http://" in str(r.url):
						print(domain)
					else:
						url = domain.replace("http://","https://")
						print(url)
					if kaydet == "E":
						with open(str(sitelistesi) + "_results.txt","a") as f:
							if "http://" in str(r.url):
								f.write(domain + "\n")
							else:
								url = domain.replace("http://","https://")
								f.write(url + "\n")
					else:
						pass								
			elif type2 in document and type3 in document:
				if "<title>Page not found" in document or "Nothing found" in document or "<title>Sayfa bulunamadı" in document or "bir şey bulunamadı</title>" in document:
					pass
				else:
					if "http://" in str(r.url):
						print(domain + " [ Email ]")
					else:
						url = domain.replace("http://","https://")
						print(url + " [ Email ]")
					if kaydet == "E":
						with open(str(sitelistesi) + "_results.txt","a") as f:
							if "http://" in str(r.url):
								f.write(domain + " [ Email ]" + "\n")
							else:
								url = domain.replace("http://","https://")
								f.write(url + " [ Email ]" + "\n")
					else:
						pass
			elif type4 in document and type9 in document:
				if "<title>Page not found" in document or "Nothing found" in document or "<title>Sayfa bulunamadı" in document or "bir şey bulunamadı</title>" in document:
					pass
				else:
					if "http://" in str(r.url):
						print(domain + " [ Email ]")
					else:
						url = domain.replace("http://","https://")
						print(url + " [ Email ]")
					if kaydet == "E":
						with open(str(sitelistesi) + "_results.txt","a") as f:
							if "http://" in str(r.url):
								f.write(domain + " [ Email ]" + "\n")
							else:
								url = domain.replace("http://","https://")
								f.write(url + " [ Email ]" + "\n")
					else:
						pass								
			elif type5 in document:
				if "http://" in str(r.url):
					if "php" in document:
						print(domain + " [ Directory - PHP File Have ]")
					elif "php5" in document:
						print(domain + " [ Directory - PHP5 File Have ]")
					elif "phtml" in document:
						print(domain + " [ Directory - PHTML File Have ]")
					else:
						print(domain + " [ Directory ]")
				else:
					url = domain.replace("http://","https://")
					if "php" in document:
						print(url + " [ Directory - PHP File Have ]")
					elif "php5" in document:
						print(url + " [ Directory - PHP5 File Have ]")
					elif "phtml" in document:
						print(url + " [ Directory - PHTML File Have ]")
					else:
						print(url + " [ Directory ]")
				if kaydet == "E":
					with open(str(sitelistesi) + "_results.txt","a") as f:
						if "http://" in str(r.url):
							if "php" in document:
								f.write(domain + " [ Directory - File Have ]" + "\n")
							elif "php5" in document:
								f.write(domain + " [ Directory - File Have ]" + "\n")
							elif "phtml" in document:
								f.write(domain + " [ Directory - File Have ]" + "\n")
							else:
								f.write(domain + " [ Directory ]" + "\n")
						else:
							url = domain.replace("http://","https://")
							if "php" in document:
								f.write(url + " [ Directory - PHP File Have ]" + "\n")
							elif "php5" in document:
								f.write(url + " [ Directory - PHP5 File Have ]" + "\n")
							elif "phtml" in document:
								f.write(url + " [ Directory - PHTML File Have ]" + "\n")
							else:
								f.write(url + " [ Directory ]" + "\n")
				else:
					pass
			elif type6 in document or type7 in document:
				if "http://" in str(r.url):
					print(domain + " [ Upload ]")
				else:
					url = domain.replace("http://","https://")
					print(url + " [ Upload ]")
				if kaydet == "E":
					with open(str(sitelistesi) + "_results.txt","a") as f:
						if "http://" in str(r.url):
							f.write(domain + " [ Upload ]" + "\n")
						else:
							url = domain.replace("http://","https://")
							f.write(url + " [ Upload ]" + "\n")
				else:
					pass
			else:
				pass
		else:
			pass	   	
	except:
		pass


def threader():
    while True:
        worker = q.get()
        sitescan(worker)
        q.task_done()

q = Queue()


for x in range(int(threadsayi)):
     t = threading.Thread(target=threader)
     t.daemon = True
     t.start()

siteler = open(sitelistesi, 'r').read().splitlines()

for worker in siteler:
    q.put(worker)

q.join()