import sys 
s = sys.argv[1]
#b = sys.argv[2]
#c = int(a)
#d = int(b)
#print(int(a) + int(b))
##########################
#s = "Hello World"
#print count of each character 
#H - 1
#e - 1
#l - 3

#Take each char(ch) from s
for ch in s:
    #initialize counter 
    counter = 0
    #Take each char(ch1) from s
    for ch1 in s:
        #if ch and ch1 are same 
        if ch == ch1:
            #increment counter 
            counter = counter + 1
    print(ch, counter) 
