# Problem 15 : Independent Alleles
# TODO

def getLines(file):
    dna_strings = []
    dna = ""
    for line in file:
        if line.startswith(">Rosalind_"):
            if dna != "":
                dna_strings.append(dna)
            dna = ""
        else:
            dna += line.replace("\n", "")
    dna_strings.append(dna)
    return dna_strings


if __name__ == "__main__":
    file = open("data/rosalind_lcsm.txt", "r")
    print (getLines(file))