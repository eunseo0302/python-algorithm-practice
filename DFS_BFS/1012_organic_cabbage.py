from collections import deque
import sys

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    visited[y][x] = True
    q = deque()
    q.append((x, y))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not visited[ny][nx] and arr[ny][nx] == 1:
                    visited[ny][nx] = True
                    q.append((nx, ny))

t = int(sys.stdin.readline())
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())

    arr = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    
    for _ in range(k):
        a, b = map(int, sys.stdin.readline().split())
        arr[b][a] = 1
    
    ans = 0
    for y in range(n):
        for x in range(m):
            if arr[y][x] == 1 and not visited[y][x]:
                bfs(x, y)
                ans += 1
    print(ans)
