# Problem 7 : Mendel's First Law

# P(dominant) = 1 - P(recessive)
# P(recessive) = 0.5P(mm) + 0.5P(mn) + P(n0.5m) + P(nn)
def get_prob_dominant(k, m, n):
    prob_rec_mm = 0.5*(m/(k+m+n+0.0)) * 0.5*((m-1.0)/(k+m-1+n))
    prob_rec_mn = 0.5*(m/(k+m+n+0.0)) * (n/(k+m-1.0+n))
    prob_rec_nm = (n/(k+m+n+0.0)) * 0.5*(m/(k+m+n-1.0))
    prob_rec_nn = (n/(k+m+n+0.0)) * ((n-1)/(k+m+n-1.0))
    return 1-(prob_rec_mm+prob_rec_mn+prob_rec_nm+prob_rec_nn)


if __name__ == "__main__":
    file = open("data/rosalind_iprb.txt", "r")
    population = file.readline().split(" ")
    print get_prob_dominant(int(population[0]), int(population[1]), int(population[2]))