#fibbonacci

n = int(input("enter the fibonacci limit"))

first = 0
second = 1
print(first," ",second,end="")
for i in range(3,n+1,1):
    third = first+second
    print(" ",third,end="")
    first = second
    second = third
