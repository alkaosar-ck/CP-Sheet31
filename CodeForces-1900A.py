for _ in range(int(input())):
   i = int(input())
   L = input().strip()
   long = 0
   total = 0
   if '...' in L:
      print(2)
   else:
      for x in range(len(L)):
         if L[x] == '.':
            long +=1
         else:
            if long>0:
               total+=long
            long = 0
      if long>0:
         total+=long
      print(total)