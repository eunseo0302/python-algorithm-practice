import sys

height = [int(sys.stdin.readline()) for _ in range(9)]

for i in range(9):
    for j in range(i + 1, 9):
        count = 0
        ans = []
        for k in range(9):
            if k != i and k != j:
                count += height[k]
                ans.append(height[k])
        if count == 100:
            ans.sort()
            print(*ans)
            sys.exit()
