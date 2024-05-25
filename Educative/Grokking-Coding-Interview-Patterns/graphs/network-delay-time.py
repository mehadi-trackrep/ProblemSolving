from queue import PriorityQueue
from collections import defaultdict

def network_delay_time(times, n, k):
    # Creat adjacency dictonary
    adjacency = defaultdict(list)
    # Store source as key, and destination and time as values
    for src, dst, t in times:
        adjacency[src].append((dst, t)) 

    print("\t Adjacency dictionary:", dict(adjacency))

    pq = PriorityQueue()
    # Initialize our queue with (time, node)
    pq.put((0, k))  # Add the source node with a delay time of 0
    visited = set() # Set to store the visited nodes
    delays = 0      # To store the delay time

    while not pq.empty():
        # Get the minimum time node from the queue
        time, node = pq.get()
      
        print("\t Retrieved time:", time)
        print("\t Retrieved node:", node)

        # If node is already visited we will continue to next iteration
        if node in visited:
            continue
          
        visited.add(node)  # Mark the node as visited
        delays = max(delays, time) # Update the delay time if necessary
        neighbours = adjacency[node]

        print("\t Neighbours:", neighbours)

        # Add all the unvisited neighbors of the current node to the queue with their new delay time
        for neighbour in neighbours:
            neighbour_node, neighbour_time = neighbour
            if neighbour_node not in visited:
                new_time =  time + neighbour_time
                pq.put((new_time, neighbour_node))
    
    # If all nodes have been visited, return the delay time else return -1
    if len(visited) == n:
        return delays

    return -1


# Driver code
def main():
    time = [
                [[2, 1, 1], [3, 2, 1], [3, 4, 2]],
                [[2, 1, 1], [1, 3, 1], [3, 4, 2], [5, 4, 2]],
                [[1, 2, 1], [2, 3, 1], [3, 4, 1]],
                [[1, 2, 1], [2, 3, 1], [3, 5, 2]],
                [[1, 2, 2]]
            ]

    n = [4, 5, 4, 5, 2]
    k = [3, 1, 1, 1, 2]

    for i in range(len(time)):
        print(i + 1, ".\t times = ", time[i], sep="")
        print("\t number of nodes 'n' = ", n[i], sep="")
        print("\t starting node 'k' = ", k[i], "\n", sep="")
        print("\t Minimum amount of time required = ", network_delay_time(time[i], n[i], k[i]), sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()