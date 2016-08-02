# Insertion sort algorithm
# comparing a value with all previous numbers, and inserting in correct location.

# Adam Shechter

from random import randint
from datetime import datetime


def insertion_sort(inlist):
    if inlist[1] < inlist[0]:
        swap = inlist.pop(1)
        inlist.insert(0, swap)

    for i in range(2, len(inlist)):
        if inlist[i] < inlist[i-1]:
            for j in range((i-1), 0, -1):
                if inlist[i] >= inlist[j-1]:
                    element = inlist.pop(i)
                    inlist.insert(j, element)
                    break
            else:
                if inlist[i] < inlist[0]:
                    swap = inlist.pop(i)
                    inlist.insert(0, swap)
    return inlist


def random_list(n):
    outlist = []
    for i in range(n):
        outlist.append(randint(0, 10000))
    return outlist

rndLst = random_list(10)
print "to be sorted\n", rndLst
t1 = datetime.now()
sortedList = insertion_sort(rndLst)
t2 = datetime.now()
print "sorted\n", sortedList
print "Time to selection sort: ", t2-t1
print "# of elements: ", len(rndLst)

rndLst = random_list(100)
print "to be sorted\n", rndLst
t1 = datetime.now()
sortedList = insertion_sort(rndLst)
t2 = datetime.now()
print "Time to selection sort: ", t2-t1
print "# of elements: ", len(rndLst)
print "sorted\n", sortedList

