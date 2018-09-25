# Problem 2 : Transcribing DNA into RNA

def replace(input):
    print input.replace("T", "U")

if __name__ == "__main__":
    f = open("data/rosalind_rna_1_dataset.txt", "r")
    replace(f.read())