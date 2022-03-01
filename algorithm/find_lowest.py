def find_lowest_cost_node(costs,processed):
    lowest_node=None
    lowest_cost=float('inf')
    for node in costs.keys():
        if costs[node]< lowest_cost and node not in processed:
            lowest_node=node
            lowest_cost=costs[node] 
return lowest_node
