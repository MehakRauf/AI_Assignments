import heapq  #for priority queue implementation

def ucs(self, start, goal):
        visited = set()  # set to keep track of visited nodes
        priority_queue = [( start,0, [])]  # Initialize priority queue for UCS

        while priority_queue:  # Loop until priority queue is empty
            current,cost, path = heapq.heappop(priority_queue)  # Pop the lowest cost node 
            if current == goal:  # Check if current node is the goal node
                return path + [(current, cost)]  
            if current not in visited: 
                visited.add(current)  # Mark current node as visited if not visited
                for neighbor, edge_cost in self.graph.get(current, {}).items():  
                    if neighbor not in visited:  
                        heapq.heappush(priority_queue, ( neighbor,cost+edge_cost, path + [(current, cost)])) 

        return None  #if no path found