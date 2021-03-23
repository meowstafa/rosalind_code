n, m = int(input()), int(input())

f1 = int(1)
f2 = int(1)
temp = int(0)
arr =[]

for i in range(0, n):
	if i < m:
		temp = f2
		f2 = f1 + f2
		f1 = temp
		arr.append(f2)
	else:
		temp = f2
		f2 = f1 + f2 - arr[i-m]
		f1 = temp
		arr.append(f2)
print(f2)
