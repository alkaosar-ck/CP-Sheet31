for _ in range(int(input())):
   i = int(input())
   L = list(map(int,input().split()))
   new = []
   target = i+1
   new = [target-x for x in L]
   print(*new)