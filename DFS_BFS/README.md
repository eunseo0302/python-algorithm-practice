# 🧠 DFS / BFS Problems

---

## ✅ Problem: Baekjoon 11724 - Number of Connected Components
- **Category**: Graph, DFS
- **Link**: [Baekjoon 11724](https://www.acmicpc.net/problem/11724)

### 🧠 Key Concepts
- Use adjacency list for undirected graph
- Track visited nodes using `visited[]`
- Run DFS on every unvisited node to count connected components

### ⚠️ What I Got Stuck On
- ❌ Mistakenly wrote `visited(i)` instead of `visited[i]` due to C++ habit
- ❌ Forgot to increase the component count in the correct place
- ✅ Learned that DFS must be run for all nodes in disconnected graphs

---

## ✅ Problem: Baekjoon 1260 - DFS and BFS
- **Category**: Graph, DFS/BFS
- **Link**: [Baekjoon 1260](https://www.acmicpc.net/problem/1260)

### 🧠 Key Concepts
- Compare traversal order of DFS (recursive) and BFS (queue-based)
- Ensure nodes are visited in ascending order
- Use `deque` for efficient BFS

### ⚠️ What I Got Stuck On
- ❌ Used `visited(i)` again instead of `visited[i]` (syntax issue)
- ❌ Didn't separate DFS and BFS traversal orders correctly at first
- ✅ After correcting, clearly understood the difference in search order

---

## ✅ Problem: Baekjoon 2606 - Virus
- **Category**: Graph, BFS
- **Link**: [Baekjoon 2606](https://www.acmicpc.net/problem/2606)

### 🧠 Key Concepts
- Start BFS from node 1
- Count all reachable nodes except the start
- BFS traversal to explore one connected component

### ⚠️ What I Got Stuck On
- ❌ Forgot to declare `cnt` as global when used outside function
- ✅ Changed to a local `cnt` and returned the count — cleaner and safer

---

## ✅ Problem: Baekjoon 1012 - Organic Cabbage
- **Category**: 2D Grid, BFS
- **Link**: [Baekjoon 1012](https://www.acmicpc.net/problem/1012)

### 🧠 Key Concepts
- Count connected components in a 2D grid using BFS
- Use `arr[y][x]` for proper coordinate access
- Handle multiple test cases

### ⚠️ What I Got Stuck On
- ❌ Mistaken coordinate access: used `arr[a][b]` instead of `arr[b][a]`
- ✅ Fixed by correctly mapping input (x, y) → grid[y][x]

---

## ✅ Problem: Baekjoon 4963 - Number of Islands
- **Category**: 2D Grid, BFS with 8 directions
- **Link**: [Baekjoon 4963](https://www.acmicpc.net/problem/4963)

### 🧠 Key Concepts
- 8-directional grid traversal using `dx` and `dy` vectors
- Infinite input loop with `while True:` and break on `0 0`
- Mark all connected land cells (1s)

### ⚠️ What I Got Stuck On
- ❌ Missed `int` conversion in `map(int, input().split())` → caused TypeError
- ❌ Initially misunderstood line-by-line input format
- ✅ Corrected input and handled all 8 directions properly
