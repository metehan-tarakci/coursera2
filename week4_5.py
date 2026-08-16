def read_mass_spectrometer(file):
    spectrum = []
    with open(file, "r") as f:
        for mass in f.readline().rstrip().split():
            spectrum.append(int(mass))
    return spectrum

spectrum = read_mass_spectrometer("week4_5.txt")

def convolution(spectrum):
    convolution = []
    for i in range(len(spectrum)):
        for j in range(0, i):
            diff = spectrum[i] - spectrum[j]
            if not (diff == 0):
                convolution.append(diff)
    return convolution
print(*convolution(spectrum))
