for _ in range(int(input())):
   i = int(input())
   L = list(map(int,input().split()))
   if L!=sorted(L):
      print(0)
      continue
   new = [L[x]-L[x-1] for x in range(1,i)]
   m = min(new)
   if m%2 == 0:
      print(m//2+1)
   else:
      print(m//2+1)