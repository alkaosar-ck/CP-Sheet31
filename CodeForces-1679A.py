for _ in range(int(input())):
   i = input().strip()
   last = int(i[-1])
   last2 = int(i[-2:])
   digits_sum = sum(int(x) for x in i)
   if last%2 == 1 or int(i)<4:
      print(-1)
      continue
   max_buses = int(i)//4
   if digits_sum%3 == 0:
      min_bus = int(i)//6
   else:
      min_bus = int(i)//6 +1
   print(min_bus,max_buses)