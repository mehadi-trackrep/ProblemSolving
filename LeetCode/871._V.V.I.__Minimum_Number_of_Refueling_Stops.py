import heapq
from typing import List

"""
    # V.V.I. - The heapq module in Python provides the min-heap implementation 
            of the priority queue algorithm. 
    So, if we use it as max-heap then we have to push the item making as negative & pop them by making
    again negative so that it can form it's original value.
"""

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
            
    # def min_refuel_stops(target, startFuel, stations):
        # If starting fuel is already greater or equal to target, no need to refuel
        if startFuel >= target:
            return 0

        # Create a max heap to store the fuel capacities of stations in
        # such a way that maximum fuel capacity is at the top of the heap
        max_heap = []

        # Initialize variables for loop
        i, n = 0, len(stations)
        stops = 0
        max_distance = startFuel

        # Loop until the car reach the target or the car is out of fuel
        while max_distance < target:
            # If there are still stations and the next one is within range, add its fuel capacity to the max heap
            if i < n and stations[i][0] <= max_distance:
                heapq.heappush(max_heap, -stations[i][1])
                i += 1
            # If there are no more stations and we can't reach the target, return -1
            elif not max_heap:
                return -1
            # Otherwise, fill up at the station with the highest fuel capacity and increment stops
            else:
                max_distance += -heapq.heappop(max_heap)
                stops += 1
        # Return the number of stops taken
        return stops