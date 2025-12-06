import sys, os
import pandas as pd
from tqdm import tqdm

sys.path.append(os.path.dirname(__file__))

from io_utils import read_expenses, save_results
from classifier import classify_expense   


def run_expense_categorizer(input_file: str, output_file: str):
    # 1. Load input file
    df = read_expenses(input_file)
    print(f"Loaded {len(df)} expenses from {input_file}.\n")

    # Validate required columns
    required_columns = ["Merchant", "Purpose"]
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Input file must contain a '{col}' column.")

    print("Classifying expenses...\n")

    # 2. Loop through each expense with progress bar
    for idx, row in tqdm(df.iterrows(), total=len(df), desc="Processing", unit="row"):
        merchant = row.get("Merchant", "") or ""
        purpose = row.get("Purpose", "") or ""

        result = classify_expense(merchant, purpose)

        df.at[idx, "Predicted Category Code"] = result["category_code"]
        df.at[idx, "Predicted Category Name"] = result["category_name"]
        df.at[idx, "Category Confidence"] = result["confidence"]
        df.at[idx, "Final Result"] = result["final_result"]
        df.at[idx, "Reason"] = result["reason"]

    # 3. Save final output
    save_results(df, output_file)
    print(f"\nCategorized expenses saved to: {output_file}\n")

    #4. Auto open the file
    print("Opening the output file...")
    try:
        if os.name == 'win32':  # For Windows
            os.startfile(output_file)
        elif os.name == 'posix':  # For macOS and Linux
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            os.system(f"{opener} {output_file}")
    except Exception as e:
        print(f"Could not open file automatically: {e}")


if __name__ == "__main__":
    input_file = "data/expenses_input.xlsx"
    output_file = "output/expenses_categorized.xlsx"

    run_expense_categorizer(input_file, output_file)

    print("Expense categorization completed.\n")

    delete = input("Do you want to delete the output file? (yes/no): ")

    if delete.lower() == "yes":
        os.remove(output_file)
        print("File deleted securely.")
    else:
        print("File retained.")
