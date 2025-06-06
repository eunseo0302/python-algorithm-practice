import sys

n = int(sys.stdin.readline())
board = [list(sys.stdin.readline().strip()) for _ in range(n)]

def swap1(i, j):
    if j + 1 < n:
        a = board[i][j]
        board[i][j] = board[i][j + 1]
        board[i][j + 1] = a

def swap2(i, j):
    if i + 1 < n:
        a = board[i][j]
        board[i][j] = board[i + 1][j]
        board[i + 1][j] = a

def check_max_candies():
    max_count = 1
    for i in range(n):
        count = 1
        for j in range(n - 1):
            if board[i][j] == board[i][j + 1]:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1
    for j in range(n):
        count = 1
        for i in range(n - 1):
            if board[i][j] == board[i + 1][j]:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1
    return max_count

ans = 0
for i in range(n):
    for j in range(n):
        swap1(i, j)
        ans = max(ans, check_max_candies())
        swap1(i, j)
        swap2(i, j)
        ans = max(ans, check_max_candies())
        swap2(i, j)

print(ans)
