def solve(s1, s2):
    n = len(s1)
    ham = 0
    for i in range(n):
        if s1[i] != s2[i]:
            ham += 1
    print(ham)

if __name__ == "__main__":
    dataset_path = "./data/rosalind_hamm.txt"
    f = open(dataset_path, "r")
    l1 = f.readline()
    l2 = f.readline()
    solve(l1, l2)