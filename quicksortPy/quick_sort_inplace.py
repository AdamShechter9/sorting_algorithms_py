# Quick sort
# Quick sort (in-place) written in python.
# this one works in place on the list.
# if left value is greater than pivot, it is inserted at the end index.
# if right value is greater, it is inserted at start index.
# might check in the future if maybe doing a value swap is faster than popping and inserting elements.

# Adam Shechter

from random import randint
from datetime import datetime

def quick_sort(inlist, start_idx=None, end_idx=None):
    if not inlist:
        return inlist
    if (start_idx is None) and (end_idx is None):
        start_idx = 0
        end_idx = len(inlist) - 1
    if start_idx >= end_idx:
        return inlist
    if start_idx < 0 or end_idx > len(inlist):
        return inlist

    # setting smart pivot
    # picks the median of three values in the center.

    pivotidx = int((start_idx + end_idx) / 2)
    if (end_idx - start_idx) > 4:
        if inlist[pivotidx] > inlist[pivotidx - 1]:
            if inlist[pivotidx] > inlist[pivotidx + 1]:
                if inlist[pivotidx - 1] < inlist[pivotidx + 1]:
                    pivotidx -= 1
                else:
                    pivotidx += 1
            elif inlist[pivotidx] <= inlist[pivotidx + 1]:
                pivotidx = pivotidx
        elif inlist[pivotidx] < inlist[pivotidx - 1]:
            if inlist[pivotidx] >= inlist[pivotidx + 1]:
                pivotidx = pivotidx
            elif inlist[pivotidx] < inlist[pivotidx + 1]:
                if inlist[pivotidx + 1] < inlist[pivotidx - 1]:
                    pivotidx += 1
                else:
                    pivotidx -= 1

    # partition
    pivot = inlist[pivotidx]
    index = start_idx
    count = 0
    end = end_idx - start_idx
    while count < end:
        # if value is less than pivot
        if inlist[index] < pivot:
            # if value is to the right, move to the left
            if index > pivotidx:
                item = inlist.pop(index)
                inlist.insert(start_idx, item)
                pivotidx += 1
        # if value is greater than pivot
        elif inlist[index] > pivot:
            # if value is to the left, move to the right
            if index < pivotidx:
                item = inlist.pop(index)
                inlist.insert(end_idx, item)
                pivotidx -= 1
                index -= 1
        index += 1
        count += 1

    # recursive call
    inlist = quick_sort(inlist, start_idx, pivotidx - 1)
    inlist = quick_sort(inlist, pivotidx + 1, end_idx)
    return inlist


# random function to generate sorting numbers.
def random_list(n):
    outlist = []
    for i in range(n):
        outlist.append(randint(0, 10000))
    return outlist


# feeding random lists to sort
rndLst= random_list(50)
print "to be sorted\n", rndLst
t1 = datetime.now()
sortedList = quick_sort(rndLst)
t2 = datetime.now()
print "sorted\n", sortedList
print "Time to selection sort: ", t2-t1
print "# of elements: ", len(rndLst)

rndLst= random_list(500)
t1 = datetime.now()
sortedList = quick_sort(rndLst)
t2 = datetime.now()
print "Time to selection sort: ", t2-t1
print "# of elements: ", len(rndLst)

rndLst= random_list(10500)
t1 = datetime.now()
sortedList = quick_sort(rndLst)
t2 = datetime.now()
print "Time to selection sort: ", t2-t1
print "# of elements: ", len(rndLst)
