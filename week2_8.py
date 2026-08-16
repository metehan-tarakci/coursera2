"""
Week2_6'nın benzeri, adjacency list ve İsolated cycle'lı hali
"""

from collections import Counter

def read_graph(file):
    with open(file, "r") as f:
        graph = {}
        for line in f:
            line = line.strip()
            if not line:
                continue
            node, neighbors = line.split(": ")
            graph[node] = neighbors.split()
    return graph
graph = read_graph("week2_8.txt")

def maximal_non_branching_paths(graph):
    indegree = Counter()
    outdegree = Counter()
    # Compute indegree and outdegree
    for node, neighbors in graph.items():
        outdegree[node] += len(neighbors)
        for neighbor in neighbors:
            indegree[neighbor] += 1
    nodes = set(indegree) | set(outdegree)
    paths = []
    visited = set()

    # --------------------------
    # Maximal non-branching paths
    # --------------------------
    for node in nodes:

        if not (indegree[node] == 1 and outdegree[node] == 1):
            if outdegree[node] > 0:
                for neighbor in graph[node]:
                    path = [node, neighbor]
                    current = neighbor

                    while indegree[current] == 1 and outdegree[current] == 1:
                        visited.add(current)

                        next_node = graph[current][0]
                        path.append(next_node)
                        current = next_node
                    paths.append(path)

    # --------------------------
    # Isolated cycles : gireni ve çıkanı 1'er ise ve bir cyclesa ve contig sağlıyorsa
    # --------------------------
    for node in nodes:
        if node in visited: #visited prevents printing duplicate cycles.
            continue
        if indegree[node] == 1 and outdegree[node] == 1:
            cycle = [node]
            visited.add(node)

            current = graph[node][0]

            while current != node:
                cycle.append(current)
                visited.add(current)
                current = graph[current][0]
            cycle.append(node)
            paths.append(cycle)

    return paths

paths = maximal_non_branching_paths(graph)

for path in paths:
    print(" ".join(path))