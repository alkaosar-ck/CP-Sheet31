for _ in range(int(input())):
   a,b,c = map(int,input().split())
   if c%2 == 0:
      if b>=a:
         print('Second')
      else:
         print('First')
   else:
      a+=1
      if b>=a:
         print('Second')
      else:
         print('First')