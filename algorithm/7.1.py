from find_lowest import find_lowest_cost_node


graph={}
graph['start']={}
graph['start']['a']=5
graph['start']['c']=2
graph['a']={}
graph['b']={}
graph['c']={}
graph['d']={}
graph['a']['b']=4
graph['a']['d']=2
graph['c']['a']=8
graph['c']['d']=7
graph['b']['d']=6
graph['b']['fin']=3
graph['d']['fin']=1
graph['fin']={}

costs={}
costs['fin']=float('inf')
parents={}
costs['a']=5
costs['c']=2
costs['d']=float('inf')
costs['b']=float('inf')
parents['a']='start'
parents['b']='start'
processed=[]
node=find_lowest_cost_node(costs,processed)
while node:
    cost=costs[node]
    for n in graph[node].keys():
        new_cost=cost + graph[node][n]
        if new_cost < costs[n]:
            costs[n]= new_cost
            parents[n]=node 
    processed.append(node)
    node=find_lowest_cost_node(costs,processed)

print(costs['fin'])
print(parents)