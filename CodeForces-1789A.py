import math
def can_be_beautiful(n, arr):
    for i in range(n):
       for j in range(i+1,n):
          if math.gcd(arr[i],arr[j])<=2:
             return True
    return False

t = int(input())
for _ in range(t):
    n = int(input())
    array = sorted(list(map(int, input().split())))
    if can_be_beautiful(n, array):
        print("Yes")
    else:
        print("No")
