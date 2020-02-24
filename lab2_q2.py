#tokenfile=[]
#import re
#with open ('Eng_test.txt','r') as file:
	
##	for line in file:
##		tokenfile.append(line.split(" "))		
#print (tokenfile)
import re
tokenfile=[]
spliton=","+"'"+"!"+","+" "
with open('Eng_test.txt','r') as file:
	for line in file:
		line.rstrip("\n")
		tokenfile.append((re.findall(r'(\'|,|!|\?|[\w]+)', line)))
print (tokenfile)
for i in range(0,len())
	print(" ".join(lst))
	if len(lst)>4:
		print("too long")
	else:
		print("okay")

