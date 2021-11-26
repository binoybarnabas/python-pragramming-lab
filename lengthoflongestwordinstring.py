#Accept a list of words and return length of longest word.

string = input("enter the string where each word is separated with comma")

p = string.split(",")

length = len(p)
#print(length)
max = len(p[0])
for i in range(0,length):
    if max<len(p[i]):
        max = len(p[i])
        index = i
        
print("longest word",p[index],"with length",max)
     
    
