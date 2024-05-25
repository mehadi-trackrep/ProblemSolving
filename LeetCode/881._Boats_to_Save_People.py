from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Replace this placeholder return statement with your code
        people.sort()
        number_of_boats = 0
        l, r = 0, len(people)-1

        while l <= r:  # N.B. Each boat can carry at most 2 peoples at a time!
            light_weight = people[l]
            heavy_weight = people[r]
            if light_weight + heavy_weight <= limit:
                l += 1
                r -= 1
            else:
                r -= 1
            number_of_boats += 1

        return number_of_boatsv  