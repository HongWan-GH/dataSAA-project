# Hong Kong Metropolitan University
# COMP8090SEF Data Structures and Algorithms
## Course Project Report - Task 2

**Submission date:** April 12, 2026
**NAME:** [Your Name Here]
**SID:** [Your SID Here]

**(Please insert the official compulsory declaration statement here on the actual PDF cover page)**

---

## 1. Introduction
For Task 2, I decided to learn and implement two things that were not covered in our lectures: a **Max-Heap** (which is a type of Priority Queue) and the **Quick Sort** algorithm. 

Why did I choose these? In Task 1, my program has to read potentially thousands of lines of stock trades from different statement files. If I just used a basic $O(N^2)$ algorithm like Bubble Sort to order them, it would be extremely slow. By self-studying Quick Sort, I could bring that down to $O(N \log N)$. Furthermore, after calculating the profits, I wanted an efficient way to output just the "Top Profitable Stocks" without having to sort the entire final list again. That's where the Max-Heap comes in handy.

## 2. Advanced Data Structure: Max-Heap (Priority Queue)
### 2.1 How it works
A Max-Heap acts like a Priority Queue. It works by treating a standard array like a complete binary tree. The main rule of a Max-Heap is that the parent node must always have a higher or equal value compared to its children. Because of this rule, the very first element (the root) is absolutely always the maximum value in the entire structure.

**The methods I built:**
*   `insert(value)`: When I add a new item, it goes to the end of the array. Then, I wrote a `heapify_up` function to make it "climb" the tree until it finds its proper place. This only takes $O(\log N)$ time.
*   `extract_max()`: This method pops off the root (the highest value). It then takes the last element, moves it to the root, and uses a `heapify_down` function to let it sink back to its correct level. This also runs in $O(\log N)$.

### 2.2 How I used it in the project
In `max_heap.py`, I used the Max-Heap to track the `profit` attribute of each stock position. When the user wants to see the top 5 most profitable stocks, I don't need to do a full expensive sort. I just throw all the positions into the heap, and call `extract_max()` 5 times. It's much faster ($O(N + K \log N)$ instead of $O(N \log N)$) when dealing with large datasets.

## 3. Advanced Algorithm: Quick Sort
### 3.1 How it works
Quick Sort is a "divide-and-conquer" sorting method. Here is how I implemented it in `quick_sort.py`:
1.  **Pivot Selection:** I choose an element (usually the last one in the target range) to act as the "pivot".
2.  **Partitioning:** I loop through the array. If an element is smaller than the pivot, it gets swapped to the left side. If it's larger, it stays on the right. 
3.  **Recursion:** Now the pivot is in its exact final sorted position. I then recursively call Quick Sort on the left chunk and the right chunk.

### 3.2 Time and Space Complexity
*   **Average Time Complexity ($O(N \log N)$):** If the pivot roughly halves the array each time, the depth of the recursive tree is $\log N$, and scanning each level takes $N$ operations.
*   **Worst Time Complexity ($O(N^2)$):** This happens if the array is already sorted (because the pivot doesn't divide the work evenly).
*   **Space Complexity ($O(\log N)$):** Since it sorts the items *in-place* by swapping them directly in the array, it barely needs any extra memory besides the recursive call stack.

### 3.3 How I used it in the project
When pulling transactions from multiple files, the dates are completely mixed up. Before I can calculate average costs and profits correctly, the trades absolutely have to be in chronological order. My `quick_sort.py` takes the unsorted lists of trades and rapidly orders them by their parsed Date objects so the financial math logic in Task 1 works perfectly.

## 4. User Guide & GitHub
1. Please execute `python3 main.py` using Python 3 via the console.
2. The interactive script parses and sorts multiple statements executing Quick Sort under the hood. Subsequently, Max-Heap triggers implicitly for calculating and publishing the "Top Profitable Stocks" dynamically.

## Links & References
*   **GitHub Repository:** [Insert your GitHub Link Here]
*   **5-Minute Intro Video:** [Insert your Video Link Here]
*   **Generative AI:** Large Language Models were consulted for reviewing ADT concepts securely and optimizing basic Markdown report structures.

---
## Appendix
*(Place your time complexity analysis charts, program screenshots, code demonstrations, and structural logs here)*