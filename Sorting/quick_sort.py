

def hoare_partition(l, lo, hi):
    pivot = l[lo] 
    i = lo
    j = hi
    print(f"Pivot is {pivot}")
    while True:
        while l[i] < pivot:
            i+=1
        while l[j] > pivot:
            j-=1
        if(i >= j):
            return j
        
        print(f"Exchange {l[i]} with {l[j]}")
        l[i], l[j] = l[j], l[i]
    


def lomuto_partition(l, lo, hi):
    pivot = l[hi] 
    i = lo - 1
    print(f"Pivot is {pivot}")

    for j in range(lo, hi):  
        if l[j] <= pivot:
            i += 1
            print(f"Exchange {l[i]} with {l[j]}")
            l[i], l[j] = l[j], l[i]  

    print(f"Exchange {l[i+1]} with {l[hi]}")
    l[i+1], l[hi] = l[hi], l[i+1]  

    print('Partition done')
    return i + 1 

def quicksort(l, lo, hi):
    if lo<hi:
        pivot_idx = lomuto_partition(l, lo, hi)
        quicksort(l, lo, pivot_idx-1)
        quicksort(l, pivot_idx+1, hi)


l = [5, 2, 4, 6, 1, 3, 7, 6, 899, 20, 45, 31]
print(f"Original list is {l}")
quicksort(l, 0, len(l)-1)
print(f"The sorted list is {l}")