def read_kmers(file):
    with open(file, "r") as f:
        line = f.readline().rstrip()
        kmers = line.split()
    return kmers


kmers = read_kmers("week1_2.txt")
for kmer in kmers:
    k = len(kmer)

def prefix():
    prefixes=[]
    for kmer in kmers:
        prefixes.append(kmer[:k-1])
    return prefixes

def suffix():
    suffixes=[]
    for kmer in kmers:
        suffixes.append(kmer[1:])
    return suffixes

def first_prefix():
    prefixes = prefix()
    suffixes = suffix()
    for p in prefixes:
        if p not in suffixes:
            return p

def elongate():
    first_p = first_prefix()
    prefixes = prefix()
    for p in prefixes:
        for x in prefixes:
            if p[1:] == x[:k-2]:
                first_p = first_p + x[-1]
    return first_p

def add_last_suffix():
    e = elongate()
    prefixes = prefix()
    suffixes = suffix()
    for s in suffixes:
        if s not in prefixes:
            return e + s[-1]

print(add_last_suffix())

""" verilen dataset'te kmerler kesinlikle sıralı verilmişse: 

def read_kmers(file):
    with open(file, "r") as f:
        line = f.readline().rstrip()
        kmers = line.split()
    return kmers


def genome_path_string(kmers):
    result = kmers[0]
    for kmer in kmers[1:]:
        result += kmer[-1]
    return result


kmers = read_kmers("week1_2.txt")
print(genome_path_string(kmers)) 

"""