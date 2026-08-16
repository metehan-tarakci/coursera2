from collections import Counter

aa_mass_list = [
    57, 71, 87, 97, 99, 101, 103, 113, 114,
    115, 128, 129, 131, 137, 147, 156, 163, 186
]

def read_mass_spectrometer(file):
    spectrum = []
    with open(file, "r") as f:
        n = f.readline().rstrip()
        for mass in f.readline().rstrip().split():
            spectrum.append(int(mass))
    return int(n), spectrum

n, spectrum = read_mass_spectrometer("week4_2.txt")

def linear_spectrum(peptide):
    masses = [0]
    total_len = len(peptide)
    for i in range(total_len):
        total = 0
        for j in range(i, total_len):
            total += peptide[j]
            masses.append(total)
    return masses

def cyclic_spectrum(peptide):
    masses = [0]
    total_len = len(peptide)
    for i in range(total_len):
        total = 0
        for j in range(total_len - 1):
            total += peptide[(i + j) % total_len]
            masses.append(total)
    masses.append(sum(peptide))
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

def cyclic_score(peptide, spectrum):
    return score(cyclic_spectrum(peptide), spectrum)

def expand(candidates):
    new_candidates = []
    for peptide in candidates:
        for mass in aa_mass_list:
            new_candidates.append(peptide + [mass])
    return new_candidates

def trim(leaderboard, spectrum, n):
    if len(leaderboard) <= n: # If there aren't even n peptides yet, there's nothing to trim — just return everything unchanged
        return leaderboard

    scored = [(peptide, linear_score(peptide, spectrum)) for peptide in leaderboard] # Build a list of (peptide, score) pairs — score each 
    # candidate peptide against the experimental spectrum using the "linear" score (since these are incomplete, still-growing peptides, 
    # not full cyclic ones yet)
    scored.sort(key=lambda x: x[1], reverse=True) # Sort this list by score, highest first. x[1] pulls out the score from each 
    # (peptide, score) tuple; reverse=True means descending order

    # Keep the top n, PLUS anyone tied with the n-th score
    cutoff_score = scored[n - 1][1] # n. peptide n-1 eder listede. [1] tuple'da sağdakini al (score'u) demek.
    trimmed = [peptide for peptide, s in scored if s >= cutoff_score]
    return trimmed

def leaderboard_cyclopeptide_sequencing(spectrum, n):
    parent_mass = max(spectrum)
    leaderboard = [[]]
    leader_peptide = []

    while leaderboard:
        leaderboard = expand(leaderboard)

        next_leaderboard = []
        for peptide in leaderboard:
            mass = sum(peptide)
            if mass == parent_mass:
                if cyclic_score(peptide, spectrum) > cyclic_score(leader_peptide, spectrum):
                    leader_peptide = peptide
                next_leaderboard.append(peptide)
            elif mass < parent_mass:
                next_leaderboard.append(peptide)
            # mass > parent_mass: dropped (not added to next_leaderboard)

        leaderboard = trim(next_leaderboard, spectrum, n)

    return leader_peptide

result = leaderboard_cyclopeptide_sequencing(spectrum, n)
print("-".join(map(str, result)))