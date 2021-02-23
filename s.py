with open("_all.txt") as f:
	data_base = f.readlines()
l = []
for i in range(len(data_base)):
	l.append(data_base[i].split()[1])

with open("_ALL.txt","w") as f:
	print(*l,file=f,sep="\n")
