n, k = int(input()), int(input())

f1 = int(1)
f2 = int(1)
temp = int(0)

for i in range(0,n-2):
	temp = f2
	f2 = f1*k + f2
	f1 = temp
print(f2)