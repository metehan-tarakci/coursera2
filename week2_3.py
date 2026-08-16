from collections import Counter

def read_kmers(file):
    with open(file, "r") as f:
        k = int(f.readline().strip())
        kmers = f.readline().rstrip().split()
    return k, kmers


def build_de_bruijn_graph(kmers, k):
    graph = {}
    for kmer in kmers:
        prefix = kmer[:k-1] # equivalent: prefix = kmer[:-1]
        suffix = kmer[1:]
        graph.setdefault(prefix, []).append(suffix)
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


def path_to_genome(path):
    result = path[0]
    for node in path[1:]:
        result += node[-1]
    return result


k, kmers = read_kmers("week2_3.txt")
graph = build_de_bruijn_graph(kmers, k)
start, end = find_start_end(graph)

# Add artificial edge end -> start to turn the Eulerian path into a cycle
graph.setdefault(end, []).append(start)

cycle = eulerian_cycle(graph, start)

# Find where the artificial edge (end -> start) was traversed, and cut the cycle there
for i in range(len(cycle) - 1):
    if cycle[i] == end and cycle[i + 1] == start:
        path = cycle[i+1:] + cycle[1:i+1] #path is a list too
        break

print(path_to_genome(path))