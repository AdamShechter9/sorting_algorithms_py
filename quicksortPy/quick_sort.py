# Quick sort
# Quick sort written in python.
# partitions the array according to a pivot value in the middle.
# sends the left right to be partitioned, and right side to be partitioned.
# when the recursive function returns, it "merges" the split arrays with the pivot in the center.

# Adam Shechter

from random import randint
from datetime import datetime


def quick_sort(inlist):
    if not inlist:
        return inlist
    if len(inlist) < 2:
        return inlist

    # setting smart pivot
    # picks the median of three values in the center.
    pivotidx = int((len(inlist) - 1) / 2)

    if len(inlist) > 4:
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

    pivot = inlist[pivotidx]

    # partition
    index = 0
    count = 0
    end = len(inlist)
    while count < end:
        # if value is less than pivot
        if inlist[index] < pivot:
            # if value is to the right, move to the left
            if index > pivotidx:
                item = inlist.pop(index)
                inlist.insert(0, item)
                pivotidx += 1
        # if value is greater than pivot
        elif inlist[index] > pivot:
            # if value is to the left, move to the right
            if index < pivotidx:
                item = inlist.pop(index)
                inlist.insert(end, item)
                pivotidx -= 1
                index -= 1
        index += 1
        count += 1

    # partition
    leftlist = inlist[0:pivotidx]
    rightlist = inlist[pivotidx + 1:]

    # recursive call
    outlist = quick_sort(leftlist) + [pivot] + quick_sort(rightlist)
    return outlist

# random function to generate sorting numbers.
def random_list(n):
    outlist = []
    for i in range(n):
        outlist.append(randint(0, 10000))
    return outlist


# feeding random lists to sort
rndLst= random_list(10)
print "to be sorted\n", rndLst
t1 = datetime.now()
sortedList = quick_sort(rndLst)
t2 = datetime.now()
print "sorted\n", sortedList
print "Time to selection sort: ", t2-t1
print "# of elements: ", len(rndLst)

rndLst= random_list(100)
print "to be sorted\n", rndLst
t1 = datetime.now()
sortedList = quick_sort(rndLst)
t2 = datetime.now()
print "sorted\n", sortedList
print "Time to selection sort: ", t2-t1
print "# of elements: ", len(rndLst)

rndLst= random_list(10500)
t1 = datetime.now()
sortedList = quick_sort(rndLst)
t2 = datetime.now()
print "Time to selection sort: ", t2-t1
print "# of elements: ", len(rndLst)
