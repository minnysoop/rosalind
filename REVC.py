s = open("data/rosalind_revc.txt", 'r')
s = s.read()
d = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C'
}
n = ""
i = len(s) - 1
while (i >= 0):
    if d.get(s[i]):
        n += d[s[i]]
    i -= 1
print(n)
