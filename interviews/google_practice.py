# practice for google interview
# import collections

# class Graph:
#     def __init__(self):
#         self.graph = collections.defaultdict(set)

#     def has_bridge(self, edges = []):
#         # create graph
#         for node in edges:
#             self.graph[node[0]].add(node[1])
#             self.graph[node[1]].add(node[0])
        
#         # check for bridges
#         for node in self.graph:
#             for edge in self.graph[node]:
#                 self.graph[node] = self.graph[node].discard(edge)
#                 if len(bfs(self.graph, node)) != len(self.graph.keys()):
#                     return True
#                 self.graph[node] = self.graph[node].add(edge)
#         return False
    
#     def bfs(self, graph, node):
#         queue = collections.deque()
#         visited = []
#         curr = None
#         queue.push(node)
#         visited.append(node)

#         while len(queue) != 0:
#             curr = queue.popleft()
#             for child in self.graph[curr]:
#                 if child not in visited:
#                     visited.append(child)
#                     queue.push(child)
#         return visited




# if __name__ == "__main__":
#     test = Graph()
#     test.has_bridge([1,2],[0,2],[3,1],[3,2])

class BinSearch:

    def __init__(self);
        pass

    def bin_search(self, arr, target, l, r):
        # Check base case 
        if r >= l: 
      
            mid = l + (r - l)/2
      
            # If element is present at the middle itself 
            if arr[mid] == target: 
                return mid 
              
            # If element is smaller than mid, then it can only 
            # be present in left subarray 
            elif arr[mid] > target: 
                return bin_search(arr, l, mid-1, target) 
      
            # Else the element can only be present in right subarray 
            else: 
                return bin_search(arr, mid+1, r, target) 
      
        else: 
            # Element is not present in the array 
            return -1



if __name__ == "__main__":
    test = BinSearch()
    test.bin_search([1,4,5,8,4], 5, 4, 5)

