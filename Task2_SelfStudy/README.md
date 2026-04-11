# Task 2: Advanced Data Structures & Algorithms applied to Real Scenarios

## 🎥 Introduction Video
> **Task 2 Video Link:** [INSERT YOUR 5-MINUTE YOUTUBE/GOOGLE DRIVE VIDEO LINK HERE]

## Project Overview
This directory demonstrates the practical application of high-efficiency algorithms (Sorting and Prioritization) explored through independent self-study, extending beyond the standard COMP 8090 curriculum to tackle real-world large-scale data matching.

### Concepts Applied:
- **Max Heap (Priority Queue)**: Extracts the top $k$ volatile stocks in $O(k \log n)$ time, directly simulating real-life stock prioritization logic.
- **Quick Sort**: Sorts the massive dataset natively in $O(n \log n)$ time, significantly faster than naïve sorts ($O(n^2)$) for determining overall market volatility.

## 📖 User Guide
1. **Prerequisites**: Ensure Python 3.9+ is installed.
2. **Dataset Setup**: The included `dataset/large_volatility_dataset.csv` contains 10,000+ rows of random, generated financial entries mimicking global markets.
3. **Execution**: Run the main program via terminal:
   ```bash
   python main.py
   ```
4. **Interaction**: 
   - Choose **Option `1`** to view the raw generated dataset preview.
   - Choose **Option `2`** to trigger the algorithmic comparisons, extracting the actual top 10 most volatile stocks using Heaps vs sorting natively.