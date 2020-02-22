with open ('text3.txt','r') as file:
	a=[]
	for line in file:
		a=line.split(' ')

def one_gram(a):
	return (a)

def two_gram(a):
	e=[]
	for i in range(0,len(a)-1) :
		e.append(a[i]+' '+a[i+1])
	return(e)
def three_gram(a):
	e=[]
	for i in range(0,len(a)-1) :
		if (i+2) <= len(a)-1:
			e.append(a[i]+' '+a[i+1]+' '+a[i+2])
		else:
			return(e)
	return(e)
def four_gram(a):
	e=[]
	for i in range(0,len(a)-1):
		if (i+3)<=len(a)-1:
			e.append(a[i]+' '+a[i+1]+' '+a[i+2]+ ' '+a[i+3])
		else:
			return(e)
print(one_gram(a))
print(two_gram(a))
print(three_gram(a))
print(four_gram(a))
