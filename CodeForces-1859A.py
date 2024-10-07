t = int(input()) 
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split())) 
    a.sort()
    if a[0] == a[-1]:
        print(-1)
    else:
        max_element = a[-1]
        b = [x for x in a if x == max_element]
        c = [x for x in a if x != max_element]
        print(len(c), len(b))
        print(*c)
        print(*b)
