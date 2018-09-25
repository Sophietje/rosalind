# Problem 13 : Calculating Expected Offspring

probs = {"AA-AA": 1.0,
         "AA-Aa": 1.0,
         "AA-aa": 1.0,
         "Aa-Aa": 0.75,
         "Aa-aa": 0.5,
         "aa-aa": 0.0}


def getNumDominantOffspring(a, b, c, d, e, f):
    return 2*(a*probs.get("AA-AA") + b*probs.get("AA-Aa") + c*probs.get("AA-aa") + d*probs.get("Aa-Aa") + e*probs.get("Aa-aa") + f*probs.get("aa-aa"))

if __name__ == "__main__":
    file = open("data/rosalind_iev.txt", "r")
    a, b, c, d, e, f = file.readline().split(" ")
    print getNumDominantOffspring(int(a), int(b), int(c), int(d), int(e), int(f))