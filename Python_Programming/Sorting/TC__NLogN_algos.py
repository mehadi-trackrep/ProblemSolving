class QuickSort:
    def __init__(self, arr):
        self.arr = arr
        self.length = len(arr)

    def quick_sort(self, low, high):
        if low < high:
            pivot_index = self.partition(low, high)
            self.quick_sort(low, pivot_index-1)
            self.quick_sort(pivot_index+1, high)

    def partition(self, low, high) -> int:
        print("YYYY")
        """
            pivot is the first element, we have to place it in its correct position
            so that all the elements to the left of pivot are smaller than pivot
            and all the elements to the right of pivot are greater than pivot
            -----------------------------------------------------------------------
            we may take the last element as pivot and also any arbitrary element as pivot
        """
        
        pivot = self.arr[high]
        i = low - 1 # i is the index of smaller element

        for j in range(low, high):
            if self.arr[j] <= pivot:
                i += 1
                ## swap the ith & jth element
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        ## swap the (i+1)th & high element (pivot)
        self.arr[i+1], self.arr[high] = self.arr[high], self.arr[i+1]
        
        return i+1 # i+1 is the correct position of pivot, as the 0 to i the elements are <= pivot


class HeapSort:
    """
    V.V.I. ==> In binary tree representation for heap tree - we consider the 0th element as root
        then it's left child will be 1th element
        & the right child will be 2th element
        So, the formula:-
            if a parent node is ith element, then its
                left child will be: 2*i + 1 & 
                right child will be: 2*i + 2
    ---------------------------------------------------------
    And for max heap / min heap we will have 2 properties:-
        1. structural property (it should be an almost complete binary tree (ACBT) / CBT)
        2. ordering property (max heap / min heap conditions)
    ----------------------------------------------------------
        Approach:-
            1. Build a max heap from the input data. (taking the array as a binary representation of a tree)
            2. Now iterate from the last element of the array to the first element of the array
                2.1. swap the root element with the last element of the array, as 
                    the root element is the largest element of the array in current state.
                    And the root element is sorted & placed in the last index of the array.
                    
                    E.x. if total elements/nodes = N, so indices - (0, 1, 2, ... N-1)
                    ---
                    Iteration - 1: the root (largest element, as it's a max heap) is placed 
                                   in the (N-1)th index of the array.
                                and then the step 2.2: heapify(arr, N-1, 0) # N-1 is the n(nodes) we will consider
                                                      means now try to max heapify from 
                                                      0th index to N-2th index, as N-1 index is sorted already.

                2.2 again heapify the array from the 0th element (root) upto the last unsorted element.
    """
    def __init__(self, arr):
        self.arr = arr
        self.N = len(arr) ## n(nodes) = N == length
    
    def heap_sort_using_max_heapify(self):
        ## step 1: build a max heap tree at first
        for i in range(self.N//2 - 1, -1, -1): ## start from the last parent node (N//2 - 1) to the root node (0)
            self.heapify(self.N, i) # O(logN)
        ## step 2: now iterate from the last element to the first element O(N)
        for i in range(self.N-1, -1, -1):
            ## swap the root element with the last unsorted ith element of the array
            self.arr[0], self.arr[i] = self.arr[i], self.arr[0]
            ## heapify the array from the 0th element (root) upto the last unsorted element.
            self.heapify(i, 0)
    
    def heapify(self, N, ith_node): ## ith node == ith element, N == total nodes except the sorted nodes
        """
            here, N will be from 0 to the last unsorted element's index
            E.X. if N = 7 then
            iteration - 1: 0 to 6
            iteration - 2: 0 to 5
            iteration - 3: 0 to 4
            iteration - 4: 0 to 3
            iteration - 5: 0 to 2
            iteration - 6: 0 to 1
            iteration - 7: 0 to 0
        """

        largest_node = ith_node

        left_child = 2*ith_node + 1
        right_child = 2*ith_node + 2

        if left_child < N and self.arr[largest_node] < self.arr[left_child]:
            largest_node = left_child
        if right_child < N and self.arr[largest_node] < self.arr[right_child]:
            largest_node = right_child
        
        if largest_node != ith_node:
            # swap the ith_node (root) with the largest_node means the largest element will be the root node now.
            self.arr[largest_node], self.arr[ith_node] = self.arr[ith_node], self.arr[largest_node]
            self.heapify(N, largest_node) ## we need again heapify as in the largest_node the parent index have been a lower value than childs might be.

if __name__ == '__main__':
    # arr = [3,2,3,1,2,4,5,5,6]
    # qs = QuickSort(arr)
    # print("cccc")
    # qs.quick_sort(0, len(arr)-1)
    # print(qs.arr)

    arr = [3,2,3,1,2,4,5,5,6]
    hs = HeapSort(arr)
    print("cccc")
    hs.heap_sort_using_max_heapify()
    print(hs.arr)