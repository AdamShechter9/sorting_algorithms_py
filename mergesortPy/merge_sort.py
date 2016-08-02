# Merge sort
# Merge sort implemented in python using recursion.
# Fragments the list into 1 element lists.
# As lists are returned using recursion, it merges the arrays while sorting the final array.
# Adam Shechter

from random import randint
from datetime import datetime


def merge_sort(inlist):
    if not inlist:
        return inlist
    if len(inlist) == 1:
        return inlist

    mid_index = int(len(inlist) / 2)
    leftlist = inlist[0:mid_index]
    rightlist = inlist[mid_index:]

    # sending lists to be broken up further recursively, until they are one element each.
    leftlist = merge_sort(leftlist)
    rightlist = merge_sort(rightlist)

    i = 0
    j = 0
    outlist = []
    # merging and sorting.
    while (i < len(leftlist)) or (j < len(rightlist)):
        if (i < len(leftlist)) and (j < len(rightlist)):
            if leftlist[i] <= rightlist[j]:
                outlist.append(leftlist[i])
                i += 1
            else:
                outlist.append(rightlist[j])
                j += 1
        else:
            if i >= len(leftlist):
                outlist.append(rightlist[j])
                j += 1
            else:
                outlist.append(leftlist[i])
                i += 1

    return outlist

def random_list(n):
    outlist = []
    for i in range(n):
        outlist.append(randint(0, 10000))
    return outlist


# feeding random lists to sort
rndLst= random_list(30)
print "to be sorted\n", rndLst
t1 = datetime.now()
sortedList = merge_sort(rndLst)
t2 = datetime.now()
print "sorted\n", sortedList
print "Time to selection sort: ", t2-t1
print "# of elements: ", len(rndLst)


rndLst= random_list(150)
t1 = datetime.now()
sortedList = merge_sort(rndLst)
t2 = datetime.now()
print "Time to selection sort: ", t2-t1
print "# of elements: ", len(rndLst)

rndLst= random_list(10500)
t1 = datetime.now()
sortedList = merge_sort(rndLst)
t2 = datetime.now()
print "Time to selection sort: ", t2-t1
print "# of elements: ", len(rndLst)