k, m, n = float(input()),float(input()),float(input()) 
t = k + m + n

p_AAAA = 1
p_AAaa = 1
p_AAAa = 1
p_AaAa = 3/4
p_Aaaa = 1/2
p_aaaa = 0

prob = ((p_AAAA*k*(k-1) + p_AaAa*m*(m-1) + p_aaaa*n*(n-1)  
	+ 2*p_AAaa*k*n + 2*p_AAAa*k*m + 2*p_Aaaa*m*n)/(t*(t-1)))
print(prob)
