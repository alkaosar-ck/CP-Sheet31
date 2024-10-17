for _ in range(int(input())):
    n, q = map(int, input().split())
    L = list(map(int, input().split()))
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + L[i - 1]
    suffix_sum = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix_sum[i] = suffix_sum[i + 1] + L[i]
    
    for _ in range(q):
        l, r, k = map(int, input().split())
        sum_outside_range = prefix_sum[l - 1] + suffix_sum[r]
        sum_in_range = (r - l + 1) * k
        total_sum = sum_outside_range + sum_in_range
        if total_sum % 2 == 1:
            print("YES")
        else:
            print("NO")
