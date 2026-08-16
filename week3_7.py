from collections import Counter
"""
Start with amino acids
        ↓
Expand each candidate
        ↓
Calculate its subpeptide masses
        ↓
Are ALL masses in the spectrum?
        ↓
YES → keep candidate
NO  → remove candidate
        ↓
If total mass = 427 → complete candidate
Otherwise → expand again
"""
aa_mass_list = [
    57, 71, 87, 97, 99, 101, 103, 113, 114,
    115, 128, 129, 131, 137, 147, 156, 163, 186
]


def read_mass_spectrometer(file):
    spectrum = []

    with open(file, "r") as f:
        for mass in f.readline().rstrip().split():
            spectrum.append(int(mass))

    return spectrum


spectrum = read_mass_spectrometer("week3_7.txt")


def linear_spectrum(peptide):
    """
    Returns all subpeptide masses of a LINEAR peptide,
    including 0 and the whole peptide.
    """
    masses = [0]
    n = len(peptide)
    # All possible contiguous subpeptides

    for i in range(n): # This chooses where the subpeptide starts.
        total = 0 # Every time we choose a new starting position, we reset the mass to zero.

        for j in range(i, n): # This chooses how far we extend the subpeptide. 
                                         # So: i = starting position j = current ending position
            total += peptide[j]
            masses.append(total)

    return masses


def cyclic_spectrum(peptide): # This assumes peptide is already a list of masses unlike week3_4.py
    masses = [0]
    n = len(peptide)

    for i in range(n):
        total = 0

        for j in range(n - 1):
            total += peptide[(i + j) % n] # The % n makes the index wrap back to the beginning, 
                                          # which is exactly what makes the peptide cyclic
            masses.append(total)

    masses.append(sum(peptide))

    return sorted(masses)


def consistent(peptide, spectrum):
    """
    Checks whether EVERY subpeptide mass of peptide
    occurs in the experimental spectrum with the
    correct multiplicity.
    """

    peptide_spectrum = linear_spectrum(peptide) # compare each subpeptide against the linear spectrum

    peptide_counter = Counter(peptide_spectrum)
    spectrum_counter = Counter(spectrum)

    for mass, count in peptide_counter.items():

        if count > spectrum_counter[mass]:
            return False

    return True


def expand(candidates):
    """
    Add every possible amino-acid mass to every
    candidate peptide.
    """

    new_candidates = []

    for peptide in candidates:

        for mass in aa_mass_list:

            new_peptide = peptide + [mass]

            new_candidates.append(new_peptide)

    return new_candidates


def cyclopeptide_sequencing(spectrum):

    parent_mass = max(spectrum)

    candidates = [[]]
    final_peptides = []

    while candidates:

        # Add one amino acid to every candidate
        candidates = expand(candidates)

        next_candidates = []

        for peptide in candidates:

            mass = sum(peptide)

            # If peptide has the correct total mass
            if mass == parent_mass:

                # Check its CYCLIC spectrum against
                # the experimental spectrum
                if Counter(cyclic_spectrum(peptide)) == Counter(spectrum):

                    final_peptides.append(peptide)

            # If peptide is smaller than parent mass,
            # check whether its LINEAR spectrum is
            # still consistent with the experiment.
            elif mass < parent_mass:

                if consistent(peptide, spectrum):
                    next_candidates.append(peptide)

        candidates = next_candidates

    return final_peptides


result = cyclopeptide_sequencing(spectrum)

for peptide in result:
    print("-".join(map(str, peptide)), end =" ")