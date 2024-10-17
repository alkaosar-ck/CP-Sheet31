import math
for _ in range(int(input())):
   i = int(input())
   maximum = 1
   for x in range(1,i+1):
      if i%x != 0:
         break
      else:
         maximum = x
   print(maximum)