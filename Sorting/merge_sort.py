

def merge_sort(l):
    print("Splitting ",l)
    n = len(l)
    if n>1:   
        #Divide input array by half
        mid = n//2
        leftSubArray = l[:mid]
        rightSubArray = l[mid:]
        merge_sort(leftSubArray)
        merge_sort(rightSubArray)
        
        #Combine divided arrays back
        i=j=k=0       
        while i < len(leftSubArray) and j < len(rightSubArray):
            if leftSubArray[i] < rightSubArray[j]:
                l[k]=leftSubArray[i]
                i=i+1
            else:
                l[k]=rightSubArray[j]
                j=j+1
            k=k+1

        while i < len(leftSubArray):
            l[k]=leftSubArray[i]
            i=i+1
            k=k+1

        while j < len(rightSubArray):
            l[k]=rightSubArray[j]
            j=j+1
            k=k+1
            
    print("Merging ",l)

l = [5, 2, 4, 6, 1, 3, 7, 6, 899, 20, 45, 31]
print(f"Original list is: {l}")
merge_sort(l)
print(f"Sorted list is {l}")
