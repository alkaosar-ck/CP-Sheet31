for _ in range(int(input())):
   i = int(input())
   L = list(map(int,input().split()))
   if L[0] == 1:
      print('YES')
   elif L[0]>L[1]:
      print('NO')
   else:
      print('NO')