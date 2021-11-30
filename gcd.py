#gcd

def gcd(a,b):
    if a == 0 :
        return b
    if b==0:
        return a
    if a==b:
        return a
    if a>b :
        return gcd(a-b,b)
    return gcd(b-a,a)

a,b = int(input("enter the value of a")),int(input("enter the value of a"))
gcdval = gcd(a,b)
if gcdval:
    print("gcd(",a,",",b,")=",gcdval)
else
    print("not found")
