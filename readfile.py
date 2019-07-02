fname = input("Enter file name\t")
handle = open(fname)
d = dict()
for line in handle :
	line = line.rstrip()
	wds = line.split()
	for w in wds:
		d[w] = d.get(w , 0) + 1
print(d)
maxkey = -1
maxvalue = -1

for k,v in d.items() :
	if v > maxvalue :
		maxvalue = v
		maxkey = k

print( maxkey , maxvalue )	

