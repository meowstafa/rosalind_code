
s = ""
sc = ""
x = ""
try:
	f = open("rosalind_revc.txt")
except:
	s = str(input())
else:
	s = f.readline()

l = int(len(s))
for i in range(0,l):
	x = s[i]
	if x == "A": 
		sc = "T" + sc
	elif x == "T":
		sc = "A" + sc
	elif x == "G":
		sc = "C" + sc
	elif x == "C":
		sc = "G" + sc
print(sc)
	