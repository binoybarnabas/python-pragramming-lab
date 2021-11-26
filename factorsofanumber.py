#factors of a number

num= int(input("enter the number"))
print("factors of the number are")
for i in range(1,num+1,1):
    if(num%i == 0):
        print(i)
    
