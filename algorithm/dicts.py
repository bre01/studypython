from lib2to3.pgen2.grammar import Grammar
from find_lowest import find_lowest_cost_node

graph={}
graph['start']={}
graph['start']['a']=6
graph['start']['b']=2

graph['a']={}
graph['b']={}
graph['a']['fin']=1
graph['b']['a']=3
graph['b']['fin']=5 
graph['fin']={} 

costs={}
infinity=float('inf')
costs['fin']=infinity
costs['a']=6
costs['b']=2
parents={}
parents['a']='start'
parents['b']='start'
parents['fin']=None
processed=[]
node=find_lowest_cost_node(costs,processed)
while node:
    cost=costs[node]
    for n in graph[node].keys():
        if cost+ graph[node][n] < costs[n]:
            costs[n]= cost+ graph[node][n]
            parents[n]=node 
    processed.append(node)
    node=find_lowest_cost_node(costs,processed)

print(costs['fin'])
print(parents)










