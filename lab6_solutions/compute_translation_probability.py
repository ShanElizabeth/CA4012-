# ID: 16304263
# Name: Shannon Mulgrew

#need to write this function because i need to iterate through the dictionary within itself to match 
#and see if the element at position 1 matches the word pair
#so wpair= (la, the)
#for e in c = (la,the )
#postion wpair[1]==e[1] so add the value to the new list everytime it matches
def matchin(c,wpair):
	# print(c)
	# print(wpair)

	p = []
	for e in c:
		if e[1] == wpair[1]:
			p.append(c[e])
			# print(p)
	#return the sum of each and divide in original function
	return (sum(p))


def calculate_translation_probability(c):
    ''' Calculates the translation probabilities given the fractional counts
        
        :param c: fractional counts (dictionary)
        :returns: translation probabilities (dictionary)
    '''
    newdict = {}
    for i in c:
    	p = matchin(c,i)
    	newdict[i] = c[i]/p #divide by total praobabolity sum for each value in new dict
    return newdict


# Do not modify the following lines:
def main():
    c = {('la', 'the'): 0.5, ('maison', 'the'): 0.5, ('la', 'house'): 0.5, ('maison', 'house'): 1.5}
    
    t = calculate_translation_probability(c)
    
    print(t)


if __name__ == "__main__":
    main()