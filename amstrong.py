"""def amstrong(num):
    duplicate = num
    summ = 0
    while(num>0):
        d=num%10
        summ = summ+(d*d*d)
        num = num//10
    if summ == duplicate:
        return summ
    else:
        return False

n = int(input("enter the number to find the amstrong"))
value = amstrong(n)

if value == False:
    print("not an amstrong")
else :
    print("amstrong ;)")
    """

def amstrong(num):
    duplicate = num
    summ = 0
    while(num>0):
        d=num%10
        summ = summ+(d*d*d)
        num = num//10
    if summ == duplicate:
        print(" amstrong")
    else:
        print(" not an amstrong")

n = int(input("enter the number to find the amstrong"))
amstrong(n)
