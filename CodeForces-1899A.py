for _ in range(int(input())):
   i = int(input())
   if i == 1 or i == 2:
      print('First')
      continue
   else:
      if i%3 == 0:
         print('Second')
      else:
         print('First')
      