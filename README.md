# Coffee Sales Analysis

A Python project for analyzing coffee sales data and generating insights.

## Setup Instructions

1. **Clone the repository** (if not already done):
   ```bash
   git clone <your-repo-url>
   cd coffeesales_analysis
   ```

2. **Create and activate virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Start Jupyter Notebook** (optional):
   ```bash
   jupyter notebook
   ```

## Project Structure

```
coffeesales_analysis/
├── data/               # Raw and processed data files including kagglehub connection
├── notebooks/          # Jupyter notebooks for analysis
├── src/               # Source code modules
├── results/           # Generated reports and visualizations
├── requirements.txt   # Python dependencies
└── README.md         # This file
```

## Usage

1. Create a python file in the data folder to import the dataset via Kagglehub API
2. Create a python file in the src folder that is a data_loader and loads this into a dataframe
