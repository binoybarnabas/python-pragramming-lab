string = input("enter the string")

lengthstring = len(string)

first = string[0:]
second = string[1]
secondlast = string[lengthstring-2]
last = string[lengthstring-1]

middle = string[2:lengthstring-2]

lastmerge = last+middle+first 

print(lastmerge)
