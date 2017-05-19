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

random_avalible = True;

def getRandomData():
    afile = open(config.topDir,'r')
    line = next(afile)
    for num, aline in enumerate(afile):
      if random.randrange(num + 2): continue
      line = aline
    return(line)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def init(word):
    clear()
    print("Searching url..")
    time.sleep(random.randint(config.timer,config.timerMax))
    url = "www.google.com.br/search?site=&source=hp&q=";
    #url = "www.facebook.com/search/top/?q=";
    q = word+" "+getRandomData();
    print("Current query: "+q)
    txtControll.setLastQuery(q,config.lastQueryDir)
    r  = requests.get("http://" +url+q)

    data = r.text

    soup = BeautifulSoup(data, "lxml")
    data = [];
    for link in soup.find_all('a'):
        result = link.get('href');
        if(re.search("url",result)):
            if(not (re.search("webcache",result))):
                result = result.replace("/url?q=","")
                data.append(result.split('&sa')[0]);
    if(random_avalible):
        try:
            link = data[random.randint(0,len(data)-1)];
        except:
            print("error 0 ")
    print("Current link: " + str(link))
    ret = searchInSite.getLinkedWord(link,q);
    if(ret != -1):
        txtControll.writeInFile(ret,config.topDir);
        txtControll.setQuery(ret,config.configDir)
        #init(ret);
    print("ERROR")
wordlist = txtControll.loadWordList(config.topDir)
for i in range(0,len(wordlist)):
    wordlist[i] = wordlist[i].replace('\n','')
while(True):
    init(wordlist[random.randint(0,len(wordlist)-1)]);
