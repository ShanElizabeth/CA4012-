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

def match_onegram(a,r):
	a=(one_gram(a))
	score=0
	for word in a:
		if word in r:
			#print(word)
			score +=1
	return (score/len(a))

def match_twogram(a,r):
	score=0
	t=two_gram(a)
	rt=two_gram(r)
	for word in t:
		if word in rt:
			#print(word)
			score+=1
	return (score/len(t))


def match_threegram(a,r):
	score=0
	t=three_gram(a)
	rt=three_gram(r)
	for word in t:
		if word in rt:
			#print(word)
			score+=1
	return (score/len(t))


def match_fourgram(a,r):
	score=0
	t=four_gram(a)
	rt=four_gram(r)

	for word in t:
		if word in rt:
			#print(word)
			score+=1
	return (score/len(t))

def brevity_penalty(a,r):
	return(len(a)/len(r))

n_gramscore=(
	(match_onegram(a,r))*
	(match_twogram(a,r))*
	(match_threegram(a,r))*
	(match_fourgram(a,r)))


n_gramscore=n_gramscore**0.25
bleu_score=(n_gramscore*brevity_penalty(a,r))
print(bleu_score)