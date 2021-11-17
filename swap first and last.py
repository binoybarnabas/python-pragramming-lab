string = input("enter the string")

lengthstring = len(string)

first = string[0]
last = string[lengthstring-1]

middle = string[1:lengthstring-1]

lastmerge = last+middle+first

print(lastmerge)



