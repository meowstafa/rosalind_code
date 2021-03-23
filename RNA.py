f = open("rosalind_rna.txt")
s = f.readline()

l = int(len(s))
r = ""
for i in range(0,l):
	x = s[i]
	if x == 'T': 
		x = 'U'
	r = r + x
print(r)
f.close()

