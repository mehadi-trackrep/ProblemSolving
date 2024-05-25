from typing import List
from queue import PriorityQueue
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
            It's a basic dijkstra algorithm (used for finding the shortest path in a graph) based problem.
        """
        adjacency_list = defaultdict(list)

        for src, dst, t in times:
            adjacency_list[src].append((dst, t))

        pq = PriorityQueue()
        pq.put((0, k))  # total cost(delay) for source node - k is 0,
                        # as priority queue sorts by default using 1st value so, 1st value will be the distance/delay
        visited = set()
        min_delays = 0  # at least this amount of time required for spreading out the signal to all nodes from the source

        while not pq.empty():
            delay_time, src = pq.get()  # distance == delay

            if src in visited:
                continue

            visited.add(src)
            min_delays = max(min_delays, delay_time)
            neighbours = adjacency_list[src]

            for neighbour in neighbours:
                neighbour_node, neighbour_time = neighbour
                if neighbour_node not in visited:
                    new_time = neighbour_time + delay_time
                    pq.put((new_time, neighbour_node))

        if len(visited) == n:
            return min_delays

        return -1