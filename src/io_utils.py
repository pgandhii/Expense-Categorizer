import pandas as pd
import os

def read_expenses(file_path: str) -> pd.DataFrame:
    """
    Reads a CSV or Excel file containing expenses.
    Returns a pandas DataFrame.
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    ext = file_path.lower().split(".")[-1]

    if ext == "csv":
        df = pd.read_csv(file_path)
    elif ext in ["xls", "xlsx"]:
        df = pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format. Please provide a CSV or Excel file.")
    
    print(f"Loaded {len(df)} expenses from {file_path}")
    return df

def save_results(df: pd.DataFrame, output_path: str) -> None:
    """
    Saves the categorized DataFrame to CSV or Excel depending on the file extension.
    """

    # Create folder if missing
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    ext = output_path.lower().split(".")[-1]

    if ext == "csv":
        df.to_csv(output_path, index=False)
    elif ext in ["xlsx", "xls"]:
        df.to_excel(output_path, index=False)
    else:
        raise ValueError("Unsupported file type. Use .csv or .xlsx")

    print(f"Results saved to {output_path}")
