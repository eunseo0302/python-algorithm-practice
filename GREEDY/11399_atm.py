import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

ans = 0
cnt = 0
for i in range(n):
    cnt += arr[i]
    ans += cnt
    
print(ans)
