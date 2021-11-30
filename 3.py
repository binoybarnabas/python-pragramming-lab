#List comprehensions:
#(a) Generate positive list of numbers from a given list of integers
#(b) Square of N numbers
#(c) Form a list of vowels selected from a given word
#(d) List ordinal value of each element of a word (Hint: use ord() to get ordinal values)

list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
listeven = []
listsquare = []

for i in range(0,len(list1)):
    if list1[i]%2 == 0:
        listeven.append(list1[i])

print("even list are",listeven)

sqrlimit = int(input("enter the value of n"))
for i in range(1,sqrlimit+1,1):
    listsquare.append(i**2)
print("squared list is:",listsquare)

word = input("enter the word")
vowels = ['a','e','i','o','u']
listvowels = []
for i in word:
    if i in vowels:
        listvowels.append(i)

print("vowels in list are:",listvowels)

ordlis = []
ordword = input("enter the word")

orlist = list(ordword)

for i in range(0,len(orlist)):
    val = ord(orlist[i])
    ordlis.append(val)

print("ordinal values of elements are",ordlis )







