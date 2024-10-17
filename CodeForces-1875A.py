def total(x, a, b, n):
    answer = b
    for i in range(len(x)):
       answer+= min(a-1,x[i])
    return answer
for _ in range(int(input())):
    a, b, n = map(int, input().split())
    x = list(map(int, input().split()))
    print(total(x, a, b, n))
