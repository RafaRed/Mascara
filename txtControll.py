import config
import re

def setLastQuery(query, locate):
    f=open(locate,'w+')
    f.write(query)
    f.close();

def setQuery(query, locate):
    f=open(locate,'w+')
    f.write("query="+"\""+query+"\"")
    f.close();


def loadWordList(locate):
    wordlist = []
    print("loading wordlist..")
    with open(locate) as fi:
        for line in fi:
            wordlist.append(line)
    fi.close()
    return wordlist

def writeInFile(text, locate):
    f=open(locate,'a+')
#print (f.readline())
    l=[]
    l.append(text+'\n')
    l.append(f.readline())
    l.append(f.readline())

    for line in l:
        data = line.split(" ")
        for word in data:
            word = word.replace(" ","")
            pattern = re.compile("([a-z]*[A-Z]*[0-9]*]*)\w{3,7}");
            if(pattern.match(word)):
                with open(locate) as fi:
                    found = False
                    for line in fi:  #iterate over the file one line at a time(memory efficient)
                        if (re.search(word,line)):
                            found = True
                    if(found == False):
                        f.write(word+'\n')
                fi.close()


    f.close()
def checkBlackList(text):
    text2 = text.split(' ')
    with open(config.blacklistDir, 'r+') as inF:
        for word in text2:
            for line in inF:
                if word in line:
                    return True
        return False
