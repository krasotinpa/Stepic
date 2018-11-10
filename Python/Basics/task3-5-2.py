import json

def getgraph(data):
    graph = {}
    for d in data:
        if d['name'] not in graph:
            graph[d['name']] = set()
        for i in range(len(d['parents'])):
            graph[d['parents'][i]] = graph.get(d['parents'][i],set()) | set([d['name']])
    return graph

def dfs(data, start, visited=None):
    # https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

    if visited is None:
        visited = set()
    visited.add(start)

    for next in data[start] - visited:
        if next not in data:
            data[next] = set()
        dfs(data, next, visited)
    return visited

json_data = [ {"name": "dfgre", "parents": ["gsdfgre"]}, {"name": "hsdgreg", "parents": ["dfgre", "gsd"]}, {"name": "gsd", "parents": ["dfgre"]}, {"name": "gsdfgre", "parents": []}]

#json_data = json.loads(input())
graph = getgraph(json_data)
print(graph)

for i in sorted(json_data, key=lambda x: x['name']):
    print(i['name'],':',len(dfs(graph,i['name'])))
