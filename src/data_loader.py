import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / 'data'))

import coffee_sales
import pandas as pd
import os

def get_coffee_sales_df():
    """Get the coffee sales dataframe."""
    dataset_path = coffee_sales.coffee_sales
    
    # Find CSV files in the dataset
    csv_files = [f for f in os.listdir(dataset_path) if f.endswith('.csv')]
    if csv_files:
        file_path = os.path.join(dataset_path, csv_files[0])
        return pd.read_csv(file_path)
    return None