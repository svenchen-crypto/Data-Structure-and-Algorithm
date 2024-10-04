
def bubble_sort(l):
    if len(l)==1 or l==None:
        return 
    
    n = len(l)
    for i in range(n):
        for j in range(0, n-i):
            if j+1 < n and l[j] >= l[j+1]:
                temp = l[j+1]
                l[j+1] = l[j]
                l[j] = temp


l = [5, 2, 4, 6, 1, 3, 7, 6, 899, 20, 45, 31]
bubble_sort(l)
print(l)