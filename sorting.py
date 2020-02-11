#insertion sort implementation in python


def insertionSort(arr):

    for i in range(1,len(arr)-1):

        hole=i
        value=arr[i]

        while(hole>0 or arr[hole-1]>value):
            arr[hole] = arr[hole-1]
            hole = hole-1


        arr[hole] = value


    return arr

print(insertionSort(([3,4,5,6,1])))


#less than pivot are pushed left to the partition index, pi will be adjusted accordingly. 

def partition(arr, start, end):
    pivot = arr[end]
    pindex = start

    for i in range(start, end-1):

        if arr[i] <= pivot:
            arr[i], arr[pindex] = arr[pindex], arr[i]
            pindex +=1

    arr[pindex], pivot = pivot, arr[pindex]

    return pindex

    

def quickSort(arr, start, end):

    if start<end:
        pi = partition(arr, start, end)

        quickSort(arr,start,pi-1)
        quickSort(arr,pi+1,end)

    
    return arr

print(quickSort([4,5,2,8,3],0,4))