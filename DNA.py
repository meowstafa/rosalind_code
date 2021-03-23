

f = open("rosalind_dna.txt")
s = f.readline()

l = int(len(s))
a = int(0)
t = int(0)
g = int(0)
c = int(0)
for i in range(0,l):
	x = s[i]
	if x == 'A': 
		a = a + 1
	elif x == 'T': 
		t = t + 1
	elif x == 'G':
		g = g + 1
	elif x == 'C':
		c = c + 1
print(a,c,g,t)
