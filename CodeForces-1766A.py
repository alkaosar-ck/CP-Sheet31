for _ in range(int(input())):
   i = int(input())
   l = len(str(i))
   if l == 1:
      print(i)
   else:
      f = int(str(i)[0])
      total = 9*(l-1)+f
      print(total)
