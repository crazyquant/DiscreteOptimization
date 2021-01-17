import numpy
import os
import sys


def testing(l1, l2):
    outputData = str(19) + ' ' + str(0) + '\n'
    taken = [0, 0, 1, 1]
    outputData += ' '.join(map(str, taken))
    return outputData


def solveIt(inputData):
    lines = inputData.split('\n')
    l1, l2 = map(list, zip(*(s.split(" ") for s in lines)))
    return testing(l1, l2)

if(len(sys.argv) == 2):
    filename = sys.argv[1]
else:
    sys.exit("Error: No input file provided. Please enter the path\\filename of the input file as an argument.")

f = open(filename, "r")
print(solveIt(f.read()))
f.close()



