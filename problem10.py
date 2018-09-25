# Problem 10 : Consensus and Profile

def get_profile_matrix(file_contents):
    strings = []
    first = True
    for line in file_contents:
        if line[0] == ">":
            if not first:
                strings.append(string)
            string = ""
            first = False
        else:
            string += line.replace("\n", "")

    strings.append(string)
    print strings
    n = len(strings[0])
    result = {"A": [0] * n, "C": [0] * n, "G": [0] * n, "T": [0] * n}

    for line in strings:
        if line[0] != ">":
            #ISSUE: There is a newline between consecutive characters
            for i in range(0, len(line)):
                if line[i] in result.keys():
                    value = result.get(line[i])
                    value[i] += 1
                    result[line[i]] = value
    return result


def get_consensus(matrix):
    result = ""
    for i in range(0, len(matrix["A"])):
        maxKey = max(matrix, key=lambda j: matrix[j][i])
        result += maxKey
    return result.strip()


if __name__ == "__main__":
    #print find_substring_locations("GATATATGCATATACTT", "ATAT")
    file = open("data/rosalind_cons.txt", "r")
    matrix = get_profile_matrix(file)
    print get_consensus(matrix)
    res = ""
    for key in ["A", "C", "G", "T"]:
        print key+":",
        for v in matrix[key]:
            print v,
        print