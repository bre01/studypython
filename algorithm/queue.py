from collections import deque
from re import search
graph={}
graph['you']=['alice','bob','claire']
graph['bob']=['anuj','peggy']
graph['claire']=[]
graph['alice']=[]
graph['anuj']=[]
graph['peggy']=[]
graph['m']=[]

def person_is_seller(person):
    return person[-1]=='m'
def search(name):
    search_queue=deque()
    search_queue+=graph[name]
    searched=[]
    while search_queue:
        person=search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):   
                return  True,person
            else:
                search_queue += graph[person]
                searched.append(person)
    return False 
print(search('you'))



