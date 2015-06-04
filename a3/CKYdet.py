#########################################################
##  CS 4750 (Fall 2014), Assignment #3                 ##
##   Script File Name: CKYdet.py                       ##
##      Student Name: Ryan Martin                      ##
##         Login Name: rtm773                          ##
##              MUN #: 201039054                       ##
#########################################################

import sys, string

def getParse(grammar, utterance):

    for line in utterance:
        words = line.split()
        matrix = [[ [] for length in range(len(words))] for length in range(len(words)) ]  # initialize 2-d matrix
        
        for i in range(len(words)):
            for g in grammar:
                if words[i] in g[1]:
                    matrix[i][i].append(g)
                    
                    for g2 in grammar:
                        temp = g2[1]  # weird stuff
                        if g[0] in temp[0] and len(temp) == 1:  # and is important
                            matrix[i][i].append(g2)        
            print ">> " + str(i) + " " + str(i) + ": " + str(matrix[i][i])  # used in debugging
        print "-------------"
	# Now, I have the matrix with the stair elements as the words from the utterance
				

def getGrammar(f):

	gramList = []
	
	for line in f:
		sides = line.split(' -> ') # split line by arrow with spaces
		elements = [] 
		elements.append(sides[0]) 
		rightSide = sides[1].split() # split right hand side
		secondRightSide = []
		
		for right in rightSide:
			secondRightSide.append(right.replace('"',''))
			
		elements.append(secondRightSide)
		gramList.append(elements)

	return gramList

		
if __name__ == '__main__':
	
	test = open(sys.argv[1])  # open the two files
	utterancefile = open(sys.argv[2])
	listL = getGrammar(test)
	getParse(ListL, utterancefile)	
	test.close()  # close files
	utterancefile.close()
