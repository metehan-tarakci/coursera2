k = 4
dna = "AAGATTCTCTAAGA"

kmers = []
for i in range(len(dna) - k + 1):
    kmers.append(dna[i:i+k])


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