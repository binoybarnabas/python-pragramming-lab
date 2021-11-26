#nested loop pattern

num = int(input("enter the middle limit"))

for i in range(0,num,1):
    for j in range(0,i+1,1):
        print(" * ",end = " ")
    print()
    
for i in range(0,num-1,1):
    for j in  range(i,num-1,1):
        print(" * ",end=" ")
    print()
