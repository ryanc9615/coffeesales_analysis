import kagglehub as kg

# Download the latest version of the dataset
coffee_sales = kg.dataset_download("ihelon/coffee-sales")

# Show dataset
print("Path to dataset files:", coffee_sales)