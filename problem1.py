# Problem 1 : Counting DNA Nucleotides

def count(input):
    countA = input.count("A")
    countC = input.count("C")
    countG = input.count("G")
    countT = input.count("T")
    print(str(countA)+" "+str(countC)+" "+str(countG)+" "+str(countT))


if __name__ == "__main__":
    f = open("data/rosalind_dna_1_dataset.txt", "r")
    count(f.read())