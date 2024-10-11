for _ in range(int(input())):
   i = int(input())
   L = list(map(int,input().split()))
   xor = 0
   for x in L:
      xor^=x 
   if i&1==0 :
      print(0 if xor == 0 else -1)
   else:
      print(xor)
