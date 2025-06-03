from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
visited = [False] * (n + 1)
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)

def bfs(start):
    visited[start] = True
    q = deque([start])

    while q:
        curr = q.popleft()
        for next in adj[curr]:
            if not visited[next]:
                visited[next] = True
                q.append(next)

count = 0
for i in range(1, n + 1):
    if not visited[i]:
        bfs(i)
        count += 1

print(count)
