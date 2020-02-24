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
for lst in tokenfile:
	print(" ".join(lst))
	if len(lst)>4:
		print("too long")
	else:
		print("okay")

#for line in tokenfile:
#	for word in line:
#		if word!=" " or "\n":
#			newtoken.append(word)
#print(newtoken)