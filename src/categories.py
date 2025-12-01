import pandas as pd
from typing import Dict
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config import CATEGORIES_FILE, CONFIDENCE_THRESHOLD

def load_categories() -> Dict[str, str]:
    """
    Load the category list from the Excel file and return a disctionary in this format:
    {'50000':'Cost of Goods Sold, ...}
    """

    df = pd.read_excel(CATEGORIES_FILE)

    df.columns = [col.strip().lower() for col in df.columns]
    
    code_col = None
    category_col = None

    for col in df.columns:
        if "code" in col:
            code_col = col
        if col == "category":
            category_col = col

    if not code_col or not category_col:
        raise ValueError("Could not find 'Category Code' or 'Category' columns in Excel file.")
    
    # emove blanks and zeros
    df = df[df[code_col].notna() & (df[code_col] != 0)]

    # Build dictionary
    categories = {
        str(row[code_col]).strip(): str(row[category_col]).strip()
        for _, row in df.iterrows()
    }

    return categories

def build_category_list_string(categories: Dict[str, str]) -> str:
    """
    Convert dictionary into text like:
    '50000: Cost of Goods Sold'
    """
    return "\n".join([f"{code}: {name}" for code, name in categories.items()])

if __name__ == "__main__":
    cats = load_categories()
    print(f"Loaded {len(cats)} categories.\n")

    # Show sample of first 10 categories
    print("Here are the first 10:")
    for i, (code, name) in enumerate(cats.items()):
        if i == 10:
            break
        print(f"{code} → {name}")