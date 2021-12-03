#Generate a list of four digit numbers in a given range with all their digits even and the
#number is a perfect square.
import math

start,limit = int(input("4 digit number start:")),int(input("4 digit number limit:"))

main = []
count = 0
for i in range(start,limit,1):
      sr = math.sqrt(i)
      if int(sr+0.5)**2 == i:
          num = i
          while(num>0):
              d=num%10
              if d%2 == 0:
                  count = count+1
              num = num//10
          if count == 4:
              main.append(i)
      count = 0     
        
          

print("list with even perfect squarea are",main)
              
              
                  
    

