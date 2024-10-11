for _ in range(int(input())):
    i = int(input())
    L = list(map(int, input().split()))
    two = L.count(2)
    one = i - two
    if two % 2 == 0:
        m = two // 2
        if m != 0:
            track = 0
            for idx, x in enumerate(L):
                if x == 2:
                    track += 1
                    if track == m:
                        print(idx + 1) 
                        break
        elif m == 0:
            print(1)
    else:
        print(-1)
