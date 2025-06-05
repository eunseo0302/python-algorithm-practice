import sys

n, k = map(int, sys.stdin.readline().split())
coins = [int(input()) for _ in range(n)]

cnt = 0

for i in range(n):
    if k == 0: break
    else:
        cnt += k // coins[n - i - 1]
        k %= coins[n - i - 1]

print(cnt)
