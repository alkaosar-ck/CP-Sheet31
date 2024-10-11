for _ in range(int(input())):
   i = int(input())
   l = list(map(int,input().split()))
   if all(x == l[0] for x in l):
      print('NO')
      continue
   s = l
   re_s = s[::-1]
   le = len(l)
   new = []
   f = l[0]
   last = l[-1]
   new.append(f)
   new.append(last)
   for x in range(1,le-1):
      new.append(l[x])
   print('YES')
   print(*new)