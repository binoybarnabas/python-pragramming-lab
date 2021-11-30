#Store a list of first names. Count the occurrences of ‘a’ within the list.


firstname = []
count = 0
n = int(input("enter the number of first name to be inserted"))

print("enter the first names")

for i in range(0,n):
    val = input()
    firstname.append(val)

for i in firstname:
    for j in i:
        if j == 'a':
            count+=1

print("number of a in the string is ",count)
