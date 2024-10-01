for _ in range(int(input())):
   a,b = map(int,input().split())
   L = list(map(int,input().split()))
   if L == sorted(L):
      print('YES')
      continue
   elif b == 1 and L == sorted(L):
      print('YES')
   elif b>1:
      print('YES')
   else:
      print('NO')