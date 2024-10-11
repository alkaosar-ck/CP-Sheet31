for _ in range(int(input())):
   i = int(input())
   L = list(map(int,input().split()))
   minus = L.count(-1)
   plus = i-minus
   total = 0
   import math
   target = math.ceil(i/2)
   if plus<=target:
      total = target-plus
      minus = minus-total
      if minus%2 == 0:
         print(total)
      else:
         print(total+1)
   else:
      if minus%2 == 0:
         print(0)
      else:
         print(1)
   
      
      




      