from collections import deque
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

adj = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)

def bfs(x):
    visited[x] = True
    q = deque([x])
    cnt = 0
    
    while q:
        curr = q.popleft()
        cnt += 1
        for y in adj[curr]:
            if not visited[y]:
                visited[y] = True
                q.append(y)
    return cnt

print(bfs(1) - 1)
