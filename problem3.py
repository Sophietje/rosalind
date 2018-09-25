# Problem 3 : Complementing a Strand of DNA

def reverse_complement(input):
    reversed = input[::-1]
    replaceA = reversed.replace("A", "1")
    replaceT = replaceA.replace("T", "A")
    replaceAT = replaceT.replace("1", "T")
    replaceC = replaceAT.replace("C", "2")
    replaceG = replaceC.replace("G", "C")
    replaceCG = replaceG.replace("2", "G")

    print replaceCG

if __name__ == "__main__":
    f = open("data/rosalind_revc_2_dataset.txt", "r")
    reverse_complement(f.read())