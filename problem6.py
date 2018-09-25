# Problem 6 : Counting Point Mutations

# Assumes that the strings have the same length!
def calculate_hamming_distance(dna_string1, dna_string2):
    diff = 0
    for i in range(0, len(dna_string1)-1):
        if (dna_string1[i] != dna_string2[i]):
            diff += 1
    return diff

if __name__ == "__main__":
    file = open("data/rosalind_hamm.txt", "r")
    first_line = file.readline()
    second_line = file.readline()
    print calculate_hamming_distance(first_line, second_line)