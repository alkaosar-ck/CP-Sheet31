i = int(input())
L = list(map(int,input().split()))
L = [abs(x) for x in L]
print(min(L))