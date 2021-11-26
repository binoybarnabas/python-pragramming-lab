finalyear = int(input("enter the final year:"))

print("leap year are")
for i in range(2021,finalyear+1,1):
    if i%4 == 0:
        print(i)
