fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
	line=line.rstrip()
	words=line.split()
    for word in words:
    	pos=lst.find(word)
        if pos==-1:
            lst.append(word)
lst.sort();
print(lst)
	
