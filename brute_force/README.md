# 🧠 BRUTE FORCE Problems

## ✅ Problem: Baekjoon 2309 - Seven Dwarfs  
- **Category**: Brute Force  
- **Link**: [Baekjoon 2309](https://www.acmicpc.net/problem/2309)

### 🔑 Key Concepts  
- Choose 7 out of 9 dwarfs whose total height is exactly 100  
- Use two nested loops to find and exclude the correct 2 dwarfs  
- Sort the remaining 7 heights before printing  

### ⚠️ What I Got Stuck On  
- Forgot to reset the list inside the loop, causing duplicate elements  
- Initially used `return` in global scope — fixed with `sys.exit()`  
- Understood that `combinations` from `itertools` could be used, but implemented manually to deepen brute-force logic understanding  

---

## ✅ Problem: Baekjoon 3085 - Candy Game  
- **Category**: Brute Force, Implementation  
- **Link**: [Baekjoon 3085](https://www.acmicpc.net/problem/3085)

### 🔑 Key Concepts  
- Try swapping adjacent candies (right and down only)  
- After each swap, scan the entire board for the maximum number of same candies in a row or column  
- Restore the original board after checking  

### ⚠️ What I Got Stuck On  
- Initially forgot to reset count inside the row/column checking loop  
- Mixed up row/column traversal order when checking vertical candies  
- Learned that early optimization (like only checking affected rows/columns) is optional for small board sizes  
- Realized that `check_max_candies()` should reset count when color changes
