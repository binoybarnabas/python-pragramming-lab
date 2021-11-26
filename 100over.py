limit = int(input("enter the limit"))
listt = []
for i in range(0,limit):
    val = int(input())
    if val>100:
        listt.append('over')
    else:
        listt.append(val)

print(listt)
    
