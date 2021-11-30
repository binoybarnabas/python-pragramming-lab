#print out colors from colorlist1 not contained in colorlist2

colorlist1 = []
colorlist2 = []

n1,n2 = int(input("length of list 1 ")),int(input("length of list 2 "))

print("enter first list")

for i in range(0,n1):
    colorlist1.append(input())

print("enter second list")

for i in range(0,n2):
    colorlist2.append(input())

for x in colorlist1:
    if x not in colorlist2:
        print(x)
