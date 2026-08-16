""" CONTIG problem
Walk through the de Bruijn graph. Keep walking while every intermediate node has exactly 
one incoming edge and one outgoing edge. 
The moment you reach a branching node (or a node where multiple edges enter), stop. 
The sequence you've spelled is one contig.
gireni ve çıkanı 1 olmayan bir node seç, gireni ve çıkanı 1 olan nodelar ekle, gireni ve çıkanı 1 olmadığında dur
"""
from collections import Counter

def read_kmers(file):
    with open(file, "r") as f:
        line = f.readline().rstrip()
        kmers = line.split()
    return kmers

kmers = read_kmers("week2_6.txt")

for kmer in kmers:
    k = len(kmer)

def debruijn(patterns):
    graph = {}

    for pattern in patterns:
        prefix = pattern[:-1]
        suffix = pattern[1:]
        graph.setdefault(prefix, []).append(suffix)

    return graph

def contigs(patterns):

    graph = debruijn(patterns)

    indegree = Counter()
    outdegree = Counter()

    # Compute degrees
    for node, neighbors in graph.items():
        outdegree[node] += len(neighbors)

        for neighbor in neighbors:
            indegree[neighbor] += 1

    # Make sure every node exists in both counters
    nodes = set(indegree) | set(outdegree) # set takes only the keys # "|" combines both nodes with 
    #incoming edges and outgoing edges and removes duplicates
    contigs = []

    # Find maximal non-branching paths
    for node in nodes:

        if not (indegree[node] == 1 and outdegree[node] == 1): # gireni ve çıkanı 1'er olmayandan başla

            if outdegree[node] > 0: # çıkanı varsa (en sondaki node'u elemek için)

                for neighbor in graph[node]: # çıktığı her bir neighbor için path oluştur

                    path = [node, neighbor]
                    current = neighbor

                    while indegree[current] == 1 and outdegree[current] == 1: # gireni ve çıkanı 1'se 
                        #yani tek rota varsa devam et
                        next_node = graph[current][0]
                        path.append(next_node)
                        current = next_node

                    contigs.append(path)

    # Convert node paths into strings
    answer = []

    for path in contigs:

        text = path[0]

        for node in path[1:]:
            text += node[-1]

        answer.append(text)

    return answer

result = contigs(kmers)

print(*sorted(result))