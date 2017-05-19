from bs4 import BeautifulSoup
import re
import requests
import random
import txtControll
import time

def returnWords(word,max):
    list = 0;
    wordList = ['','','','',''];
    for w in word:
        if(list < max):
            pattern = re.compile("([a-z]*[A-Z]*[0-9]*]*)\w{1,}");
            if(pattern.match(w)):
                wordList[list] = pattern.match(w).group();
                list += 1;
    #print(wordList)
    return wordList;


def getLinkedWord(url, word):
    url = str(url)
    if(re.search("http",url)):
        try:
            r  = requests.get(url)
        except:
            return -1;
        data = r.text
        soup = BeautifulSoup(data, "html.parser")
        [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
        visible_text = soup.getText()



        #Text = re.search(word, body);
        secret = word.split(' ');
        secret2 = " "
        b = False
        while (b == False):
            secret2 = secret[random.randint(0,len(secret)-1)]
            pattern = re.compile("([a-z]*[A-Z]*[0-9]*]*)\w{1,}");
            if(pattern.match(secret2)):
                b = True
        secret = secret2;

        #print("SECRET " + secret)
        Text = re.search(secret+"(.*)", visible_text)
        if(Text is None):
            Text = re.search("([a-z]*[A-Z]*[0-9]*]*)\w{4,}", visible_text)

        try:
            wl = returnWords(Text.group().split(' '),random.randint(1,5));
            query = wl[0]+" "+wl[1]+" "+wl[2]+" "+wl[3]+" "+wl[4]+" ";
            query = query.replace("  "," ")
            if(query != "    " and txtControll.checkBlackList(query) == False):
                print("\nData found: " + query + " :)")
                time.sleep(5)
                return query;
            else:
                return -1;
        except:
            return -1;

    else:
        return -1;

    #print ((checkWord(Text.group()).split(' ')[0])+" "+
    #       (checkWord(Text.group()).split(' ')[1])+" "+
    #       (checkWord(Text.group()).split(' ')[2]));
