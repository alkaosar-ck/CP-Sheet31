for _ in range(int(input())):
   i = int(input())
   L = list(map(int,input().split()))
   if all(x == 0 for x in L):
      print(0)
      continue
   possible = True
   for x in range(1,i-1):
      if L[x-1] >0 and L[x] == 0 and any(x>0 for x in L[x+1:]):
         possible = False
         break
   if possible :
      print(1)
   else:
      print(2)