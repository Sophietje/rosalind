# Problem 4 : Rabbits and Recurrence Relations

def recurringRabbits(n, k):
    # Start at month 0 with 1 rabbit pair
    rabbitPairsPrev = 1
    # Two months prior, at the beginning we have no reproduction-age rabbits
    rabbitPairsPrev2 = 0
    # For positive integers 1 <= n <= 40
    for i in range(1, n):
        #print "round: "+str(i)
        temp = rabbitPairsPrev2
        rabbitPairsPrev2 = rabbitPairsPrev2 + rabbitPairsPrev
        rabbitPairsPrev = k*temp

        rabbitPairs = rabbitPairsPrev + rabbitPairsPrev2
        #print str(rabbitPairs) + " = "+str(rabbitPairsPrev) +" + "+ str(rabbitPairsPrev2)

    print rabbitPairs

if __name__ == "__main__":
    recurringRabbits(31, 2)