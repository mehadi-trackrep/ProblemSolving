

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        """
            We have to track three things for fetching maximum area. 
            1. all will be 1 so, 1 * total_heights
            2. check if max(sofar_max_area, max(current_bar, previous_bar))
            3. check max(
                sofar_max_area, 
                (current_ind - consecutive_small_or_equal_previous_item_ind) * consecutive_small_or_equal_previous_item
                )
        """
        h = len(heights)
        
        consecutive_small_or_equal_previous_item = 1
        consecutive_small_or_equal_previous_item_ind = 0
        sofar_max_area = heights[0]

        for ind in range(1, h):
            sofar_max_area = max(sofar_max_area, 2* min(heights[ind], heights[ind - 1]))
            sofar_max_area = max(
                sofar_max_area, 
                (ind - consecutive_small_or_equal_previous_item_ind) * consecutive_small_or_equal_previous_item
            )
            if heights[ind] < heights[ind - 1]:
                consecutive_small_or_equal_previous_item = heights[ind]
                consecutive_small_or_equal_previous_item_ind = ind
        
        sofar_max_area = max(sofar_max_area, h)
        return sofar_max_area


if __name__ == '__main__':
    solution = Solution()
    # max_area = solution.largestRectangleArea(
    #     heights=[2,1,5,6,2,3]
    # )

    # max_area = solution.largestRectangleArea(
    #     heights=[2,4]
    # )

    max_area = solution.largestRectangleArea(
        heights=[2,1,2,3,2,3]
    )

    print("Max area: ", max_area)