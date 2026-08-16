
def read_kmers(file):
    with open(file, "r") as f:
        line = f.readline().rstrip()
        kmers = line.split()
    return kmers

kmers = read_kmers("week1_5.txt")
for kmer in kmers:
    k = len(kmer)

def prefix_and_suffix():
    prefixes_and_suffixes = {}

    for kmer in kmers:
        prefix = kmer[:k-1] # equivalent prefix = kmer[:-1]
        suffix = kmer[1:]

        prefixes_and_suffixes.setdefault(prefix, []).append(suffix)

    return prefixes_and_suffixes


debruijn_graph = prefix_and_suffix()

for prefix, suffixes in debruijn_graph.items():
    print(f"{prefix}: {' '.join(suffixes)}")