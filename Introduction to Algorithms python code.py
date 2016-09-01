#插入排序算法
def insertionSort(alist):
    start_time = time.time()
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index
        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position-1
        alist[position]=currentvalue
    print time.time() - start_time
alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)

#选择排序

def selectionSort(alist):
    for fiilslot in range(len(alist)-1,0,-1):
        positionOfMax = 0
        for location in range(1,fiilslot + 1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        temp = alist[fiilslot]
        alist[fiilslot] = alist[positionOfMax]
        alist[positionOfMax] = temp


#合并排序
def mergeSort(alist):
    print("Splitting",alist)
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1
        print("Merging",alist)

#冒泡算法

def bubbleSort(alist):
    for i in range(len(alist)-1,0,-1):
        for j in range(i):
            if alist[j] > alist[j + 1]:
                temp  = alist[j]
                alist[j] = alist[j + 1]
                alist[j + 1] = temp



##quicksort 1

def quicksort(array):
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return quicksort(less)+equal+quicksort(greater)# Just use the + operator to join lists
        # Note that you want equal ^^^^^ not pivot
    else:# You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array

##quicksort 2

def quicksort(alist):
    if not alist:
        return []
    pivots = [x for x in alist if x == alist[0]]
    less = quicksort([x for x in alist if x < alist[0]])
    greater = quicksort([x for x in alist if x > alist[0]])
    return less + pivots + greater

#Max Subarray Naive
#works for all numbers ,even all negative.

def MaxSubarray(alist):
    if alist is None or len(alist) == 0:
        return 0
    maxSum = alist[0]
    miniSum = 0
    sum = 0
    for x in alist:
        sum += x
        if sum - miniSum > maxSum:
            maxSum = sum - miniSum
        if sum < miniSum:
            miniSum = sum
    return maxSum

#Max Subarray Naive 2 
#doesn't work for all negative numbers ,just return 0

def MaxSubarray(alist):
    max = 0
    sum = 0
    for x in alist:
        sum += x
        if sum < 0:
            sum = 0
        elif (max < sum):
            max = sum
    return max


#Max Subarray D&C

def MaxCrossingSubarray(a,low,mid,high):
    leftSum = None
    maxLeft = 0
    sum1 = 0
    for i in range(mid,low - 1, -1):
        sum1 = sum1 + a[i]
        if None == leftSum:
            leftSum = sum1
            maxLeft = i
        elif sum1 > leftSum:
            left_sum = sum1
            maxLeft = i
    rightSum = None
    sum2 = 0
    maxRight = 0
    for j in range(mid + 1,high + 1):
        sum2 = sum2  + a[j]
        if None == rightSum:
            rightSum = sum2
            maxRight = j
        elif sum2 > rightSum:
            rightSum = sum2
            maxRight = j
    return maxLeft,maxRight,leftSum + rightSum

def MaximumSubarray(a,low,high):
    mid = (low + high)/2
    leftSum = a[low]
    rightSum = a[high]
    if high == low:
        return low,high,a[low]
    else:
        mid == (low + high)/2
        leftLow,leftHigh,leftSum = MaximumSubarray(a,low,mid)
        rightLow,rightHigh,rightSum = MaximumSubarray(a,mid + 1,high)
        crossLow,crossHigh,crossSum = MaxCrossingSubarray(a,low,mid,high)
        if leftSum >= rightSum and leftSum >= crossSum:
            return leftLow,rightHigh,rightSum
        elif rightSum >= leftSum and rightSum >= crossSum:
            return  rightLow,rightHigh,rightSum
        else:
            return crossLow,crossHigh,crossSum
MaximumSubarray(a,0,len(alist) - 1)




