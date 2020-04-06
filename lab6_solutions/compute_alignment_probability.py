# ID: 16304263
# Name: Shannon Mulgrew

from collections import defaultdict
def calculate_alignment_probability(f, e, a, T, epsilon=1.0):
    ''' Calculates the probability of a sentence given the alignment, the translation
        probabilities and a normalization constant
        
        :param f: the foreign sentence (string)
        :param e: the target sentence (string)
        :param a: the alignment (dictionary)
        :param T: the translation probabilities (dictionary)
        :param epsilon: normalization constant (float, default = 1.0)
        :returns: the probability of the sentence (float)
    '''
        
    # print("foreign sentence",f)
    # print("target setence",e)
    # print("alignment dict",a)
    # print("Translation probabilities",T)
    overall=1
    e=e.split()
    f=f.split()

    for i in T:
        #if i[0] is in the target sentence and the i[1] in the foreign 
        # print(i[0])
        # print(i[1])
        if i[0] in a and i[1] in f:
            #then *= whatever value is in the translation proabbalilty dictionary  at that osition i 
            overall*=T[i]

    tmp=(len(f)+1)**len(e)
    ans=epsilon/tmp
    overall =overall*ans
    return overall

# Do not modify the following lines
def main():
    a = {'wo': 'am', 'zai': 'i', 'xuexi': 'studying'}
    T={('wo', 'am'): 0.5, ('ziji', 'i'): 0.2, ('wo', 'me'): 0.3, ('ziji', 'me'): 0.1, ('zai', 'i'): 0.3, ('shi', 'am'): 0.5, ('zai', 'is'): 0.2, ('shi', 'is'): 0.5, ('xuexi', 'study'): 0.6, ('yanjiu', 'study'): 0.3, ('xuexi', 'studying'): 0.5, ('yanjiu', 'studying'): 0.5}
    f = 'i am studying'
    e = 'wo zai xuexi'
    
    p_a = calculate_alignment_probability(f, e, a, T)
    
    print(p_a)


if __name__ == "__main__":
    main()