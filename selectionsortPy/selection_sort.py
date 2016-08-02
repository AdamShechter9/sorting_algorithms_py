# Selection sort
# simple selection sort written in python.
# uses minimum and maximum values to sort an array.
# keep adding sorted minimum values to the left, and adding sorted maximum values to the right.

# Adam Shechter


from random import randint
from datetime import datetime


def selection_sort(inlist):
    sortleftindex = 0
    sortrightindex = len(inlist)-1
    minValueIndex = 0
    minValue = inlist[minValueIndex]
    maxValueIndex = len(inlist)-1
    maxValue = inlist[maxValueIndex]

    while sortleftindex < sortrightindex:
        for i in range(sortleftindex, sortrightindex):
            if inlist[i] < minValue:
                minValue = inlist[i]
                minValueIndex = i
            elif inlist[i] > maxValue:
                maxValue = inlist[i]
                maxValueIndex = i
        # minimum sorting
        inlist[sortleftindex], inlist[minValueIndex] = inlist[minValueIndex], inlist[sortleftindex]
        sortleftindex += 1
        minValueIndex = sortleftindex + 1
        minValue = inlist[minValueIndex]
        # maximum sorting
        inlist[sortrightindex], inlist[maxValueIndex] = inlist[maxValueIndex], inlist[sortrightindex]
        sortrightindex -= 1
        maxValueIndex = sortrightindex - 1
        maxValue = inlist[maxValueIndex]

    return inlist

def random_list(n):
    outlist = []
    for i in range(n):
        outlist.append(randint(0, 10000))
    return outlist

rndLst= random_list(10)
print "to be sorted\n", rndLst
t1 = datetime.now()
sortedList = selection_sort(rndLst)
t2 = datetime.now()
print "sorted\n", sortedList
print "Time to selection sort: ", t2-t1
print "# of elements: ", len(rndLst)


rndLst= random_list(100)
print "to be sorted\n", rndLst
t1 = datetime.now()
sortedList = selection_sort(rndLst)
t2 = datetime.now()
print "sorted\n", sortedList
print "Time to selection sort: ", t2-t1
print "# of elements: ", len(rndLst)
