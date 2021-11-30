#Enter 2 lists of integers. Check (a) Whether list are of same length (b) whether list sums
#to same value (c) whether any value occur in both

list1 = []
list2 = []
similar = []
n1 = int(input("enter the number of elements to be inserted on list 1"))
n2 = int(input("enter the number of elements to be inserted on list 2"))

print("enter the first list elements")
for i in range(0,n1,1):
    val=int(input())
    list1.append(val)
    
print("enter the second list elements")
for i in range(0,n2,1):
    val=int(input())
    list2.append(val)

if len(list1) == len(list2):
    print("both list have same length of",len(list1))

sum1 = 0
sum2=0

for i in range(0,n1):
    sum1=sum1+list1[i]

for i in range(0,n2):
    sum2=sum2+list2[i]

if sum1 == sum2:
    print("sum of both elements in the list are same which is,",sum1)

for elements in list1:
        if elements in list2:
            similar.append(elements)
print("similar elements are:",similar)


    
