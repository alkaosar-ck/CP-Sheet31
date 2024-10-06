for _ in range(int(input())):
   n,k = map(int,input().split())
   L = list(map(int,input().split()))
   if k in L:
      print('YES')
   else:
      print('NO')