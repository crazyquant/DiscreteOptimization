import numpy
import os


def solveIt(inputData):
    lines = inputData.split('\n')
    a, b = map(list, zip(*(s.split(" ") for s in lines)))
    print(a)
    print(b)
    return lines


inputFileName = "inputData1.dat"
inputFileName = "datafile/" + inputFileName

f = open(inputFileName, "r")

solveIt(f.read())

