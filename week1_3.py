def read_kmers(file):
    with open(file, "r") as f:
        line = f.readline().rstrip()
        kmers = line.split()
    return kmers


kmers = read_kmers("week1_3.txt")
for kmer in kmers:
    k = len(kmer)

def prefix():
    kmer_and_prefixes={}
    for kmer in kmers:
        kmer_and_prefixes[kmer] = kmer[:k-1]
    return kmer_and_prefixes

def suffix():
    kmer_and_suffixes={}
    for kmer in kmers:
        kmer_and_suffixes[kmer] = kmer[1:]
    return kmer_and_suffixes

def compare():
    result = {}
    kmer_and_prefixes = prefix()
    kmer_and_suffixes = suffix()
    for kmer1, s in kmer_and_suffixes.items():
        for kmer2, p in kmer_and_prefixes.items():
            if s == p and kmer1 != kmer2:
                if kmer1 in result:
                    result[kmer1].append(kmer2)
                else:
                    result[kmer1] = [kmer2]
    return result

overlap_graph = compare()
for kmer, neighbors in overlap_graph.items():
    print(f"{kmer}: {' '.join(neighbors)}")

