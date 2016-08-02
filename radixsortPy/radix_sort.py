# Adam Shechter
# Radix Sort
# radix sorts by the digits (or letters) moving from rightmost to leftmost.

from random import randint
from datetime import datetime


def radix_sort(inlist):
    if len(inlist) == 0:
        return False
    
    # copy list to new list for work. (for non-destructive).
    worklist = inlist
    # get maximum number in array.  This is to know how many digits we will need to sort.
    maxnum = max(worklist)
    # multiplier is our counter to be multiplied by 10 every pass.
    multiplier = 10

    while (maxnum * 10) > multiplier:
        # empty digit buckets list
        digitlist = [[], [], [], [], [], [], [], [], [], []]
        for x in worklist:
            # truncates the number down
            sortdigit = x % multiplier
            # gets our single digit we'll be sorting with
            sortdigit //= (multiplier / 10)
            digitlist[sortdigit].append(x)
        worklist = []
        # parsing the numbers back to the list.
        for i in range(0, 9):
            for j in range(0, len(digitlist[i])):
                worklist.append(digitlist[i][j])
        # increasing multiplier.  (could do a pow(10, i) if we wanted).
        multiplier *= 10
    return worklist


def random_list(n):
    outList = []
    for i in range(n):
        outList.append(randint(0, 10000))
    return outList

# feed arrays to sort
rndList = random_list(500)
t1 = datetime.now()
sortedlist = radix_sort(rndList)
t2 = datetime.now()
print "Time to selection sort: ", t2-t1
print "# of elements: ", len(rndList)


rndList = random_list(50500)
t1 = datetime.now()
sortedlist = radix_sort(rndList)
t2 = datetime.now()
print "Time to selection sort: ", t2-t1
print "# of elements: ", len(rndList)
