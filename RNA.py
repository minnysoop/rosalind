code = open("./data/rosalind_dna.txt", "r")
code = code.read()
a,c,g,t = code.count('A'), code.count('C'), code.count('G'), code.count('T')
print(a,c,g,t)