string = input("enter the string")
s = string.find('o')
#print(s)

string1 = string[:s+1]
#print(string1)

string2 = string[s+1:]
#print(string2)

string3 = string2.replace('o','$')

newstring = string1+string3

print(newstring)





