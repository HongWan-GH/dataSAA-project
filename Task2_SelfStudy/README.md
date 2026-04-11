# Task 2: Advanced Data Structures & Algorithms applied to Real Scenarios

## 🎥 Introduction Video
> **Task 2 Video Link:** https://youtu.be/beEFB_INa9g

## Project Overview
This directory demonstrates the practical application of high-efficiency algorithms (Sorting and Prioritization) explored through independent self-study, extending beyond the standard COMP 8090 curriculum to tackle real-world temporal data processing.

### Concepts Applied:
- **Max Heap (Priority Queue)**: Extracts the top $k$ most profitable trades immediately in $O(k \log n)$ time, entirely avoiding the overhead of sorting the array ($O(n \log n)$) just to find a handful of maximum values.
- **Quick Sort**: Organizes an unstructured array of stock tracking dates strictly chronologically, efficiently achieving $O(n \log n)$ average runtime.

## 📖 User Guide
1. **Prerequisites**: Ensure Python 3.9+ is installed.
2. **Execution**: Run the main program via terminal:
   ```bash
   python main.py
   ```
3. **Interaction**: 
   - Choose **Option `1`** to view the dynamic raw dataset randomly generated upon launch (with randomized financial dates and PNL data records).
   - Choose **Option `2`** to observe the underlying algorithms: watching Quick Sort order the entries chronologically by date, and seeing the Max Heap instantly extract exactly the Top 3 most profitable trades automatically.
