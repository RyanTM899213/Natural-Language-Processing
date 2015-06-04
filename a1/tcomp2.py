##################################
# Comp Sci 4750 - NLP            #
# Assignment # 1 Q2              #
# submitted to: Todd Wareham     #
# submitted by: Ryan Martin      #
# login name: rtm773             #
# student number: 201039054      #
# due date: Sept. 19/14          #
##################################

import sys 
import string

numargs = len(sys.argv)

if numargs < 4:
    print "usage: python tcomp2.py filename file1name file2name ..."
    sys.exit()
    
# counts the TOTAL number of words that occur unquely in first file
# or second file. the number of words that occur in X that do not occur
# in Y) + (the number of words that occur in Y that do not occur in X)
# *please note: Python is picky about passing references of files to functions
# already opened in main as I found out, so I've passed the index of the current 
# file I want to compare denoted by i as the argument in functions below. 
def sd(i):
    file1 = open(sys.argv[1])  # master text file
    file2 = open(sys.argv[i])
    dicA = getWords(file1)  # file1 aka X
    dicB = getWords(file2)  # file2 aka Y
    summ = 0  # number of words that occur in two files together
    
    for key in dicA:
        if key in dicB:
            continue
        else:
            summ += 1
            
    for key in dicB:
        if key in dicA:
            continue
        else:
            summ += 1
    file1.close()
    file2.close()             
    return summ
    
# counts the number of DIFFERENT words that occur in the file given
def numWords(i):
    f = open(sys.argv[i])
    list = []
    for line in f:
        words = trimPunctuation(line).split() # trim punctuation
        for w in words:
            if w in list:
                continue
            else:
                list.append(w) 
    f.close()          
    return float(len(list))                   

# remove all punctuation
def trimPunctuation(strng):
    return strng.translate(string.maketrans("",""), string.punctuation)
        
# similar to above function, but returns the dictionary instead.
# I passed the reference to files here and it seemed to work, but 
# anywhere else I got incorrect results.  
def getWords(f):
    dic = {}
    for line in f:
        words = trimPunctuation(line).split() # trim punctuation
        for w in words:
            if w in dic:
                continue
            else:
                dic[w] = 0
    return dic
    
def Sim(i):
    return "%.3f" % (1.0 - ( sd(i) / ( numWords(1) + numWords(i) )) )
  

if __name__ == '__main__':  
  
    j = 2  # start at first comparison file
    largestvalue = 0.0
    largestfile = ''

    while j < numargs:
        sim = Sim(j)

        print ">>> Sim(" + sys.argv[1] + ", " + sys.argv[j] + ") = " + str(sim)
        if sim > largestvalue:
            largestvalue = sim
            largestfile = sys.argv[j]
    
        j += 1
    
    print "File \"" + largestfile + "\" is most similar to \"" + sys.argv[1] + "\""









    




               
