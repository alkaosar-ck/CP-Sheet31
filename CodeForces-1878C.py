for _ in range(int(input())):
    n,k,x = map(int,input().split())
    total = (n*(n+1))//2
    min_sum = (k*(k+1))//2
    max_sum = total-(((n-k)*(n-k+1))//2)
    if x>= min_sum and x<=max_sum:
       print('YES')
    else:
      print('NO')
    
    