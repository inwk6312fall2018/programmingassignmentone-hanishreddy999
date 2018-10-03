#Task 2
def replace_ip(file):
	fin=open(file) #opening a file
	a=[] 		#creating an empty list
	b=[]
	oldip= []
	newip= []
	for line in fin:
		line=line.strip()
		line=line.split()
		a.append(line)
	for i in  range(len(a)):
		if a[i] == "ip" and a[i+1] == "address" :  #checks  if ip add exists
			b.append(a[i+2])
	for i in  b: 
		oldip.append(i.split('.'))  #splits using  """.""" 
	for i in oldip:
		i[0]=10                       #  assigning 10  
		newip.append('.'.join(i))
	return newip #returns  the  new ip add with 10 starting
print(replace_ip("running-config.cfg"))