###### this is the first .py file ###########
#!/usr/bin/python

str1 = raw_input(" enter the srting : ")
word_freq = {}
from collections import Counter


#Print the top three nfrequent words
print ("top 3 frequent words:")
lis = sorted(Counter(str1.split()).items(),key=lambda (i,j):(-j,i))[:3]
for word,freq in lis:
    print word, freq


#The permutation of each word
    def perms(s):       
            if(len(s)==1): return [s]
            result=[]
            for i,v in enumerate(s):
                result += [v+p for p in perms(s[:i]+s[i+1:])]
            return result


    print('\n'.join(perms(word)))
