for _ in range(int(input())):
   i = int(input())
   s = input().strip()
   longest =1
   current = 1
   for x in range(1,i):
      if s[x]==s[x-1]:
         current+=1
         longest = max(longest,current)
      else:
         current = 1
   print(longest+1)
      