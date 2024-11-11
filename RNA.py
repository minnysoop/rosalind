code = open('./data/rosalind_rna.txt', 'r')
code = code.read()
rna = code.replace('T', 'U')
print(rna)