##################################
# Comp Sci 4750 - NLP            #
# Assignment # 1 Q1              #
# submitted to: Todd Wareham     #
# submitted by: Ryan Martin      #
# login name: rtm773             #
# student number: 201039054      #
# due date: Sept. 19/14          #
##################################

import sys 
import string

numargs = len(sys.argv)  

if numargs < 5:
    print "usage: python tcomp1.py filename n file1name file2name ..."
    sys.exit()
    
if int(sys.argv[2]) < 2:
    print "n too small (n < 2)"
    sys.exit()
    
def doFrequencies(dic):  # sums all values and divides each one by the sum
    summ = diff(dic)
    for key in dic:
        dic[key] /= float(summ)  
        
def diff(comp):  # sums all values of a dictionary
    summ = 0.0
    for key in comp:
        summ += comp[key]
    return summ    

n = int(sys.argv[2])    
master = open(sys.argv[1])  # sys.argv[0] is .py file!
mastdict = {}  # master dictionary
j = 0  # used for indexing within dictionary

for line in master:
    words = line.replace(",","").split()  # split each line by whitespace and remove commas
    for w in words:
        if len(w) < n:
            continue
        else:
            mastdict[str(j)] = w  # dictionary of indexes as keys and values as words from file
            j += 1
           
mastngrams = {}  # frequency matrix of the master file
            
for key in mastdict:
    value = mastdict[key]
    slength = len(value) 
    for i in range(0,slength):  # full string
        if (slength - i) < n:
            break  # exit
        if value[i:i+n] in mastngrams:
            mastngrams[value[i:i+n]] += 1
        else:
            mastngrams[value[i:i+n]] = 1
                     
doFrequencies(mastngrams) 
master.close()  # close file since we have its data   
x = 3
list = []  # list of dictionaries
gramslist = []  # list of dictionaries that hold n-grams 
 
while x < numargs:  # look through each comparison file 
    f = open(sys.argv[x])
    comps = {}
    y = 0
    for line in f: 
        words = line.replace(",","").split() # remove unnecessary characters  # change!**
        for w in words:
            if len(w) < n:
                continue  # skip words too small
            else:
                comps[str(y)] = w
                y += 1
    f.close()  # close file when finished          
    list.append(comps)               
    
    ngrams = {}  # dictionary of ngrams
    for key in comps:
        value = comps[key]
        slength = len(value)
        for i in range(0,slength):  # full string
            if (slength - i) < n:
                break  # exit
            if value[i:i+n] in ngrams:
                ngrams[value[i:i+n]] += 1
            else:
                ngrams[value[i:i+n]] = 1
    doFrequencies(ngrams)    # get relative frequencies
    gramslist.append(ngrams)
    x += 1             

i = 3  # index starting at first comparison file
largestvalue = 0.0
largestfile = ''

for dic in gramslist:  # for each dictionary in the list of comps dicts
    mastncopy = {}
    for key in mastngrams:   # make a copy of master which contains the union of each comp and mast file
        mastncopy[key] = mastngrams[key]
    for key in dic:
        try:
            x = mastncopy[key]
            x -= dic[key]
            if x < 0:
                x *= -1  # if negative, make positive -- abs value
            mastncopy[key] = x    
        except KeyError:
            mastncopy[key] = dic[key]
    difference = ("%.3f" % (1.0 - (diff(mastncopy) / 2.0)))        
    print ">>> Sim(" + sys.argv[1] + ", " + sys.argv[i] + ") = " + str(difference)
    
    if difference > largestvalue:
        largestvalue = difference
        largestfile = sys.argv[i]

    i += 1
        
print "File \"" + largestfile + "\" is most similar to \"" + sys.argv[1] + "\""
