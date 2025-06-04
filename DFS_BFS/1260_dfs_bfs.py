from collections import deque
import sys

n, m, v = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)
    
for i in range(1, n + 1):
    adj[i].sort()

visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)

def dfs(x):
    visited_dfs[x] = True
    print(x, end=' ')
    
    for y in adj[x]:
        if not visited_dfs[y]:
            dfs(y)
    
def bfs(x):
    visited_bfs[x] = True
    q = deque([x])
    
    while q:
        curr = q.popleft()
        print(curr, end=' ')
        for y in adj[curr]:
            if not visited_bfs[y]:
                visited_bfs[y] = True
                q.append(y)
dfs(v)
print()
bfs(v)
