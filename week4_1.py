from collections import Counter

def read_mass_spectrometer(file):
    spectrum = []

    with open(file, "r") as f:
        peptide = f.readline().rstrip()

        for mass in f.readline().rstrip().split():
            spectrum.append(int(mass))

    return peptide, spectrum

cyclic_peptide_str, spectrum = read_mass_spectrometer("week4_1.txt")

double = cyclic_peptide_str + cyclic_peptide_str

n = len(cyclic_peptide_str)

aa_mass_table = {
    'G':57, 'A':71, 'S':87, 'P':97, 'V':99, 'T':101, 'C':103, 'I':113, 'L':113, 'N':114, 
    'D':115, 'K':128, 'Q':128, 'E':129, 'M':131, 'H':137, 'F':147, 'R':156, 'Y':163, 'W':186
}

def generate_substrings():
    substrings = []
    for length in range(1, n):
        for start in range(n):
            substrings.append(double[start:start+length])
    substrings.append(cyclic_peptide_str)   # full peptide
    substrings.append("") # empty peptide
    return substrings

def mass():
    mass_list = []
    for string in generate_substrings():
        m=0
        for i in range(len(string)):
            m += aa_mass_table[string[i]]
        mass_list.append(m)
    return sorted(mass_list)

def score_peptide():
    score = 0
    for m in Counter(spectrum):
        if Counter(spectrum)[m] == Counter(mass())[m]:
            score += Counter(spectrum)[m]
        elif Counter(spectrum)[m] < Counter(mass())[m]:
            score += Counter(spectrum)[m]
        elif Counter(mass())[m] < Counter(spectrum)[m]:
            score += Counter(mass())[m]
    return score

print(score_peptide())