string = input("enter the string")

index = int(input("enter the index from which the character should be removed"))

string1 = string[:index]
print(string1)
string2 = string[index+1:]
print(string2)
stringnew = string1+string2

print(stringnew)
