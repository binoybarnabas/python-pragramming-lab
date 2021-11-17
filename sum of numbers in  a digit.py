num = int(input("enter the number"))

d = 0
summ = 0
number = num

while(number>0):
    d = number % 10
    #print("d is ",d)
    summ = summ + d
    #print("summ is ",summ)
    number = number//10
    #print("number is ",number)
    

print("sum is ",summ)



