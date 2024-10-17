from collections import Counter

def solve():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        s = input().strip()
        freq = Counter(s)
        odd_count = sum(1 for count in freq.values() if count % 2 != 0)
        if odd_count <= k + 1:
            print("YES")
        else:
            print("NO")
solve()
