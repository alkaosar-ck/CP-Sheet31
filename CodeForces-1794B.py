for _ in range(int(input())):
   n = int(input())
   L = list(map(int,input().split()))
   for x in range(n):
      L[x]+=1
   for x in range(n-1):
      if L[x+1]%L[x]==0:
         L[x+1] +=1
   print(*L)