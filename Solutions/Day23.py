from collections import defaultdict
text = open('Input/Day23.txt').read().splitlines()
##text = open('Solutions/test.txt').read().splitlines()

graph = defaultdict(set)

for line in text:
    x, y = line.split('-')
    graph[x].add(y)
    graph[y].add(x)

result = set()

for x in graph:
    for y in graph[x]:
        for c in graph[y]:
            if c != y and c in graph[x]:
                result.add(tuple(sorted([x, y, c])))

t_result = [x for x in result if any(node.startswith('t') for node in x)]
print(len(t_result))

from itertools import combinations

def largest(graph):
    def is_clique(nodes):
        return all(b in graph[a] for a in nodes for b in nodes if a != b)
    nodes = sorted(graph.keys(), key = lambda x: len(graph[x]), reverse = True)
    result = []

    for node in nodes:
        candidates = [node] + sorted(graph[node], key = lambda x: len(graph[x]), reverse = True)
        clique = [candidates[0]]

        for candidate in candidates[1:]:
            if is_clique(clique + [candidate]):
                clique.append(candidate)
        if len(clique) > len(result):
            result = clique
    return sorted(result)

print(','.join(largest(graph)))

