from collections import Counter

def read_graph(file):
    with open(file, "r") as f:
        graph = {}
        for line in f:
            line = line.rstrip()
            if line == "":
                continue
            node, neighbors = line.split(": ")
            graph[node] = neighbors.split()
    return graph


def find_start_end(graph):
    out_degree = Counter()
    in_degree = Counter()
    for node, neighbors in graph.items():
        out_degree[node] += len(neighbors)
        for n in neighbors:
            in_degree[n] += 1

    start = end = None
    for node in set(list(out_degree.keys()) + list(in_degree.keys())):
        diff = out_degree[node] - in_degree[node]
        if diff == 1:
            start = node
        elif diff == -1:
            end = node
    return start, end


def eulerian_cycle(graph, start):
    remaining = {node: list(neighbors) for node, neighbors in graph.items()}
    stack = [start]
    cycle = []
    while stack:
        current = stack[-1]
        if current in remaining and remaining[current]:
            next_node = remaining[current].pop()
            stack.append(next_node)
        else:
            cycle.append(stack.pop())
    cycle.reverse()
    return cycle


graph = read_graph("week2_2.txt")
start, end = find_start_end(graph)

graph.setdefault(end, []).append(start)  # Add "artificial edge: end -> start" to the graph

full_cycle = eulerian_cycle(graph, start)
#Cutting logic — instead of [:-1], we scan the full cycle for the specific position where end is immediately 
# followed by start (the artificial edge's signature), then reconstruct the path by 
# rotating around that cut point. This works regardless of whether the artificial edge happens to land at the 
# end, middle, or anywhere else in the raw cycle.
for i in range(len(full_cycle) - 1): 
    if full_cycle[i] == end and full_cycle[i + 1] == start:
        path = full_cycle[i+1:] + full_cycle[1:i+1]
        break

print(" ".join(path))