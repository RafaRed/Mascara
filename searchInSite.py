from bs4 import BeautifulSoup
import re
import requests
import random
import txtControll
import time

# Return just words, ignore random stuff
def returnWords(word,max):
    list = 0;
    wordList = ['','','','',''];
    for w in word:
        if(list < max):
            pattern = re.compile("([a-z]*[A-Z]*]*)\w{1,}");
            if(pattern.match(w)):
                wordList[list] = pattern.match(w).group();
                list += 1;
    return wordList;


def getLinkedWord(url, word):
    url = str(url)
    # Check if there is http in url
    if(re.search("http",url)):
        try:
            r  = requests.get(url)
        except:
            return -1;
        data = r.text
        # Get all usefull text from url
        soup = BeautifulSoup(data, "html.parser")
        # Ignore these texts..
        [s.extract() for s in soup(['style', 'script', '[document]', 'head'])]
        visible_text = soup.getText()

        # Split search query
        secret = word.split(' ');
        b = False
        # Get a random query word to search on site.
        while (b == False):
            secret = secret[random.randint(0,len(secret)-1)]
            pattern = re.compile("([a-z]*[A-Z]*[0-9]*]*)\w{1,}");
            if(pattern.match(secret)):
                b = True
        # Try to found words linked to the random select query
        Text = re.search(secret+"(.*)", visible_text)
        # If cant, get the first 4 letter + word found.
        if(Text is None):
            Text = re.search("([a-z]*[A-Z]*[0-9]*]*)\w{4,}", visible_text)

        try:
            # Get the new 1 ~ 5 querys.
            wl = returnWords(Text.group().split(' '),random.randint(1,5));
            query = wl[0]+" "+wl[1]+" "+wl[2]+" "+wl[3]+" "+wl[4]+" ";
            query = query.replace("  "," ")
            if(query != "    " and txtControll.checkBlackList(query) == False):
                print("\nData found: " + query + " :)")
                driver.find_element_by_xpath("//a[contains(@href,url)]").click()

                time.sleep(5)
                # Return the new querys to save on wordlist
                return query;
            else:
                return -1;
        except:
            return -1;

    else:
        return -1;
