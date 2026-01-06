import pandas as pd
import matplotlib.pyplot as plt
import os


# Step 1: Load Data

try:
    df = pd.read_csv("sales_data.csv")
    print("Data loaded successfully")
except FileNotFoundError:
    print("Error: sales_data.csv not found in data folder")
    exit()


# Step 2: Data Cleaning

print("\nChecking missing values:")
print(df.isnull().sum())

# Remove rows with missing values (if any)
df.dropna(inplace=True)

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])


# Step 3: Data Analysis


# Total sales by product (for bar chart)
product_sales = df.groupby("Product")["Total_Sales"].sum()

# Total sales by date (for line chart)
daily_sales = df.groupby("Date")["Total_Sales"].sum()

print("\nProduct-wise Sales:")
print(product_sales)

print("\nDaily Sales Trend:")
print(daily_sales)

# Create visualizations folder if not exists
os.makedirs("visualizations", exist_ok=True)


# Step 4: Visualization


# Bar Chart - Sales by Product
plt.figure()
product_sales.plot(kind="bar")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("visualizations/product_sales_bar_chart.png")
plt.close()

# Line Chart - Daily Sales Trend
plt.figure(figsize=(10, 5))
plt.plot(daily_sales.index, daily_sales.values, marker='o')

plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)   
plt.tight_layout()        
plt.savefig("visualizations/daily_sales_line_chart.png")
plt.close()



# Step 5: Completion Message

print("\nAnalysis completed successfully.")
print("Charts saved in 'visualizations' folder.")
