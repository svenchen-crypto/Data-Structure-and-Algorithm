
def max_heapify(l, N, i):

    largest = i

    #Get index of left child and right child
    left_child = 2*i+1
    right_child = 2*i+2

    if left_child<N and l[left_child]>l[largest]:
        largest = left_child
    
    if right_child<N and l[right_child]>l[largest]:
        largest = right_child

    #Left or child > parent, need to swap
    if largest!=i:
        print(f"Exchange {l[i]} with {l[largest]}")
        l[i], l[largest] = l[largest], l[i]
        max_heapify(l, N, largest)



def build_max_heap(l):
    if not l:
        return
    
    N = len(l)
    for i in range(len(l)//2, -1, -1):
        max_heapify(l, N, i)


def heapsort(l):
    build_max_heap(l)
    N = len(l)
    for i in range(N-1, 0, -1):
        l[i], l[0] = l[0], l[i]
        max_heapify(l, i, 0)


l = [5, 2, 4, 6, 1, 3, 7, 6, 899, 20, 45, 31]
heapsort(l)
print(l)