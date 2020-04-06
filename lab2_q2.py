#tokenfile=[]
#import re
#with open ('Eng_test.txt','r') as file:
	
##	for line in file:
##		tokenfile.append(line.split(" "))		
#print (tokenfile)
import re
tokenfile=[]
tokenfile_fr=[]

with open('train_data_en.txt','r') as file:
	for line in file:
		line.rstrip("\n")
		tokenfile.append((re.findall(r'(\'|,|!|\?|[\w]+)', line)))
	print(tokenfile)
with open("new_eng_file",'w') as newfile:

	for i in range(0,len(tokenfile)-1):
		if len(tokenfile[i])>4:
			print(tokenfile[i])
			print("too long")
		else:
			new=" ".join(tokenfile[i])
			newfile.write(new+"\n")
