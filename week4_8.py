from collections import Counter

aa_mass_table = {
    'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114, 'D': 115,
    'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186
}

def read_input(file):

    with open(file, "r") as f:

        leaderboard = f.readline().rstrip().split()

        spectrum = []
        for mass in f.readline().rstrip().split():
            spectrum.append(int(mass))

        n = int(f.readline().rstrip())

    return leaderboard, spectrum, n

leaderboard, spectrum, n = read_input("week4_8.txt")

def linear_spectrum(peptide):

    masses = [0]
    for i in range(len(peptide)):
        total = 0
        for j in range(i, len(peptide)):
            total += aa_mass_table[peptide[j]]
            masses.append(total)

    return masses

def linear_score(peptide, spectrum):

    peptide_spectrum = linear_spectrum(peptide)

    peptide_counter = Counter(peptide_spectrum)
    spectrum_counter = Counter(spectrum)

    score = 0

    for mass in peptide_counter:

        score += min(peptide_counter[mass],spectrum_counter[mass])

    return score

def trim(leaderboard, spectrum, n):

    # Calculate the score of every peptide
    scored = []

    for peptide in leaderboard:

        score = linear_score(peptide, spectrum)
        scored.append((peptide, score))

    # Sort peptides according to decreasing score
    scored.sort(key=lambda x: x[1], reverse=True)

    # If there are N or fewer peptides, keep them all
    if len(scored) <= n:
        return [peptide for peptide, score in scored]

    # Score of the N-th peptide
    cutoff_score = scored[n - 1][1]

    # Keep N peptides PLUS all peptides tied with the N-th score
    result = []

    for peptide, score in scored:

        if score >= cutoff_score:
            result.append(peptide)
        else:
            break
    return result

result = trim(leaderboard, spectrum, n)

print(*result)