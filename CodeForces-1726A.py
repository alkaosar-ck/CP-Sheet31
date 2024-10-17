for _ in range(int(input())):
   i = int(input())
   L = list(map(int,input().split()))
   if i == 1:
      print(0)
      continue
   mi = min(L)
   if L.index(mi) == 0:
      mx = max(L)
      print(mx-mi)
      continue
   mx = max(L)
   if L.index(mx) == i-1:
      print(mx-mi)
      continue
   f = L[0]
   fmx = max(L[1:])
   l = L[-1]
   lmi = min(L[:-1])
   maximu = (max((fmx-f),(l-lmi)))
   just_max = 0
   for x in range(i-1):
      maximu = max(maximu,L[x]-L[x+1])
   print(maximu)
   