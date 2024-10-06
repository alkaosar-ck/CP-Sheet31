from collections import Counter
def can_be_good(arr):
    n = len(arr)
    if n == 2:
        return "Yes"
    count = Counter(arr)
    if len(count) > 2:
        return "No"
    if len(count) == 1:
        return "Yes"
    keys = list(count.keys())
    if abs(count[keys[0]] - count[keys[1]]) > 1:
        return "No"
    return "Yes"
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(can_be_good(arr))
