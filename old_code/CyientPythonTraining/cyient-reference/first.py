import sys 
s = sys.argv[1]
#print count of each character 
#Take each char(ch) from s
d = {}
for ch in s:
    #initialize counter 
    counter = 0
    #Take each char(ch1) from s
    for ch1 in s:
        #if ch and ch1 are same 
        if ch == ch1:
            #increment counter 
            counter = counter + 1
    d[ch] = counter 
    print(ch, counter) 
############################################
s = "Hello World"
#create a empty dict 
d = {}
#Take each char(ch) from s
for ch in s:
    if ch not in d:
    #if does not exist
        #create ch as key and initialize to 1 
        d[ch] = 1
    else :
        #increment ch 's value 
        d[ch] = d[ch]+1
print(d) 
    
##############################################
#[]  list - Indexing-A, Duplicates-A, IO - A, Mutable
#()      tuple - Immutable, -----above-----
#      
#{}  set - Indexing - NA, Duplicates - NA, IO-NA, Mutable
#      frozenset - Immutable , -----above---
#----------------
#dict - key and associated value, key is like set 












l = [1,2,3,4]
res = [1,4,9,16]

Create empty list 
Take each element from input list
    if that element is odd
        append to empty list 









