def insertion_sort(l):
    if(len(l)==1 or l==None):
        return 
    
    for j in range(1, len(l)):
        key = l[j]
        i = j-1

        #insert key to subarray [0:j]
        while(i>=0 and l[i]>key):
            l[i+1] = l[i]
            i=i-1
        l[i+1] = key


l = [5, 2, 4, 6, 1, 3, 7, 899, 20, 45, 31]
insertion_sort(l)
print(l)

