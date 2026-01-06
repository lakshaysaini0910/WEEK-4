# E-commerce Sales Data Analysis

## Project Overview
This project performs an end-to-end data analysis on e-commerce sales data using Python. It covers data loading, cleaning, analysis, and visualization to extract meaningful insights from sales records.

## Project Objectives
- Implement a complete data analysis pipeline
- Analyze product-wise and date-wise sales performance
- Create professional visualizations using Matplotlib
- Derive meaningful insights from the data

## Dataset Description
The dataset used in this project is `sales_data.csv`, which contains e-commerce sales records.

Dataset columns:
- Date: Date of sale
- Product: Product name
- Quantity: Number of units sold
- Price: Price per unit
- Customer_ID: Unique customer identifier
- Region: Sales region
- Total_Sales: Total sales amount

## Tools and Technologies Used
- Python
- Pandas
- Matplotlib

## Visualizations Created
The following visualizations were created and saved in the `visualizations/` folder:
- Bar Chart: Total sales by product
- Line Chart: Daily sales trend

These visualizations help in comparing product performance and understanding sales trends over time.

## Key Insights
- Phones generate higher total sales compared to headphones.
- Daily sales fluctuate, indicating varying customer demand.
- Product-wise analysis highlights differences in customer purchasing behavior.

## How to Run the Project
1. Install required dependencies:
pip install -r requirements.txt
2. Run the analysis script:
python main.py

## Project Structure
The project follows the structure below:

project-folder/
├── main.py
├── README.md
├── requirements.txt
├── sales_data.csv
├── visualizations/
│   ├── daily_sales_line_chart.png
│   └── product_sales_bar_chart.png
└── report.md

Note: For simplicity, the dataset and report files are kept in the root directory. The project still follows a complete data analysis workflow and all required outputs are generated correctly.

## Conclusion
This project successfully demonstrates a complete data analysis workflow including data loading, cleaning, analysis, visualization, and documentation. It provides clear insights into sales performance and showcases practical data visualization skills.
