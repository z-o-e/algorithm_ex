""" 'IntegerArray.txt' contains all of the 100,000 integers between 1 and 100,000 (inclusive) in some order, 
    with no integer repeated.Task is to compute the number of inversions in the file given, where the ith row of 
    the file indicates the ith entry of an array. Because of the large size of this array, you should implement 
    the fast divide-and-conquer algorithm. 
"""
def merge_and_count(left,right):
    assert left==sorted(left) and right==sorted(right)
    output=[]
    count=0
    i,j=0,0
    while i<len(left) and j<len(right):
        if right[j]<left[i]:
            output.append(right[j])
            count+=len(left)-i  # number of elements left in the right half
            j+=1
        else:
            output.append(left[i])
            i+=1
    output+=left[i:]+right[j:] # append the ramainder of the list
    return count,output
    
def sort_and_count(arr):
    if len(arr)==1: return 0,arr
    n=len(arr)//2
    left,right=arr[:n],arr[n:]
    # iterate recursively
    lcount,left=sort_and_count(left)
    rcount,right=sort_and_count(right)
    rlcount,arr=merge_and_count(left,right)
    return rcount+lcount+rlcount,arr
    
if __name__=="__main__":
    import sys
    f=open(sys.argv[1],'r')
    arr=f.readlines()
    arr=[int(x) for x in arr]
    r=sort_and_count(arr)
    print 'number of inversions is: ',r[0]
