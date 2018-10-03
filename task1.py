#task1

def task1():
	fin=open("running-config.cfg") #opening the file
	list1= []                      #creating an empty list
	for line in fin:
		line=line.strip()              #getting rid of white spaces
		line=line.split()              #this will create a list 
		if(line[0] ==  "interface"): #checks if the 1st word is iterface
			list1.append(line[1])  #assigning the  next  item  
	print(list1)
task1()
