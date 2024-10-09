for _ in range(int(input())):
   i = int(input())
   L = list(map(int,input().split()))
   odds = [x for x in L if x%2 ==1]
   odds = len(odds)
   if odds%2 == 1:
      print('NO')
   else:
      print('YES')