import sys

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

arr.sort(key=lambda x: (x[1], x[0]))

last_end = 0
count = 0

for start, end in arr:
    if start >= last_end:
        count += 1
        last_end = end

print(count)
