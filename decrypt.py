import ngram_score as ns
from random import seed
from random import random
from random import randint
cipher = "RDYQYTXCQYKEX,MYRQGKJLCJIEJFIJRO,JIBGJHVCHYIG,DQCHCDCKGOYTHXZCIC,BHYAGIZJCIRFHTEFCMHCGLRYICDATRJIO,DQCHCZJVJKMKYYEAGLCXZJVJKQGIEXTIZKCGI.BHYABYHRQRQCBGRGKKYJIXYBRQCXCRDYBYCXGUGJHYBXRGH-ZHYXX'EKYVCHXRGLCRQCJHKJBC;DQYXCAJXGEVCIRTHCEUJRCYTXYVCHRQHYDXEYDJRQRQCJHECGRQMTHORQCJHUGHCIRX'XRHJBC.RQCBCGHBTKUGXXGFCYBRQCJHECGRQ-AGHL'EKYVC,GIERQCZYIRJITGIZCYBRQCJHUGHCIRX'HGFC,DQJZQ,MTRRQCJHZQJKEHCI'XCIE,IYTFQRZYTKEHCAYVC,JXIYDRQCRDYQYTHX'RHGBBJZYBYTHXRGFC;RQCDQJZQJBOYTDJRQUGRJCIRCGHXGRRCIE,DQGRQCHCXQGKKAJXX,YTHRYJKXQGKKXRHJVCRY"

sub_dict = {'C': 'E', 'R': 'T', 'Y': 'A', 'H': 'O', 'J': 'I', 'Q': 'N', 'G': 'S', 'X': 'H', 'I': 'R', 'K': 'D', 'B': 'L', 'E': 'C', 'T': 'U', 'D': 'M', 'Z': 'W', 'V': 'F', 'A': 'G', 'F': 'Y', 'U': 'P', 'L': 'B', 'M': 'V', 'O': 'K', 'N': 'J', 'P': 'X', 'S': 'Q', 'W': 'Z'}


probability = 3/26
def decrypt(cipher,sub_dict):
   plain = ""
   for x in cipher:
      if x in sub_dict.keys():
         plain+=sub_dict[x]
   else:
      plain+=x      
   return plain

seed(1)
plain = decrypt(cipher,sub_dict)
fitness = ns.ngram_score('quadgrams.txt')

fit = fitness.score(plain)
print("The starting fitness is: "+str(fit))
for i in range(100):
   candidate = sub_dict.copy()
   for j in range(1000):
      newdict = sub_dict.copy()
      for key in newdict:
         if(random() < probability):
            target = list(sub_dict.keys())[randint(0,len(sub_dict.keys())-1)]
            temp = newdict[key]
            newdict[key] = newdict[target]
            newdict[target] = temp
      plain = decrypt(cipher,newdict)
      score = fitness.score(plain)
      if score > fit:
         fit = score
         candidate = newdict
         print("The new fitness is: "+str(fit))
   if candidate == sub_dict:
      print("FINISHED\n")
      break
   sub_dict = candidate
print(decrypt(cipher,sub_dict))
    




 


     
      






