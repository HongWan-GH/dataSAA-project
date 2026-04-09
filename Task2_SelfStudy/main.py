import random
from quick_sort import quick_sort
from max_heap import MaxHeap

class StatementDemo:
    def __init__(self, target, date):
        self.target = target
        self.date = date
        self.realized_pnl = round(random.uniform(-5000, 15000), 2)
        self.unrealized_pnl = round(random.uniform(-2000, 10000), 2)
        self.total_pnl = round(self.realized_pnl + self.unrealized_pnl, 2)
        
        # MaxHeap internally looks for a 'profit' attribute because of the implementation in Task 1
        self.profit = self.total_pnl

    def __str__(self):
        return f"[{self.date}] {self.target} | Realized PNL: {self.realized_pnl} | Unrealized PNL: {self.unrealized_pnl} | Total PNL: {self.total_pnl}"

def main():
    print("=" * 60)
    print("TASK 2 DEMONSTRATION: Quick Sort and Max Heap")
    print("=" * 60)
    
    # Generate mock objects once globally for the session
    targets = ["AAPL", "TSLA", "MSFT", "NVDA", "GOOGL", "AMZN"]
    dates = ["2024-01-31", "2024-02-28", "2024-03-31", "2024-04-30", "2024-05-31", "2024-06-30"]

    raw_data = []
    # Make dates un-ordered initially
    random.shuffle(dates)
    for d in dates:
        for t in random.sample(targets, k=3):
            raw_data.append(StatementDemo(t, d))

    while True:
        print("\n" + "-" * 40)
        print("Please select an option:")
        print("1. Show all raw data")
        print("2. Apply Quick Sort & Max Heap")
        print("3. Exit")
        print("-" * 40)
        
        choice = input("Enter your choice (1/2/3): ").strip()
        
        if choice == '1':
            print(f"\n[Raw Data] Total Records Generated: {len(raw_data)}")
            for r in raw_data:
                print("  -", r)
                
        elif choice == '2':
            # Create a copy so we can run it multiple times if we want
            data_to_sort = raw_data.copy()
            
            # Demonstrate Quick Sort (Sorting chronologically)
            print("\n[Operations] Testing Quick Sort (O(N log N))...")
            quick_sort(data_to_sort, 0, len(data_to_sort) - 1)
            
            print("\nChronologically Sorted (All records):")
            for r in data_to_sort:
                print("  -", r)

            # Demonstrate Max Heap
            print("\n[Operations] Testing Max Heap (O(log N) extraction)...")
            print("Building Priority Queue to find top absolute maximum profits...")
            
            heap = MaxHeap()
            for record in raw_data:
                heap.insert(record)
                
            print(f"Heap Size Built: {len(heap.heap)}")
            
            print("\nExtracting TOP 3 Most Profitable Trades:")
            for i in range(1, 4):
                if len(heap.heap) > 0:
                    top = heap.extract_max()
                    print(f"  Rank {i}: {top}")
                    
        elif choice == '3':
            print("Exiting Task 2 Demonstration. Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
