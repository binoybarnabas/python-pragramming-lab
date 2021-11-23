def listss(start,limit):
    a = []
    for i in range(start,limit+1,1):
        a.append(i**2)

    print("the squared list is:  ")

    for j in range(0,len(a)):
        print(a[j])
