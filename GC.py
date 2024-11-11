def solve(data, name):
    d = len(data)
    n = 0

    for i in range(0, d):
        if data[i] == 'C' or data[i] == 'G':
            n += 1
    
    gc = n/d * 100
    return name, gc

if __name__ == "__main__":
    dataset_path = "data/rosalind_gc.txt"
    f = open(dataset_path, 'r')
    data = f.read().replace('\n', '').split('>')[1:]
    max_name = None
    max_gc = -1
    for s in data:
        name = s[:13]
        data = s[13:]
        p, gc = solve(data, name)
        if gc > max_gc:
            max_gc = gc
            max_name = p
    print(max_name, '\n', max_gc, sep='')