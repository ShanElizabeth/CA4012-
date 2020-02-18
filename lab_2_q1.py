import nltk
from nltk.tokenize import word_tokenize

with open ('test.txt','r') as file:
	
	for line in file:
		print(word_tokenize(line))
