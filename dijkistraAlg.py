
graph = {}
graph["Start"] = {} # First node
graph["Start"]["a"] = 6
graph["Start"]["b"] = 2 

graph["a"] = {} # Second node
graph["a"]["fin"] = 1 

graph["b"] = {} # Third node
graph["b"]["a"] = 3
graph["b"]["fin"] = 5 

graph["fin"] = {} # Finishing node 

infinity = float("inf") 
costs = {} 
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity  

parents = {} 
parents["a"] = "Start"
parents["b"] = "Start"
parents["fin"] = None 

processed = []

def find_lowest_node(costs): 
  lowestCost = float("inf") 
  lowestCostNode = None
  for node in costs: 
    cost = costs[node] 
    if cost < lowestCost and node not in processed: 
      lowestCostNode = node 
      lowestCost = cost

  return lowestCostNode 

node = find_lowest_node(costs)
while node is not None: 
  cost = costs[node]
  neighbours = graph[node] 
  for n in neighbours.keys(): 
    newCost = cost + neighbours[n] 
    if costs[n] > newCost: 
      costs[n] = newCost 
      parents[n] = node 

  processed.append(node) 
  node = find_lowest_node(costs) 



order = ["Start"] 
prevNode = 0
while processed != []:
  for i in parents.keys() : 
    if parents[i] == order[prevNode]:
      order.append(i)
      prevNode += 1 
      processed.pop(processed.index(i)) 
     
      
      

print("Route is : ", "|".join(order))
print("Smallest weight is:", costs["fin"])

  
      
