from collections import Counter
from itertools import product

def all_kmers(k):
    kmers = []
    for p in product('01', repeat=k):
        kmers.append(''.join(p))
    return kmers

kmers = all_kmers(8)

def prefix_and_suffix(k):
    prefixes_and_suffixes = {}

    for kmer in kmers:
        prefix = kmer[:k-1]
        suffix = kmer[1:]

        prefixes_and_suffixes.setdefault(prefix, []).append(suffix)

    return prefixes_and_suffixes


def eulerian_cycle(graph):
    # Make a mutable copy of the adjacency lists so we can remove edges as we use them
    remaining = {node: list(neighbors) for node, neighbors in graph.items()}

    start = next(iter(graph))
    stack = [start]
    cycle = []

    while stack:
        current = stack[-1]
        if current in remaining and remaining[current]:
            next_node = remaining[current].pop() #.pop() removes and returns the last item in a list
            stack.append(next_node)
        else:
            cycle.append(stack.pop())

    cycle.reverse()
    return cycle


graph = prefix_and_suffix(8)
print(kmers)
print(graph)
cycle = eulerian_cycle(graph)
print(cycle)

def path_to_genome(path, k):
    result = path[0]
    for node in path[1:]:
        result += node[-1]
    return result[:-k+1]

print(path_to_genome(cycle, 8))
