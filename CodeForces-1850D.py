for _ in range(int(input())):
   n, k = map(int, input().split())
   L = sorted(list(map(int, input().split())))
   total = 1
   current = 1 
   f = L[0] 
   for x in L[1:]: 
      if x - f <= k:
         current += 1
         total = max(total, current)
      else:
         current = 1 
      f = x  
   print(n-total)
