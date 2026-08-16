"""

Problem 2: StringSpelledByGappedPatterns (this one)

Input:

(k,d)-mers

already arranged in path order!!!!

↓

Just reconstruct the two strings

↓

Merge them

No graph construction is needed.
"""

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

k , d, first , second, pairs = read_kmers("week2_7.txt")
print(k)
print(d)
print(pairs)
print(first)
print(second)

def generate_string(path):
    result = path[0]
    for node in path[1:]:
        result += node[-1]
    return result

prefix_string = generate_string(first) # 1. pairdaki soldakini komple al diğer pairlerdaki soldakinin sonuncu harfini ekle 
suffix_string = generate_string(second) # 2. pairdaki sağdakini komple al diğer pairlerdaki sağdakinin sonuncu harfini ekle 

def generate_genome():
    return prefix_string + suffix_string[-(k+d):]

print(generate_genome())
