ni = int(input("enter your number to find the reverse"))

rev,d = 0,0

while(ni>0):
    d = ni%10
    rev = rev*10+d
    ni= ni//10

print("reverse of the number is",rev)
