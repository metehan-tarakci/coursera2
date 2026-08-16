from collections import Counter

aa_mass_table = {
    'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114, 'D': 115,
    'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186
}

def read_mass_spectrometer(file):
    spectrum = []
    with open(file, "r") as f:
        peptide = f.readline().rstrip()
        for mass in f.readline().rstrip().split():
            spectrum.append(int(mass))
    return peptide, spectrum

p, spectrum = read_mass_spectrometer("week4_7.txt")

def peptide_to_mass(p): # transforms str peptide to int mass peptide   WNAV --> [186, 114 ,71, 99]
    masses = []

    for aa in p:
        masses.append(aa_mass_table[aa])

    return masses

peptide = peptide_to_mass(p)

def linear_spectrum(peptide):
    masses = [0]
    total_len = len(peptide)
    for i in range(total_len):
        total = 0
        for j in range(i, total_len):
            total += peptide[j]
            masses.append(total)
    return sorted(masses)

def score(peptide_spectrum, spectrum):
    peptide_counter = Counter(peptide_spectrum)
    spectrum_counter = Counter(spectrum)
    total = 0
    for mass, count in peptide_counter.items():
        total += min(count, spectrum_counter[mass])
    return total

def linear_score(peptide, spectrum):
    return score(linear_spectrum(peptide), spectrum)

print(linear_score(peptide, spectrum))