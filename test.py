from numpy import *
import operator
from os import listdir


def file2matrix(filename):
    fr = open(filename)
    arrayOlines = fr.readlines()
    numberOfLines = len(arrayOlines)         #get the number of lines in the file
    returnMat = zeros((numberOfLines,3))        #prepare matrix to return
    classLabelVector = []                       #prepare labels return   
    index = 0
    for line in arrayOlines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index:] = listFromLine[0:3]
        classLabelVector.append(listFromLine[-1])
        index += 1
    for x in xrange(0,len(classLabelVector)):
        if classLabelVector[x] == 'largeDoses':
            classLabelVector[x] = 3
        elif classLabelVector[x] == 'smallDoses':
            classLabelVector[x] = 2
        elif classLabelVector[x] == 'didntLike':
            classLabelVector[x] =1
    return returnMat,classLabelVector

print file2matrix('datingTestSet.txt')