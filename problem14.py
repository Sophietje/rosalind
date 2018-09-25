# Problem 14 : Finding a Shared Motif

def getLongestCommonSubstring(strings):
    tested = []
    for input in strings:
        j = len(input)
        while j>0:
            # j is length of substring
            for i in range(0, len(input)-j+1):
                substring = input[i:i+j]
                found = True
                for string in strings:
                    if substring not in string:
                        found = False
                if found:
                    return substring
            j = j-1
    return ""

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
    print getLongestCommonSubstring(getLines(file))