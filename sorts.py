def selectionSort(ls):
    if len(ls) <= 1:
        return ls
    else:
        curr_min = 0
        end = len(ls)-1
        for fill in xrange(0, end):
            next = fill + 1
            for y in xrange(fill, end):
                if ls[next] < ls[curr_min]:
                    curr_min = next


                next += 1
            tmp = ls[fill]
            ls[fill] = ls[curr_min]
            ls[curr_min] = tmp
            fill += 1
            next = fill + 1
        return ls

#print selectionSort([3, 2, 5, 15, 7, 9, 1, 0])

def insertionSort(ls):
    if len(ls) <= 1:
        return ls
    else:
        end = len(ls)
        for nextPos in xrange(1,end):
            nextVal = ls[nextPos]
            while nextPos > 0 and ls[nextPos-1] > nextVal:
                ls[nextPos] = ls[nextPos-1]
                nextPos -= 1
            ls[nextPos] = nextVal
            print ls
        return ls

#print insertionSort([3, 2, 5, 15, 7, 9, 1, 0])

def bubbleSort(ls):
    if len(ls) <= 1:
        return ls
    else:
        swapped = True
        end = len(ls)
        while swapped == True and end != 1:
            swapped = False
            for pos in xrange(0,end-1):
                if ls[pos] > ls[pos+1]:
                    tmp = ls[pos]
                    ls[pos] = ls[pos+1]
                    ls[pos+1] = tmp
                    swapped = True
            end -= 1
        return ls

#print bubbleSort([3, 2, 5, 15, 7, 9, 1, 0])

def mergeSort(ls):
    if len(ls) <= 1:
        return ls
    else:
        mid = len(ls)/2
        left = mergeSort(ls[:mid])
        right = mergeSort(ls[mid:])
        left_pt = 0
        right_pt = 0
        length = len(left)+len(right)
        ret = [0]*length
        for x in xrange(len(left)+len(right)):
            if left_pt == len(left):
                ret[x] = right[right_pt]
                right_pt += 1
            elif right_pt == len(right):
                ret[x] = left[left_pt]
                left_pt += 1
            else:
                l = left[left_pt]
                r = right[right_pt]
                if l <= r:
                    ret[x] = l
                    left_pt += 1
                elif r < l:
                    ret[x] = r
                    right_pt += 1
        return ret

#print mergeSort([3, 2, 5, 15, 7, 9, 1, 0, 6])

def quickSort(ls):
    if len(ls) <= 1:
        return ls
    else:
        piv = (ls[0]+ls[-1])/2.0
        left = []
        right = []
        for each in ls:
            if each <= piv:
                left.append(each)
            else:
                right.append(each)
        ret_left = quickSort(left)
        ret_right = quickSort(right)
        return ret_left + ret_right

#print quickSort([3, 2, 5, 15, 7, 9, 1, 0, 6])









