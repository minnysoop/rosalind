def solve(data):
    d = data.split()
    n = int(d[0])
    k = int(d[1])

    a = 1
    b = 1
    c = None
    i = 2
    while (i < n):
        c = b + k * a
        a = b
        b = c
        i += 1
    print(c)


if __name__ == "__main__":
    dataset_path = "./data/rosalind_fib.txt"
    data = open(dataset_path, 'r')
    data = data.read()
    solve(data)