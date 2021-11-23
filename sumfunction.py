
"""def sum(a,b):
    summ = a+b
    return summ

a,b = int(input("enter the first number")),int(input("enter the second number"))

s = sum(a,b)
print("sum =",s)


def student(name,age,subject):
    print("name of the student is ",name)
    print("age of the student is ",age)
    print("course of the student is ",subject)
    
student(age=18,subject="mca",name="binoy")

"""


def student(*arg):
    print("name of the student is ",arg[0])
    print("age of the student is ",age)
    print("course of the student is ",subject)
    
student(18,"mca","binoy")
