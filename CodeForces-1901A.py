for _ in range(int(input())):
   n , x = map(int,input().split())
   L = list(map(int,input().split()))
   if L:
      M = max(L)
   else:
      M = L[0]
   if min(L) == 0 or max(L) == x:
      print(M)
      continue
   d = []
   d.append(L[0])
   for i in range(0,n-1):
      d.append(L[i+1]-L[i])
   if d:
      m = max(d)
   else:
      m = L[0]
   print(max(m,(x-M)*2))