 # -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
import requests
import random
import searchInSite
import config
import query
import txtControll
import time
import os
import browsercookie
import urllib2
import GoogleSession
import requests

random_avalible = True;

# Return a random text from wordlist to join with stated query.
def getRandomData():
    afile = open(config.topDir,'r')
    line = next(afile)
    for num, aline in enumerate(afile):
      if random.randrange(num + 2): continue
      line = aline
    return(line)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait():
    randomTime = random.randint(config.timer,config.timerMax)
    while randomTime > 0:
        clear()
        print("Wait "+str(randomTime)+" Seconds")
        time.sleep(1)
        randomTime -= 1
    clear()

def init(word):
    clear()
    # Wait for random time, configure it.
    wait()
    # Search from query on google.
    print("Searching url..")
    url = "www.google.com.br/search?site=&source=hp&q=";
    q = word+" "+getRandomData();
    print("Current query: "+q)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.0; it-IT; rv:1.7.12) Gecko/20050915'}
    txtControll.setLastQuery(q,config.lastQueryDir)
    s = requests.Session()


    #r  = s.get("http://" +url+q, headers=headers, cookies={'GAPS': '1:59NH-PXMjnyIKfwda9RPWytK1iVgLQ:c6g05IxIkrDXzX3d'})

    nurl = "http://" +url+q
    #print nurl
    #cj = browsercookie.firefox()
    #opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    #login_html = opener.open(nurl).read()
    #print login_html


    url_login = "https://accounts.google.com/ServiceLogin"
    url_auth = "https://accounts.google.com/ServiceLoginAuth"
    session = GoogleSession.SessionGoogle(url_login, url_auth, config.user, config.passs)
    r = session.get(nurl)

    #print(r.cookies)
    #with open("r.txt",'w') as f:
    #    f.write(r.text.encode('utf-8'));
    #with open("r2.txt",'w') as f:
    #0    f.write(r2.text.encode('utf-8'));

    data = r
    soup = BeautifulSoup(data, "html.parser")
    data = [];
    # Get all links
    for link in soup.find_all('a'):
        result = link.get('href');
        if(re.search("url",result)):
            # Ignore webcache links
            if(not (re.search("webcache",result))):
                result = result.replace("/url?q=","")
                data.append(result.split('&sa')[0]);
    # Get a random url after filters.
    if(random_avalible):
        try:
            link = data[random.randint(0,len(data)-1)];
        except:
            print("error 0 ")
    print("Current link: " + str(link))
    # Load site and get new querys
    ret = searchInSite.getLinkedWord(link,q);
    if(ret != -1):
        # Write new querys found on worklist
        txtControll.writeInFile(ret,config.topDir);
        txtControll.setQuery(ret,config.configDir)


# Load wordlist on start
wordlist = txtControll.loadWordList(config.topDir)
for i in range(0,len(wordlist)):
    wordlist[i] = wordlist[i].replace('\n','')
# Start with an infinity loop.
while(True):
    #get a random word from wordlist.
    init(wordlist[random.randint(0,len(wordlist)-1)]);
