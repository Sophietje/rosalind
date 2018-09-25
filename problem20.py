# Problem 20 : Calculating Protein Mass
def getMonoisotopicMassTable():
    file = open("data/monoisotopic_mass_table.txt", "r")
    table = {}
    for line in file:
        parts = line.split(" ")
        table[parts[0]] = float(parts[3].replace("\n", ""))
    return table


def getProteinMass(protein_string):
    mass = 0
    protein_string = protein_string.replace("\n", "")
    for s in protein_string:
        mass += table[s]
    return mass


if __name__ == "__main__":
    file = open("data/rosalind_prtm.txt", "r")
    table = getMonoisotopicMassTable()
    print getProteinMass(file.readline())