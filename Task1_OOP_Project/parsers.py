import csv
import pypdf
from models import Trade

class StatementParser:
    """
    Base parser class to demonstrate Inheritance and Polymorphism.
    """
    def __init__(self, filepath: str):
        self.filepath = filepath

    def process(self):
        """Abstract method to be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement process()")

class CSVParser(StatementParser):
    def process(self):
        trades = []
        with open(self.filepath, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader) # Skip header
            for row in reader:
                # Assuming format: TICKER, BUY/SELL, PRICE, QUANTITY, DATE
                try:
                    trade = Trade(row[0], row[1], float(row[2]), int(row[3]), row[4])
                    trades.append(trade)
                except Exception as e:
                    pass # Ignore malformed rows
        return trades

class PDFParser(StatementParser):
    def __init__(self, filepath: str, password: str = None):
        super().__init__(filepath)
        self.__password = password # Encapsulate password

    def process(self):
        trades = []
        reader = pypdf.PdfReader(self.filepath)
        
        # Handle password encrypted files!
        if reader.is_encrypted:
            if self.__password:
                try:
                    reader.decrypt(self.__password)
                except Exception as e:
                    print("Failed to decrypt: Incorrect password.")
                    return trades
            else:
                print(f"Error: The file {self.filepath} is password protected. Please provide a password.")
                return trades

        text = ""
        for page in reader.pages:
            text += page.extract_text()
            
        # Simplified logic: mock extracting trades from text.
        # In a real scenario, regular expressions would be used here.
        # We will create one dummy trade as proof of concept if text is found.
        if "BUY" in text.upper() or "SELL" in text.upper():
            trades.append(Trade("SAMPLE", "BUY", 150.0, 10, "2026-01-01"))
            
        return trades
