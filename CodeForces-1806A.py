for _ in range(int(input())):
   x1,y1,x2,y2 = map(int,input().split())
   if (y1<=y2) and x2<=(x1+y2-y1):
      print(y2-y1+x1+y2-x2-y1)
   else:
      print(-1)
