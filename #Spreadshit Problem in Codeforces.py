# your code goes here 
def convert(n): 
	s = '' 
	z = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
	 
	while n>0: 
		if n%26==0: 
			n = n/26 - 1 
			s+='Z' 
		else: 
			k = n%26 
			n = n/26 
			 
			s+=z[k-1] 
	 
	return s[::-1] 
	 
def sconvert(s): 
	z = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
	i = 0 
	 
	for l in s: 
	 
		k = z.index(l)+1 
		i = i*26+k 
		 
	return i 
		 
t = input() 
 
	 
for i in xrange(t): 
	s = raw_input() 
	n = len(s) 
	ans = '' 
	digits = False 
	if 'R' in s and 'C' in s: 
		m = s.index('R') 
		q = s.index('C') 
		k = m+1 
		while m<q: 
			if s[m].isdigit(): 
				digits = True 
			else: 
				digits = False 
			m+=1 
				 
	if 'R' in s and 'C' in s and digits: 
		rin = s.index('R') 
		cin = s.index('C') 
		row = int(s[rin+1:cin]) 
		col = int(s[cin+1:]) 
		ans = convert(col)+str(row) 
		 
			 
				 
	else: 
		col = '' 
		j = 0 
		while j<n and not s[j].isdigit(): 
			col+=s[j] 
			j+=1 
		col = sconvert(col) 
		row = int(s[j:]) 
		ans = 'R'+str(row)+'C'+str(col) 
			 
			 
	print (ans) 