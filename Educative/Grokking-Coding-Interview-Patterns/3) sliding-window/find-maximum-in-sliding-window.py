# function to clean up the window
def clean_up(i, current_window, nums):
    # remove all the indexes from current_window whose corresponding values are smaller than or equal to the current element
    while current_window and nums[i] >= nums[current_window[-1]]:
        print(f"\t\tAs nums[{i}] = {nums[i]} is greater than or equal to nums[{current_window[-1]}] = {nums[current_window[-1]]},")
        print(f"\t\tremove {current_window[-1]} from current_window")
        del current_window[-1]

# function to find the maximum in all possible windows
def find_max_sliding_window(nums, w):
    # if the input array is empty, return an empty array
    if len(nums) == 0:
        return []
    
    # initializing variables
    output = []
    current_window = []

    # if window size is greater than the array size, set the window size to the array size
    if w > len(nums):
        w = len(nums)

    print("\n\tFinding the maximum in the first window:")
    
    # iterate over the first w elements
    for i in range(w):
        print(f"\tAdding nums[{i}] = {nums[i]} to the first window:\n\t\tInitial state of current_window: {current_window}")
        # for every element, remove the previous smaller elements from current_window
        clean_up(i, current_window, nums)

        # append the index of the current element to current_window
        current_window.append(i)
        print(f"\t\tFinal state of current_window: {current_window}")

    # appending the maximum element of the current window to the output list
    output.append(nums[current_window[0]])

    print("\n\tFinding the maximum in the remaining windows:")

    # iterate over the remaining input list
    for i in range(w, len(nums)):
        print(f"\tAdding nums[{i}] = {nums[i]} to current_window:\n\t\tInitial state of current_window: {current_window}")

        # for every element, remove the previous smaller elements from current_window
        clean_up(i, current_window, nums)

        # remove first index from the current_window if it has fallen out of the current window
        if current_window and current_window[0] <= (i - w):
            print(f"\t\tIndex {current_window[0]} has fallen out of the current window,")
            print(f"\t\tso, remove it")
            del current_window[0]

        # append the index of the current element to current_window
        print(f"\t\tAppending {i} to current_window")
        current_window.append(i)
        print(f"\t\tFinal state of current_window: {current_window}")

        # appending the maximum element of the current window to the output list
        output.append(nums[current_window[0]])

    # return the array containing output
    return output

# driver code
def main():
    window_sizes = [3, 3, 3, 3, 2, 4, 3, 2, 3, 18]
    nums_list = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        [1, 5, 8, 10, 10, 10, 12, 14, 15, 19, 19, 19, 17, 14, 13, 12, 12, 12, 14, 18, 22, 26, 26, 26, 28, 29, 30],
        [10, 6, 9, -3, 23, -1, 34, 56, 67, -1, -4, -8, -2, 9, 10, 34, 67],
        [4, 5, 6, 1, 2, 3],
        [9, 5, 3, 1, 6, 3],
        [2, 4, 6, 8, 10, 12, 14, 16],
        [-1, -1, -2, -4, -6, -7],
        [4, 4, 4, 4, 4, 4]
    ]

    for i in range(len(nums_list)):
        print(f"{i + 1}.\tInput array:\t{nums_list[i]}")
        print(f"\tWindow size:\t{window_sizes[i]}")
        output = find_max_sliding_window(nums_list[i], window_sizes[i])
        print(f"\n\tMaximum in each sliding window:\t{output}")
        print("-"*100)

if __name__ == '__main__':
    main()