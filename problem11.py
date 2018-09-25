# Problem 11 : Mortal Fibonacci Rabbits

def mortalRabbits(n, m):
    rabbits = [0]*m
    # Start with one pair of rabbits
    rabbits[0] = 1
    for i in range(0, n-1):
        # All rabbits become 1 month older
        rabbits.insert(0, 0)
        dying = rabbits.pop()
        # All rabbits who are mature will produce offspring for next generation
        rabbits[0] = sum(rabbits[2:]) + dying
    return sum(rabbits)


if __name__ == "__main__":
    file = open("data/rosalind_fibd.txt", "r")
    n, m = file.readline().split(" ")
    print mortalRabbits(int(n), int(m))