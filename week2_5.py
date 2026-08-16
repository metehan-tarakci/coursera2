"""
**** week2_3'ün READ PAIR'LI HÂLİ ****

Problem 1: String Reconstruction from Read-Pairs

Input:

(k,d)-mers

unordered!!! Week2_7 ile farkı bu

↓

Build paired de Bruijn graph

↓

Find Eulerian path

↓

Reconstruct string
"""


from collections import Counter

def read_kmers(file):
    with open(file, "r") as f:
        k, d = f.readline().rstrip().split()
        pairs = f.readline().replace(" ", "|").rstrip().split("|")
        first=[]
        second=[]
        for i in range(len(pairs)):
            if i % 2 == 0:
                first.append(pairs[i])
            if i % 2 == 1:
                second.append(pairs[i])
    return int(k), int(d), first, second, pairs

k , d, first , second, pairs = read_kmers("week2_5.txt")


def build_de_bruijn_graph():
    read_pairs_graph = {}

    for left, right in zip(first, second):
        prefix = (left[:-1], right[:-1])
        suffix = (left[1:], right[1:])

        read_pairs_graph.setdefault(prefix, []).append(suffix)

    return read_pairs_graph

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

graph = build_de_bruijn_graph()
start, end = find_start_end(graph)

# Add artificial edge end -> start to turn the Eulerian path into a cycle
graph.setdefault(end, []).append(start)

cycle = eulerian_cycle(graph, start)

for i in range(len(cycle) - 1): # here to remove the artificial edge. find the eularian path from eularian cycle
    if cycle[i] == end and cycle[i + 1] == start:
        path = cycle[i+1:] + cycle[1:i+1] #path is a list too
        break

lefts = [left for left, right in path]
rights = [right for left, right in path]

def generate_string(path):
    result = path[0]
    for node in path[1:]:
        result += node[-1]
    return result

prefix_string = generate_string(lefts) # 1. pairdaki soldakini komple al diğer pairlerdaki soldakinin sonuncu harfini ekle 
suffix_string = generate_string(rights) # 2. pairdaki sağdakini komple al diğer pairlerdaki sağdakinin sonuncu harfini ekle 

def generate_genome():
    return prefix_string + suffix_string[-(k+d):]

print(generate_genome())
print(graph)