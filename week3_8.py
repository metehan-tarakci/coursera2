peptide = "HPSTIKKSMAEHEFCPTWPGYSFQKFWGDTARIRPVEVNV"

aa_mass_table = {
    'G':57, 'A':71, 'S':87, 'P':97, 'V':99, 'T':101, 'C':103, 'I':113, 'L':113, 'N':114, 
    'D':115, 'K':128, 'Q':128, 'E':129, 'M':131, 'H':137, 'F':147, 'R':156, 'Y':163, 'W':186
}

def linear_spectrum(peptide):
    """
    Returns all subpeptide masses of a LINEAR peptide,
    including 0 and the whole peptide.
    """

    masses = [0]

    # All possible contiguous subpeptides
    for i in range(len(peptide)):
        total = 0

        for j in range(i, len(peptide)):
            total += aa_mass_table[peptide[j]]
            masses.append(total)

    return sorted(masses)

print(*linear_spectrum(peptide))