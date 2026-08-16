cyclic_peptide_str = "LEQN"

n = len(cyclic_peptide_str)

double = cyclic_peptide_str + cyclic_peptide_str

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

print(*mass())