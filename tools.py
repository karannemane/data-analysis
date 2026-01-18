import pandas as pd

def preview_csv(file_path: str) -> str:
    df = pd.read_csv(file_path)
    return df.head().to_string()

def summary_csv(file_path: str) -> str:
    df = pd.read_csv(file_path)
    return df.describe().to_string()

def missing_csv(file_path: str) -> str:
    df = pd.read_csv(file_path)
    return df.isnull().sum().to_string()
