cipher = "RDYQYTXCQYKEX,MYRQGKJLCJIEJFIJRO,JIBGJHVCHYIG,DQCHCDCKGOYTHXZCIC,BHYAGIZJCIRFHTEFCMHCGLRYICDATRJIO,DQCHCZJVJKMKYYEAGLCXZJVJKQGIEXTIZKCGI.BHYABYHRQRQCBGRGKKYJIXYBRQCXCRDYBYCXGUGJHYBXRGH-ZHYXX'EKYVCHXRGLCRQCJHKJBC;DQYXCAJXGEVCIRTHCEUJRCYTXYVCHRQHYDXEYDJRQRQCJHECGRQMTHORQCJHUGHCIRX'XRHJBC.RQCBCGHBTKUGXXGFCYBRQCJHECGRQ-AGHL'EKYVC,GIERQCZYIRJITGIZCYBRQCJHUGHCIRX'HGFC,DQJZQ,MTRRQCJHZQJKEHCI'XCIE,IYTFQRZYTKEHCAYVC,JXIYDRQCRDYQYTHX'RHGBBJZYBYTHXRGFC;RQCDQJZQJBOYTDJRQUGRJCIRCGHXGRRCIE,DQGRQCHCXQGKKAJXX,YTHRYJKXQGKKXRHJVCRY"

avoid = ["-"," ","'",",",";","."]

freq = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0}

ENG_freq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}


sub_dict = {}


for x in cipher:
  if x not in avoid:
     freq[x]+=1
      
#dict ordered by most freq characters
freq = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1],reverse = True)}

for i in range(len(list(freq.keys()))):
   sub_dict[list(freq.keys())[i]] = list(ENG_freq.keys())[i]


print(sub_dict)






