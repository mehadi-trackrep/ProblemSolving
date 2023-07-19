class QuickSort:
    def __init__(self, arr, k):
        self.arr = arr
        self.length = len(arr)
        self.k = k

    def quick_sort(self, low, high):
        if low == high:
            print(self.arr[low])
            return
        if low < high:
            
            pivot_index = self.partition(low, high)
            
            items_to_right_including_pivot = high - pivot_index + 1

            if items_to_right_including_pivot == self.k:
                print("## pivot_index: {}".format(pivot_index))
                print(self.arr[pivot_index])
                return
            elif items_to_right_including_pivot > self.k:
                print("==> pivot_index+1, high: {}, {}".format(pivot_index+1, high))
                self.quick_sort(pivot_index+1, high)
            else:
                print("--> low, pivot_index-1: {}, {}".format(low, pivot_index-1))
                self.quick_sort(low, pivot_index-1)
            

    def partition(self, low, high) -> int:
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
            if self.arr[j] < pivot:
                i += 1
                ## swap the ith & jth element
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        ## swap the (i+1)th & high element (pivot)
        self.arr[i+1], self.arr[high] = self.arr[high], self.arr[i+1]
        
        return i+1 # i+1 is the correct position of pivot, as the 0 to i the elements are <= pivot


if __name__ == '__main__':
    while True:
        arr = [3,2,3,1,2,4,5,5,6]
        k = int(input("Enter k: "))
        qs = QuickSort(arr, k)
        qs.quick_sort(0, len(arr)-1)
        print(qs.arr)
        if k > len(arr):
            print("k should be less than or equal to {}".format(len(arr)))
    # print(qs.arr)
