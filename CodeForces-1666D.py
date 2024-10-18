for _ in range(int(input())):
   main,find = map(str,input().split())
   main = list(main)
   from collections import Counter
   c  =Counter(main)
   fc = Counter(find)
   for x in set(main):
      if c[x]>fc[x]:
         for _ in range(c[x]-fc[x]):
            main.remove(x)
   start = 0
   current = find[start]
   possible = True
   for x in find:
      if x not in main:
         possible = False
         break
   if possible:
      main = [x for x in main if x in find]
   else:
      print('NO')
      continue
   j = ''.join(main)
   if j == find:
      print('YES')
   else:
      print('NO')
      