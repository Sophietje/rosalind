# Problem 5 : Computing GC Content

def get_GC_content(dna_string):
    count_c = 0.0
    count_g = 0.0
    count = 0.0
    for c in dna_string:
        if (c != "\n"):
            if c == "C":
                count_c += 1
            elif c == "G":
                count_g += 1
            count += 1
    return ((count_c+count_g)/count)*100

if __name__ == "__main__":
    file = open("data/rosalind_gc.txt", "r")
    max_GC_content = -1
    dict = {}
    first = True
    dna = ""
    for line in file:
        # If it is an identifier then we will need to adapt the dict
        if line[0] == ">":
            # If there was a previous identifier, then add this to the dict
            if not first:
                dict[id] = get_GC_content(dna)
                dna = ""
            # Remember identifier to add to dict
            id = line[1:]
            first = False
        else:
            # Store all lines describing the dna string
            dna += line
    # Add last item to dict
    dict[id] = get_GC_content(dna)
    print dict
    # Print result
    print str(max(dict.iterkeys(), key=(lambda key: dict[key]))) + str(dict[max(dict.iterkeys(), key=(lambda key: dict[key]))])