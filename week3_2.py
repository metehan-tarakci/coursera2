def read_file(file):
    with open(file, "r") as f:
        genome=""
        for line in f:
            line = line.strip()
            genome = genome + line
    return genome

dna_str = read_file("week3_2.txt")

aa_str = "VKLFPWFNQY"

DNA_Codons = {
    "TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",
    "TAT": "Y", "TAC": "Y", "TAA": "*", "TAG": "*",
    "TGT": "C", "TGC": "C", "TGA": "*", "TGG": "W",

    "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",

    "ATT": "I", "ATC": "I", "ATA": "I", "ATG": "M",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "AGT": "S", "AGC": "S", "AGA": "R", "AGG": "R",

    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G"
}
def translate_seq(seq, init_pos=0): #DNA TO PROTEIN
    possible_protein=[]
    for i in range(init_pos, len(seq) - 2, 3): #  you need at least 3 characters left to form a codon, so you stop 2 positions before the end. 
        possible_protein.append(DNA_Codons[seq[i:i + 3]])            
    return possible_protein
    


def reverse_complement(seq): # CODING'İN KARŞI STRAND'İ
    translation_table = str.maketrans("ATGC", "TACG")
    complementedStr = seq.translate(translation_table)
    return complementedStr[::-1]

starting_positions = 0

window = len(aa_str) * 3

for i in range(len(dna_str) - window + 1):

    fragment = dna_str[i:i+window]

    protein = "".join(translate_seq(fragment))

    if protein == aa_str:
        print(fragment)
        starting_positions += 1


    rev = reverse_complement(fragment)

    protein = "".join(translate_seq(rev))

    if protein == aa_str:
        print(fragment)
        starting_positions += 1
print(dna_str)
print(starting_positions)