dx = [-1, 1, -1, 1]
dy = [-1, -1, 1, 1]

def knight_fork(a,b, x1, y1, x2, y2):
    results = 0
    for i in range(1):
        st1, st2 = set(), set()
        for j in range(4):
            st1.add((x1 + dx[j] * a, y1 + dy[j] * b))
            st1.add((x1 + dx[j] * b, y1 + dy[j] * a))
        for j in range(4):
            st2.add((x2 + dx[j] * a, y2 + dy[j] * b))
            st2.add((x2 + dx[j] * b, y2 + dy[j] * a))
        results = len(st1.intersection(st2))
    return results

for _ in range(int(input())):
   a,b = map(int,input().split())
   x1,y1 = map(int,input().split())
   x2,y2 = map(int,input().split())
   results = knight_fork(a,b,x1,y1,x2,y2)
   print(results)