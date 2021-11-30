#Generate a list of four digit numbers in a given range with all their digits even and the
#number is a perfect square.
import math

start,limit = int(input("4 digit number start:")),int(input("4 digit number limit:"))
even = [2,4,6,8,0]
count = 0
newlist = []
for i in range(start,limit+1,1):
    num = start
    numstring = str(num)
    for x in numstring:
        if x in even:
            count =count+1
    if count == 4:
        sr = math.sqrt(i)
        if (sr*sr) == float(i):
            newlist.append(i)
    count = 0

print("list is",newlist)
    
