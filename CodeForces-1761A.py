def check(n,a,b):
   if (n == a == b) or (a+b+2<=n):
      return 'Yes'
   return 'No'
   
for _ in range(int(input())):
   n,a,b = map(int,input().split())
   print(check(n,a,b))