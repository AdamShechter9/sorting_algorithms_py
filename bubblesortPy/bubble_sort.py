# Implementing a simple bubble sort algorithm.
# Adam Shechter
# Coding Dojo

from random import randint
from datetime import datetime

x = [3, 12, 11, 7, 6, 10, 4, 8, 2, 13, 9, 1]


def bubble_sort(inlist):
    unsorted = True
    print "sorting this list"
    print inlist

    while unsorted:
        unsorted = False
        for i in range(1, len(inlist)):
            if inlist[i] < inlist[i-1]:
                inlist[i], inlist[i-1] = inlist[i-1], inlist[i]
                unsorted = True
                # print "Swapping"
    else:
        print "finished sorting."
    return inlist


def random_list(n):
    outlist = []
    for i in range(n):
        outlist.append(randint(0, 10000))
    return outlist


t1 = datetime.now()
sortedList = bubble_sort(x)
t2 = datetime.now()
print sortedList 
print "Time to bubble sort: ", t2-t1
print "# of elements: ", len(x)
rndLst = random_list(100)
t1 = datetime.now()
sortedList = bubble_sort(rndLst)
t2 = datetime.now()
print sortedList
print "Time to bubble sort: ", t2-t1
print "# of elements: ", len(rndLst)