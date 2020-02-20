import nltk
from nltk.tokenize import word_tokenize
tokenfile=[]
with open ('Eng_test.txt','r') as file,open('Eng_token.txt','w') as token:
	
	for line in file:
		tokenfile=(word_tokenize(line))
		print(tokenfile)
