import os
from models import StockPosition
from parsers import CSVParser, PDFParser
from max_heap import MaxHeap
from quick_sort import quick_sort

def process_file(filepath, password=None):
    """Helper function to parse individual files"""
    if filepath.endswith('.csv'):
        return CSVParser(filepath).process()
    elif filepath.endswith('.pdf'):
        return PDFParser(filepath, password).process()
    return []

def main():
    while True:
        print("\n" + "="*70)
        print("Welcome to the Ultimate Stock Profit Calculator (OOP & Data Structures)")
        print("="*70)
        print("\n--- MAIN MENU ---")
        print("[1] Run Demo: Process 12 sample monthly CSV statements (Auto)")
        print("[2] Custom Input: Enter a specific file or folder path manually")
        print("[3] Exit")
        
        choice = input("\nPlease select an option (1/2/3): ").strip()
        
        if choice == '2':
            path = input("\nEnter a file path OR a folder path: ").strip()
        elif choice == '3':
            print("Exiting... Goodbye!")
            return
        elif choice == '1':
            path = os.path.join(os.path.dirname(__file__), "monthly_statements")
            print("\n--> Auto-loading the 'monthly_statements' sample folder...")
        else:
            print("Invalid option, please try again.")
            continue
            
        trades = []
        # Check if user entered a folder (Directory)
        if os.path.isdir(path):
            if choice == '2': 
                password = input("If PDFs are encrypted, enter the universal password (or press Enter to skip): ").strip()
            else:
                password = "" # Skip password prompt for auto-demo
            password = password if password else None
            print(f"\nScanning folder: {path} ...")
            # Loop through all 12 monthly PDFs
            for filename in sorted(os.listdir(path)):
                filepath = os.path.join(path, filename)
                if os.path.isfile(filepath) and (filepath.endswith('.pdf') or filepath.endswith('.csv')):
                    print(f"Processing {filename}...")
                    trades.extend(process_file(filepath, password))
        # Check if user entered a single file
        elif os.path.isfile(path):
            password = None
            if path.endswith('.pdf'):
                password = input("Is this PDF password protected? Enter password or press Enter to skip: ").strip()
            trades.extend(process_file(path, password if password else None))
        else:
            print("Invalid path or file does not exist!")
            continue

        if not trades:
            print("No valid trades found or file could not be parsed.")
            continue

        # Task 2: Algorithm - Sort Trades by date using QuickSort
        quick_sort(trades, 0, len(trades) - 1)
        print(f"\nSuccessfully loaded and sorted {len(trades)} trades across all files.")

        # Task 1: Calculate Position
        positions = {}
        for trade in trades:
            if trade.ticker not in positions:
                positions[trade.ticker] = StockPosition(trade.ticker)
            positions[trade.ticker].add_trade(trade)

        # Task 2: Data Structure - Use MaxHeap to get Top Profitable Stocks
        heap = MaxHeap()
        for pos in positions.values():
            if pos.profit > 0:
                heap.insert(pos)

        print("\n--- TOP PROFITABLE STOCKS ---")
        top_stocks = heap.get_top_n(5)
        if top_stocks:
            for i, stock in enumerate(top_stocks, 1):
                print(f"{i}. {stock}")
        else:
            print("No profitable stocks found.")

if __name__ == "__main__":
    main()
