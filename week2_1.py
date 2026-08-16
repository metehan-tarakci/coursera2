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


graph = read_graph("week2_1.txt")
cycle = eulerian_cycle(graph)
print(" ".join(cycle))
print(graph)