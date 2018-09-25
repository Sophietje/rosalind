# Problem 10 : Consensus and Profile

def get_substring_locations(text, substring):
    result = ""
    for i in range(0, len(text)):
        if text[i:i+len(substring)] == substring:
            result += str(i+1) + " "
    return result


if __name__ == "__main__":
    #print find_substring_locations("GATATATGCATATACTT", "ATAT")
    file = open("data/rosalind_subs.txt", "r")
    full_string = file.readline().replace("\n", "")
    print full_string
    substring = file.readline().replace("\n", "")
    print substring
    print get_substring_locations(full_string, substring)