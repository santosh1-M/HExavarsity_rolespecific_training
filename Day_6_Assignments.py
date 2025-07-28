import pandas as pd
# Task 1: Extract and Preview the Data
#     Q1. The Superstore sales team has shared a new CSV file. Load the dataset and give a preview of the top 5 records to validate its structure.
#     Load Superstore.csv into a DataFrame.
#     Check number of rows and columns.
#     Display column names and their data types.
store_data=pd.read_csv("Superstore.csv")
print(store_data)
print("Row",len(store_data),"columns:",store_data.columns.size)
print("Columns along with datatypes:",store_data.dtypes)

# Task 2: Clean Column Names and Normalize Dates
#     Q2. Some columns have inconsistent names with spaces and slashes. Also, the dates are strings. Clean the column names and convert Order Date and Ship Date to datetime format so that you can later group data by month.
#     Clean column headers using .str.replace().
#     Convert Order_Date and Ship_Date to datetime64.
store_data.columns=store_data.columns.str.strip().str.replace(r'[/]','_',regex=True)
print(store_data.columns)
store_data["Order Date"]=store_data["Order Date"].astype("datetime64[ns]")
store_data["Ship Date"]=store_data["Ship Date"].astype("datetime64[ns]")

# Task 3: Profitability by Region and Category
# Q3. The regional manager wants to know which region and category combinations are most profitable. 
# Summarize total Sales, Profit, and average Discount grouped by Region and Category.
#     Use groupby() + agg() to generate the report.
#     Identify which Region+Category had highest profit.
print(store_data.groupby(["Region","Category"]).agg(Total_sales=('Sales',"sum"),total_profit=('Profit','sum'),Average_discount=('Discount','mean')))
profit=store_data.sort_values(by="Profit",ascending=False)[["Category","Region"]].head(1)
print(profit)

# Task 4: Top 5 Most Profitable Products
# Q4. The product team is planning to promote high-profit items. Identify the top 5 products that contributed the most to overall profit.
#     Group by Product_Name, sum the profit, sort descending, and take top 5.
print(store_data["Product Name"])
print(store_data.groupby("Product Name").agg(Total_profit=('Profit','sum')).head(5))
total_profit=store_data.groupby("Product Name").agg(AGG_profit=("Profit",'sum'))
print(total_profit.sort_values(by="AGG_profit",ascending=False).head(5))

# Task 5: Monthly Sales Trend
# Q5. The leadership team wants to review monthly sales performance to understand seasonality. Prepare a month-wise sales trend report.
#     Extract month from Order_Date
#     Group by month and sum Sales
store_data["Order Date"]=store_data["Order Date"].astype("datetime64[ns]")
store_data["Month"]=store_data["Order Date"].dt.month
print(store_data.groupby('Month').agg(Total_sales=("Sales",'sum')))

# Task 6: Cities with Highest Average Order Value
# Q6. The business is interested in targeting high-value cities for marketing. Calculate the average order value (Sales ÷ Quantity) for each city and list the top 10.
#     Create a new column Order_Value
#     Group by City and calculate average order value
#     Sort and get top 10
store_data["Order Value"]=store_data["Sales"]/store_data["Quantity"]
print(store_data)
avg_value=store_data.groupby("City")["Order Value"].mean()
print(avg_value)
avg_value=avg_value.sort_values(ascending=False).head(10)
print(avg_value)

# Task 7: Identify and Save Orders with Loss
# Q7. Finance wants to analyze all loss-making orders. Filter all records where Profit < 0 and save it to a new file called loss_orders.csv.
#     Use boolean filtering
#     Export the filtered DataFrame to a CSV file without index
low_profit=store_data[store_data["Profit"]<0]
low_profit.to_csv("loss_Orders.csv",index=False)

# Task 8: Detect Null Values and Impute
# Q8. Are there any missing values in the dataset? If yes, identify columns with nulls and fill missing Price values with 1.
#     Use isnull().sum()
#     Apply fillna() only on Price column
store_data.isnull().sum()
store_data["Profit"].fillna(1,inplace=True)