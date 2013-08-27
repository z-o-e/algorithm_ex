"""'kargerMinCut.txt' contains the adjacency list representation of a simple undirected graph. 
   There are 200 vertices labeled 1 to 200. The first column in the file represents the vertex label, 
   and the particular row (other entries except the first column) tells all the vertices that 
   the vertex is adjacent to. So for example, the 6th row looks like : "6  155  56  52  120......". 
   This just means that the vertex with label 6 is adjacent to (i.e., shares an edge with) the vertices 
   with labels 155,56,52,120,......,etc. 
   Task is to code up and run the randomized contraction algorithm for the min cut problem and use it 
   on the above graph to compute the min cut. 
"""

import random
import copy
import math

def karger_min_cut(arr):
    while(len(arr)>2):
        # randomly pick two vertices
        u_index=random.randint(0,len(arr)-1)
        u=arr[u_index][0]
        v=random.choice(arr[u_index][1:])
        for i in range(len(arr)):
            if arr[i][0]==v:
                v_index=i   # search for v_index
                break
        # merge uv
        while v in arr[u_index]:
            arr[u_index].remove(v) # delete v(s)
        for x in arr[v_index][1:]:
            if x!=u: # avoid self loop
                arr[u_index].append(x)
        # replace v values with u
        for i in range(len(arr)):
            if i!=u_index:
                for j in range(1,len(arr[i])):
                    if arr[i][j]==v:
                        arr[i][j]=u
        # delete node v
        del arr[v_index]
    # count cuts
    cuts=len(arr[0])-1
    for i in range(1,len(arr[0])):
        if arr[0][i]==arr[0][0]: # deduct self-loop
            cuts=cuts-1
    return cuts

if __name__=="__main__":
    import sys
    f=open(sys.argv[1],'r').readlines()
    # strip tab and newline
    f=[f[i].split() for i in range(len(f))]
    # convert to integer
    for i in range(len(f)):
	    for j in range(len(f[i])):
	        f[i][j]=int(f[i][j])
    # run n*log(n) times to ensure that success is (1-1/n)
    #n=len(f)
    #run_time=int(n*math.log(n))
    arr=copy.deepcopy(f)    # lists are mutable, this is to prevent deprecate the original data
    min_cut=karger_min_cut(arr)
    for i in range(10):
        arr=copy.deepcopy(f)
        cut=karger_min_cut(arr)
        if cut<min_cut:
            min_cut=cut
    print min_cut
        
    
        
    

    
    
    
    
