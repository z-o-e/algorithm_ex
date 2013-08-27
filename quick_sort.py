""" 'QuickSort.txt' contains all of the integers between 1 and 10,000 (inclusive, with no repeats) in unsorted order. 
    The integer in the ith row of the file gives you the ith entry of an input array. 
    Task is to compute the total number of comparisons used to sort the given input file by QuickSort. As you know, 
    the number of comparisons depends on which elements are chosen as pivots, so explore three different pivoting rules. You should not count comparisons one-by-one. Rather, when there is a recursive call on a subarray of length m, you should simply add m−1 to your running total of comparisons. (This is because the pivot element is compared to each of the other m−1 elements in the subarray in this recursive call.)
"""

from random import randint
 
def part(a, left, right,count): #left and right are the start and end indixes of the subarray

##    choose random pivot
##    pivot = randint(left, right)
##    a[left], a[pivot] = a[pivot], a[left]
 
    
   
##    choose first element in subarray as pivot
##    pivot = a[left]


##    choose last element in subarray as pivot
##    pivot=a[right]
##    temp=a[left]
##    a[left]=pivot
##    a[right]=temp


##    choose median of first,last and middle element of the subarray as pivot
    first=a[left]
    last=a[right]
    if (right-left+1)%2==0:
        mid=a[left+(right-left+1)//2-1]
    else:
        mid=a[left+(right-left+1)//2]
        
    pivot=sorted([first,last,mid])[1]

    if pivot==mid:
        temp=a[left]
        a[left]=pivot
        if (right-left+1)%2==0:
            a[left+(right-left+1)//2-1]=temp
        else:
            a[left+(right-left+1)//2]=temp
    if pivot==last:
        temp=a[left]
        a[left]=pivot
        a[right]=temp


##  initialize i,j
        
    i = left + 1
     
    for j in range(left + 1, right + 1):
        count+=1
        if a[j] < pivot:
            a[j], a[i] = a[i], a[j]
            i += 1            
             
    pos = i - 1
    a[left], a[pos] = a[pos], a[left]
     
    return pos,count#new pivot position. Used to determine the next left and right side of the
 

 
def quick_sort(a, left, right,count):
 
    if left < right: 
        pivot_pos,count = part(a, left, right,count )
        #recursively call quick_sort on left and right
        count=quick_sort(a, left, pivot_pos - 1,count)
        count=quick_sort(a, pivot_pos + 1, right,count)
    return count

 
if __name__ == '__main__':

    import sys
    f=open(sys.argv[1],'r')
    arr=f.readlines()
    arr=[int(x) for x in arr]

    count=quick_sort(arr, 0, len(arr) - 1,0)
    print (count)
