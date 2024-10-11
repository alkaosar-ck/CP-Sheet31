for _ in range(int(input())):
   l = int(input())
   i = input().strip()
   total = len(i)
   start,end = 0,len(i)-1
   for x in range(len(i)):
      if (i[start]=='0'and i[end]=='1') or (i[start]=='1'and i[end]=='0'):
         total-=2
         start+=1
         end-=1
      else:
         break
   if total<=0:
      print(0)
   else:
      print(total)