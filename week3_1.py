rna_str = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"

RNA_Codons = {
    # Phenylalanine
    "UUU": "F", "UUC": "F",
    # Leucine
    "UUA": "L", "UUG": "L",
    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    # Isoleucine
    "AUU": "I", "AUC": "I", "AUA": "I",
    # Methionine (Start)
    "AUG": "M",
    # Valine
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    # Serine
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "AGU": "S", "AGC": "S",
    # Proline
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    # Threonine
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    # Alanine
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    # Tyrosine
    "UAU": "Y", "UAC": "Y",
    # Histidine
    "CAU": "H", "CAC": "H",
    # Glutamine
    "CAA": "Q", "CAG": "Q",
    # Asparagine
    "AAU": "N", "AAC": "N",
    # Lysine
    "AAA": "K", "AAG": "K",
    # Aspartic Acid
    "GAU": "D", "GAC": "D",
    # Glutamic Acid
    "GAA": "E", "GAG": "E",
    # Cysteine
    "UGU": "C", "UGC": "C",
    # Tryptophan
    "UGG": "W",
    # Arginine
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AGA": "R", "AGG": "R",
    # Glycine
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    # Stop codons denoted by ""
    "UAA": "", "UAG": "", "UGA": ""
}

def translate_seq(seq, init_pos=0):
    """Translates a DNA sequence into an aminoacid sequence"""
    protein = ""
    for i in range(init_pos, len(seq) - 2, 3): #len(seq)-k+1
        protein = protein + RNA_Codons[seq[i:i + 3]]
    return protein

print(translate_seq(rna_str))