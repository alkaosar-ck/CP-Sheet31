for _ in range(int(input())):
   i = int(input())
   l = list(map(int,input().split()))
   start = 0
   current = 0
   total = 0
   while start<len(l)-1:
      first = l[start]
      second = l[start+1]
      if first%2== second%2:
         l[start] = first
         l.pop(start+1)
         start = max(0,start)
         total+=1
      else:
         start+=1
   print(total)