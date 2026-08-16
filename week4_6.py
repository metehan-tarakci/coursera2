from collections import Counter

def read_mass_spectrometer(file):
    spectrum = []
    with open(file, "r") as f:
        m = f.readline().rstrip()
        n = f.readline().rstrip()
        for mass in f.readline().rstrip().split():
            spectrum.append(int(mass))
    return int(m), int(n), spectrum


m, n, spectrum = read_mass_spectrometer("week4_6.txt")


def convolution(spectrum, m):
    convolution = []
    mass_freq_dict = {}
    for i in range(len(spectrum)):
        for j in range(0, i):
            diff = spectrum[i] - spectrum[j]
            if not (diff == 0):
                convolution.append(diff)

    for key, value in Counter(convolution).items():
        if 57 <= key and key <= 200:
            mass_freq_dict[key] = value
    sorted_dict = dict(sorted(mass_freq_dict.items(), key=lambda x: x[1], reverse=True))

    cutoff_freq = list(sorted_dict.values())[m - 1]
    convolution_aa_mass_list = [mass for mass, freq in sorted_dict.items() if freq >= cutoff_freq]

    return convolution_aa_mass_list

aa_mass_list = convolution(spectrum, m)

def linear_spectrum(peptide):
    masses = [0]
    total_len = len(peptide)
    for i in range(total_len):
        total = 0
        for j in range(i, total_len):
            total += peptide[j]
            masses.append(total)
    return sorted(masses)

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
    # candidate peptide against the experimental spectrum using the "linear" score (since these are incomplete, still-growing peptides, not full cyclic ones yet)
    scored.sort(key=lambda x: x[1], reverse=True) # Sort this list by score, highest first. x[1] pulls out the score from each (peptide, score) tuple; reverse=True means descending order

    # Keep the top n, PLUS anyone tied with the n-th score
    cutoff_score = scored[n - 1][1] # n. peptide n-1 eder listede. [1] tuple'da sağdakini al (score'u) demek.
    trimmed = [peptide for peptide, s in scored if s >= cutoff_score]
    return trimmed


def leaderboard_cyclopeptide_sequencing(spectrum, n):

    parent_mass = max(spectrum)
    leaderboard = [[]]
    leader_peptides = []
    best_score = 0

    while leaderboard:

        leaderboard = expand(leaderboard)
        next_leaderboard = []

        for peptide in leaderboard:
            mass = sum(peptide)
            if mass == parent_mass:
                peptide_score = cyclic_score(peptide, spectrum)

                if peptide_score > best_score:
                    best_score = peptide_score
                    leader_peptides = [peptide] # Start a new list containing this peptide, because it is now the only best peptide.

                elif peptide_score == best_score:
                    if peptide not in leader_peptides:
                        leader_peptides.append(peptide)

            elif mass < parent_mass:
                next_leaderboard.append(peptide)

        leaderboard = trim(next_leaderboard, spectrum, n)

    return leader_peptides, best_score


leader_peptides, best_score = leaderboard_cyclopeptide_sequencing(spectrum, 1000)

print(best_score)
print(len(leader_peptides))

for peptide in leader_peptides:
    print("-".join(map(str, peptide)))