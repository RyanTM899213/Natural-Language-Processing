##################################
# Comp Sci 4750 - NLP            #
# Assignment #2                  #
# submitted to: Todd Wareham     #
# submitted by: Ryan Martin      #
# login name: rtm773             #
# student number: 201039054      #
# due date: Nov. 5/14            #
##################################
# * Please note: I have designed my FST state transitions with input/output, or 
# lower/upper string style. 

import sys, string

if len(sys.argv) < 2:
    print "usage: python reconstruct.py <filename>.fst ..."
    sys.exit()
    
# toString equivalent for the FST supplied    
def printFST(F):  # prints FST
    for outer in F:
        print ">>> outer " + str(outer)
                    
        for middle,value in F[outer].iteritems():
            print ">> middle: " + middle
                
            for vals in value:
                print "> inner: " + vals
                print "inner value: " + str(value[vals])
     
     
global currstate
# reads in a file, stores the data as FST and returns
# the dictionary containing the FST and all its states           
def readFST(filename):
    global currstate
    currstate = 1
    read = open(filename,"r")  # file to read
    lexicon = []  # list of acceptable lexicon values
    fst = {}  # dictionary holding an FST
    firstLine = read.readline()  # first line of the file
    firstlinevalues = firstLine.split()
    numStates = int(firstlinevalues[0])
    alphabet = firstlinevalues[1]
    
    for char in alphabet:
        lexicon.append(char)  # populate lexicon list
    
    for line in read:  # for remaining lines of the file
        print line
        array = line.split()
        try:  # try to cast to integer
            first = int(array[0])
        except ValueError:
            first = array[0]  # the string    
        if type(first) is int:
            fst[str(currstate)] = {}
            currentFST = fst[str(currstate)]  # fst[str(first)]
            currstate += 1
        # *Note: the FSTs are assumed to be deterministic, therefore we will not have duplicate
        # key entries in the dictionaries or their sub dictionaries! *    
        elif (array[0] in lexicon) and (array[1] in lexicon):  # check that the l/U is in lexicon
        # set lower value as key and new dict as value
                       # *make sure to check whether the inner value is an int or a '-' for epsilon*
            currentFST[array[0]] = {array[1] : array[2]}               
                               
    printFST(fst)  # print fst values  
    return fst                    
   
   
global composedFSTs  # declared out here in case I need to use later   
def createPermutationStates(F1, F2):
    global composedFSTs
    composedFSTs = {}  # initialize the dictionary
    for keyf1 in F1.keys():  # for each F1 key
        for keyf2 in F2.keys():  # for each F2 key
            composedFSTs[keyf1+keyf2] = {}  # create new sub-dictionaries with permutated keys
            
    printFST(composedFSTs)  # print composed FST
    return composedFSTs     
         
         
def existsin(F, lower):  # returns true iif upper variable is a lower in F
    for outer in F:
        for middle, value in F[outer].iteritems():
            if middle == lower:
                return True
    return False
    
    
def existsinupper(F, upper):
    for outer in F:
        for middle, value in F[outer].iteritems():
            for vals in value:
                if vals == upper:
                    return True
    return False
    
    
def getlower2(F, upper):
    for outer in F:
        for middle, value in F[outer].iteritems():
            for vals in value:
                if vals == upper:
                    return middle  # return lower string
    return None
    
def getlower3(F, lower, upper):    
    for outer in F:
        for middle, value in F[outer].iteritems():
            for vals in value:
                if vals == upper and middle == lower:
                    return middle  # return lower string
    return None                                            


def getupper2(F, lower):  # returns the upper string of the given lower from F
    for outer in F:
        for middle, value in F[outer].iteritems():
            if middle == lower:
                for val in value:
                    return val        
    return None  # None is null in python!
    
    
def getupper3(F, lower, upper):
    for outer in F:
        for middle, value in F[outer].iteritems():
            if middle == lower:
                for val in value:
                    if val == upper:
                        return val
    return None                                               
                                           

def getnextstate(F, lower, upper):
    for outer in F:
        for middle, inner in F[outer].iteritems():
            if middle == lower:
                for vals in inner:
                    if upper == vals:
                        return inner[vals]
                        

def inserttransition(fst, insstate, lower, upper, state):  # inserts new transition into the fst supplied
    fst[insstate] = {lower:{upper:state}}  # inserts necessary info.
    
         
def composeFST(F1, F2):
    fst = createPermutationStates(F1,F2)
    q1 = 1  # fist state to enter for transition starts at 1
    for outer in F1:  # below, middle is the lower string!
        q2 = 1
        for middle,value in F1[outer].iteritems():  # iterate through the 'middle' elements # value is reference to inner key and value
            upper = value.keys()[0]  # upper string value.keys().next()
            if existsin(F2, upper):  # if upper exists in F2's lower
                lower = middle                           # value.iteritems().next() is F1's upper
                upperval = getupper2(F2, upper)  # get the upper string of F2 given a lower value, here called upper
                f1state = value[upper]
                f2state = getnextstate(F2, upper, upperval)  # gets the next state given F2, a lower string(here called upper) and upper string
                combinedstate = f1state + f2state
                # now insert (lower/upperval) with next state combinedstate from the state, state
                state = str(q1) + str(q2)  # insert values below into q1q2 state
                inserttransition(fst, state, lower, upperval, combinedstate)
                if q2 >= len(F2):
                    q2 = q2 % len(F2)
                q2 += 1
        q1 += 1  # update counters indicating (going-from) states
    print "========================="
    print "composed FST: "
    printFST(fst)
    print "========================="
    return fst


#def createTrieFST(filename):  



def reconstructUpper(l,F):  # * lexical is lower! *
    print "Upper of string l: "
    state = str(1)  #  start state is 1
    for i in range(len(l)):
        if existsin(F, l[i]):
            lower = l[i]
            upper = getupper3(F, state, lower)
            print upper
            state = getnextstate(F, lower, upper)  # update state


def reconstructLower(u,F):
    print "Lower of string u: "
    state = str(1)
    for i in range(len(u)):
        if existsinupper(F, u[i]):
            upper = u[i]
            lower = getlower3(F, state, upper)
            print lower
            state = getnextstate(F, lower, upper)  

          
if __name__ == '__main__':
    d1 = readFST(sys.argv[1])
    d2 = readFST(sys.argv[1])
    print "====================="
    composed = composeFST(d1,d2)
    reconstructUpper("abac", d1)
    reconstructLower("bab", d2)
    

