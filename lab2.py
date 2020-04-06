import re


def main():
    en = open("train_data_en.txt", "r+")
    fr = open("train_data_fr.txt", "r+")
    data_en = en.readlines()
    data_fr = fr.readlines()
    print(data_en)
    print(data_fr)
    new_en = []
    new_fr = []
    en=data_en.split('')
    print(en)
    i = 0

    #while i < len(data_en):
     #   en_sent = re.split("", data_en[i])
      #  print(en_sent)
       # fr_sent = re.split("[' ]", data_fr[i])
        #print(fr_sent)
        #if len(en_sent) <= 3 and len(fr_sent) <= 3:
         #   new_en.append(data_en)
          #  new_fr.append(data_fr)

        #i += 1

    #print(new_fr)
    #print(new_en)


if __name__ == '__main__':
    main()