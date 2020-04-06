import sys
from collections import defaultdict

if len(sys.argv) < 2:
  print ('Usage: %s <input_source_file> <input_target_file> <output_lexical_translation>' % sys.argv[0])
  sys.exit()

def data_read(src_in, tgt_in):
  with open(src_in) as fsrc, open(tgt_in) as ftgt:
    src_lines = fsrc.readlines()
    tgt_lines = ftgt.readlines()
    #define source, target and pair dictionaries
    src_dict = {}
    tgt_dict = {}
    src_tgt_dict = {}
    #collect vocabulary of source, target and source-target
    for i in range(len(src_lines)):
      src_line = src_lines[i].strip().split()
      tgt_line = tgt_lines[i].strip().split()
      for srcword in src_line:
        src_dict[srcword] = 1
        # src_dict {'the': 1, 'house': 1}
        for tgtword in tgt_line:
          tgt_dict[tgtword] = 1
          #tgt_dict {'la': 1, 'maison': 1}
          src_tgt_dict[(tgtword, srcword)] = 0
       	  #src_tgt_dict {('la', 'the'): 0, ('maison', 'the'): 0, ('la', 'house'): 0, ('maison', 'house'): 0}

    return src_lines, tgt_lines, src_dict, tgt_dict, src_tgt_dict

def initialization(src_dict, src_tgt_dict):
  #uniformly initialize the lexical translation probability for each word pair t(e,f)
  src_voc_size = len(src_dict)
  #----1/unuqie words in src file
  initial_value = 1.0/src_voc_size
  for (tgtword, srcword) in src_tgt_dict:
    src_tgt_dict[(tgtword, srcword)] = initial_value
    # print(src_tgt_dict)
# {('la', 'the'): 0.5, ('maison', 'the'): 0.5, ('la', 'house'): 0.5, ('maison', 'house'): 0.5}
  print("src_tgt_dict",src_tgt_dict)
  return src_tgt_dict

def run_EM(src_lines, tgt_lines, src_tgt_dict, src_dict, tgt_dict, iterNum):

  #run iterNum times
  for i in range(iterNum): #2
    print(src_tgt_dict)
    #initialize
    counts = defaultdict(float) #counts of each word pair (e,f) //counts defaultdict(<class 'float'>, {
    total = defaultdict(float)  #normalization factor for estimating the new lexical translation probability for word pair (e,f)
    print("i",i)
    #for all sentence pairs, compute normalization
    for j in range(len(src_lines)):  #src_lines ['the house\n', 'house']
      tgt_words = tgt_lines[j].strip().split()
      src_words = src_lines[j].strip().split()
      s_total = defaultdict(float)
      print("j",j)

      for tgtword in tgt_words:
        for srcword in src_words:
        	s_total[tgtword] += src_tgt_dict[(tgtword, srcword)]
        	print("s_total ",tgtword," ",srcword," ",s_total[tgtword])
      print("hello")
      print(s_total)
      #collect counts
      for tgtword in tgt_words:
        for srcword in src_words:
          print("i loop")
          counts[(tgtword, srcword)] += (src_tgt_dict[(tgtword, srcword)] / s_total[tgtword])
          print(tgtword," ",srcword)
          print((src_tgt_dict[(tgtword, srcword)] / s_total[tgtword]))
          print(counts[(tgtword, srcword)])
          total[srcword] += (src_tgt_dict[(tgtword, srcword)] / s_total[tgtword])
          print(tgtword," ",srcword)
          print((src_tgt_dict[(tgtword, srcword)] / s_total[tgtword]))
          print(total[srcword])
      print("counts dict",counts)
      print("total dict",total)
    
         #estimate probabilities    
    for srcword in src_dict:
      for tgtword in tgt_dict:
        src_tgt_dict[(tgtword, srcword)] = counts[(tgtword, srcword)] / total[srcword] 
        print(srcword," ",tgtword)
        print(counts[(tgtword, srcword)] / total[srcword])

  return src_tgt_dict


if __name__ == "__main__":
  
    src_lines, tgt_lines, src_dict, tgt_dict, src_tgt_dict = data_read(sys.argv[1], sys.argv[2])

    src_tgt_dict = initialization(src_dict, src_tgt_dict)
    iterNum = 2
    src_tgt_dict = run_EM(src_lines, tgt_lines, src_tgt_dict, src_dict, tgt_dict, iterNum)

    with open(sys.argv[3], 'w') as fout:
      for (tgtword, srcword) in src_tgt_dict:
        fout.write(tgtword + ' ' + srcword + ' ' + str(src_tgt_dict[(tgtword, srcword)]) + '\n')


