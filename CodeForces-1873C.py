one_side = [
    [1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2],
    [1, 2, 3, 3, 3],
    [1, 2, 3, 4, 4],
    [1, 2, 3, 4, 5]
]
matrix = [[0 for _ in range(10)] for _ in range(10)]
for x in range(5):
    for i in range(5):
        matrix[x][i] = one_side[x][i]    
        matrix[x][9 - i] = one_side[x][i]  
        matrix[9 - x][i] = one_side[x][i] 
        matrix[9 - x][9 - i] = one_side[x][i]


t = int(input())
for _ in range(t):
    store = []
    grid = [input().strip() for _ in range(10)]
    for i,x in enumerate(grid):
       for j,y in enumerate(x):
          if y == 'X':
            store.append([i,j])
    total = 0
    for x in store:
       r,c = x
       total+=matrix[r][c]
    print(total)
    
