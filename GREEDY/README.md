🧠 GREEDY Problems

---

✅ **Problem: Baekjoon 11047 - Coin 0**  
- **Category:** Greedy  
- **Link:** [Baekjoon 11047](https://www.acmicpc.net/problem/11047)

🔑 **Key Concepts**  
- Use the largest denomination coins first  
- Integer division and modulo operations  
- Input optimization with `sys.stdin.readline()`

⚠️ **What I Got Stuck On**  
- Initially used `/` instead of `//`, resulting in a float  
- Understood that greedy works when larger coins are multiples of smaller ones  

---

✅ **Problem: Baekjoon 11399 - ATM**  
- **Category:** Greedy, Sorting  
- **Link:** [Baekjoon 11399](https://www.acmicpc.net/problem/11399)

🔑 **Key Concepts**  
- Sort waiting times in ascending order  
- Use cumulative sum (prefix sum) to minimize total time

⚠️ **What I Got Stuck On**  
- Misunderstood input format (multiple values on one line)  
- Learned how total cost decreases with earlier smaller values

---

✅ **Problem: Baekjoon 1931 - Meeting Room Assignment**  
- **Category:** Greedy, Sorting  
- **Link:** [Baekjoon 1931](https://www.acmicpc.net/problem/1931)

🔑 **Key Concepts**  
- Sort meetings by end time first, then start time  
- Select meetings where `start >= last_end`

⚠️ **What I Got Stuck On**  
- Forgot to use `.split()` when reading 2D input with `sys.stdin.readline()`  
- Learned how to use `lambda` for custom tuple-based sorting
