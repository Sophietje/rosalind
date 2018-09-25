# Problem 12 : Overlap Graphs

def overlap(s, t):
    suffix = s[-3:]
    prefix = t[:3]
    return suffix == prefix


def getAdjacencyList(file_contents):
    # Construct list of nodes
    nodes = []
    first = True
    dna = ""
    name = ""
    for line in file_contents:
        if line[0] != ">":
            dna += line.replace("\n", "")
        else:
            if not first:
                nodes.append(tuple([name, dna]))
            name = line.replace("\n", "").replace(">", "")
            dna = ""
            first = False
    nodes.append(tuple([name, dna]))
    edges = []
    for (origin, s) in nodes:
        for (destination, t) in nodes:
            if s != t:
                if overlap(s,t):
                    edges.append(tuple([origin, destination]))
    return edges

if __name__ == "__main__":
    file = open("data/rosalind_grph.txt", "r")
    for (origin, destination) in getAdjacencyList(file):
        print origin + " " + destination