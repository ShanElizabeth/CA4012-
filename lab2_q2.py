import os 
def clean(file,num):
	with open('Etmp.txt','w') as tmp:
		for line in file:
			if len(line)>num:
				print(line)
	#			tmp.write(line)
	

with open('Eng_test.txt','r') as file:
	clean(file,4)

