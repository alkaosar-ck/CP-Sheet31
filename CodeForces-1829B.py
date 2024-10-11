for _ in range(int(input())):
   i  = int(input())
   L = list(map(int,input().split()))
   m = 0
   current = 0
   for x in L:
      if x !=1:
         current+=1
         m = max(m,current)
      else:
         m = max(m,current)
         current = 0
   print(m)