# 🧠 DFS / BFS Problems

---

## ✅ Problem: Baekjoon 11724 - Number of Connected Components
- **Category**: Graph, DFS
- **Link**: [Baekjoon 11724](https://www.acmicpc.net/problem/11724)

### 🧠 Key Concepts
- Use adjacency list for undirected graph
- Track visited nodes with `visited[]`
- Run DFS for every unvisited node to count connected components

### ⚠️ What I got stuck on
- ❌ Mistakenly wrote `visited(i)` instead of `visited[i]` (syntax error)
- ❌ Initially forgot to increase component count correctly
- ✅ Understood that for disconnected graphs, DFS must run for all nodes

---

## ✅ Problem: Baekjoon 1260 - DFS and BFS
- **Category**: Graph, DFS/BFS
- **Link**: [Baekjoon 1260](https://www.acmicpc.net/problem/1260)

### 🧠 Key Concepts
- Compare traversal order of DFS (recursive) and BFS (queue)
- Ensure visiting nodes in ascending order
- Use `deque` for BFS implementation

### ⚠️ What I got stuck on
- ❌ Used `visited(i)` instead of `visited[i]` again (Python syntax habit from C++)
- ❌ BFS와 DFS 순서 출력을 구분하지 않음
- ✅ 익숙해진 이후에는 오히려 두 알고리즘의 차이를 명확히 이해함

---

## ✅ Problem: Baekjoon 2606 - Virus
- **Category**: Graph, BFS
- **Link**: [Baekjoon 2606](https://www.acmicpc.net/problem/2606)

### 🧠 Key Concepts
- Connected components from node 1
- Count all nodes visited except the starting node
- Simple graph traversal with BFS

### ⚠️ What I got stuck on
- ❌ `cnt` 변수를 함수 밖에서 쓸 때 `global` 선언을 잊어서 런타임 에러 발생
- ✅ 함수 내에서 `cnt`를 선언하고 반환하는 방식으로 깔끔하게 수정

---

## ✅ Problem: Baekjoon 1012 - Organic Cabbage
- **Category**: 2D BFS
- **Link**: [Baekjoon 1012](https://www.acmicpc.net/problem/1012)

### 🧠 Key Concepts
- Grid traversal using BFS
- Count connected components in 2D matrix
- Handle multiple test cases

### ⚠️ What I got stuck on
- ❌ 처음에 `arr[b][a]` 순서를 `arr[a][b]`로 잘못 입력해 틀림
- ✅ 문제 조건이 x, y 순서라는 것을 보고 배열 접근을 `arr[y][x]`로 고침

---

## ✅ Problem: Baekjoon 4963 - Number of Islands
- **Category**: 2D BFS (8 directions)
- **Link**: [Baekjoon 4963](https://www.acmicpc.net/problem/4963)

### 🧠 Key Concepts
- Use 8-directional BFS with dx, dy vectors
- Handle multiple maps with `while True:` and break on `0 0`
- Represent land with 1 and sea with 0

### ⚠️ What I got stuck on
- ❌ `map()`에 `int` 없이 `map(sys.stdin.readline().split())`만 써서 TypeError 발생
- ❌ 입력을 한 줄씩 받는 구조를 이해하는 데 시간이 조금 걸림
- ✅ 수정 후 완전히 입력 형식에 맞추고, 대각선 방향까지 정확히 탐색 완료

