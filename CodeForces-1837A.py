for _ in range(int(input())):
   x,k = map(int,input().split())
   x = abs(x)
   valid = [x for x in range(1,x+1) if x%k !=0]
   if x in valid:
      print(1)
      print(x)
   else:
      print(2)
      print(valid[-1],1)
      