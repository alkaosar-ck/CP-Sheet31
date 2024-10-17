for _ in range(int(input())):
   i = int(input())
   L = list(map(int,input().split()))
   L = [abs(value - index+1) for value,index in enumerate(L)]
   import math
   gcd = math.gcd(L[0],L[1])
   for x in L[2:]:
      gcd = math.gcd(gcd,x)
   print(gcd)