##################################
# Comp Sci 4750 - NLP            #
# Assignment # 1 Q3              #
# submitted to: Todd Wareham     #
# submitted by: Ryan Martin      #
# login name: rtm773             #
# student number: 201039054      #
# due date: Sept. 19/14          #
##################################

import sys 
import string

if len(sys.argv) != 4:
    print "usage: python index1.py word1.txt text1.txt index1.txt"
    sys.exit()
    
def trimPunctuation(strng):
    return strng.translate(string.maketrans("",""), string.punctuation)    
    
def putToDict(i): # open file with index i and line number j
    dic = {}
    f = open(sys.argv[i])
    j = 1
    for line in f:
        words = trimPunctuation(line).split() # trim punctuation
        for w in words:
            if w in dic:
                dic[w] = str(dic[w]) + " " +str(j)    
            else:
                dic[w] = j
        j += 1        
    f.close()            
    return dic

    
if __name__ == '__main__':

    text = putToDict(2)
    ignore = putToDict(1)
    write = open(sys.argv[3],"w")
    usable = {}
    sys.stdout = write  # redirect standard output to file
    
    for word in text:
        if word in ignore:
            continue
        else:    
            usable[word] = text[word]
    
    list = []
    for word in usable:
        list.append(word)
        
    sortedlist = sorted(list)
    
    for word in sortedlist:
        print word + ": " + str(usable[word])
