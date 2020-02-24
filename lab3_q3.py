import math
with open ('text3.txt','r') as file:
	a=[]
	for line in file:
		a=line.split(' ')

#######referebces
r1=['the','gunman','was','shot','to','death','by','the','police','.']
r2=['the','gunman','was','shot','to','death','by','the','police','.']
r3=['police','killed','the','gunman','.']
r4=['the','gunman','was','shot','dead','by','the','police','.']

refs=[r1,r2,r3,r4]

############################
#REFERENCE N-GRAMS
def token_onegramrefs(refs):
	newrefs=[]
	for lst in refs:
		#print(lst)
		for j in range(0,len(lst)):
				newrefs.append(lst[j])
				#print(lst[j]+' '+lst[j+1])
	return newrefs
def token_twogramrefs(refs):
	newrefs=[]
	for lst in refs:
		#print(lst)
		for j in range(0,len(lst)-1):
				newrefs.append(lst[j]+' '+lst[j+1])
				#print(lst[j]+' '+lst[j+1])
	return newrefs

def token_threegramsrefs(refs):
	newrefs=[]
	for lst in refs:
		#print(lst)
		for i in range(0,len(lst)-1):
			#print(i)
			if(i+2)<=len(lst)-1:
				newrefs.append(lst[i]+' '+lst[i+1]+' '+lst[i+2])
		
	return (newrefs)

def token_fourgramrefs(refs):
	newrefs=[]
	for lst in refs:
		for i in range(0,len(lst)-1):
			#print(i)
			if(i+3)<=len(lst)-1:
				newrefs.append(lst[i]+' '+lst[i+1]+' '+lst[i+2]+' '+lst[i+3])
		
	return (newrefs)

#END OF REFERNCE N-GRAMS
#######################


#####################
#MT OUTPUT NGRAM
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
#END OF MT NGRAM
####################

#MATCHING NGRAMS FUNCTIONS
def match_onegram(a,refs):
	a=(one_gram(a))
	newrefs=token_onegramrefs(refs)
	score=0
	for word in a:
		if word in newrefs:
			#print(word)
			score +=1
	if score==0:
		return 0
	else:
		return (score/len(a))

def match_twogram(a,refs):
	score=0
	t=two_gram(a)
	newrefs=token_twogramrefs(refs)
	for word in t:
		if word in newrefs:
			#print(word)
			score+=1
	
	return (score/len(t))


def match_threegram(a,refs):
	score=0
	t=three_gram(a)
	newrefs=token_threegramsrefs(refs)
	for word in t:
		if word in newrefs:
			#print(word)
			score+=1
	if score==0:
		return 0
	else:
		return (score/len(t))


def match_fourgram(a,r):
	score=0
	t=four_gram(a)
	newrefs=token_fourgramrefs(refs)

	for word in t:
		if word in newrefs:
			#print(word)
			score+=1
	return (score/len(t))
#####getting average ken of all references 

def ref_average(refs):
	score=0
	#return(len(refs))
	for lst in refs:
		
		score+=len(lst)
		#print(score)
	return score/len(refs)
######### getting the bevrity penalty an droynding ref len number
def brevity_penalty(a,refs):
	newrefs_len_avg=ref_average(refs)
	rounded_avg=math.ceil(newrefs_len_avg)
	#print(len(a))
	#print(rounded_avg)
	return(len(a)/(rounded_avg))

############################
#calculating ngram score
n_gramscore=(
	(match_onegram(a,refs))*
	(match_twogram(a,refs))*
	(match_threegram(a,refs))*
	(match_fourgram(a,refs)))

print(match_onegram(a,refs))
print(match_twogram(a,refs))
print(match_threegram(a,refs))
print(match_fourgram(a,refs))
######### to the power of 1/4 because 4 n grams
n_gramscore=n_gramscore**0.25

########adding brevity penalty
bleu_score=(n_gramscore*brevity_penalty(a,refs))

######bleu score final score
print(bleu_score)