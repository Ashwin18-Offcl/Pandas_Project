# Importing Pandas
import pandas as pd

# Step 1: Creating Dataset
data = {
    "OrderID": [101, 102, 103, 104, 105, 106],
    "Product": ["Laptop", "Mouse", "Keyboard", "Laptop", "Monitor", "Mouse"],
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics", "Electronics", "Accessories"],
    "Quantity": [1, 2, 1, 1, 1, 3],
    "Price": [75000, 500, 1500, 76000, 12000, 500],
    "City": ["Pune", "Mumbai", "Pune", "Delhi", "Delhi", "Mumbai"]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Step 2: Calculate Total Sales for Each Order
df["Total"] = df["Quantity"] * df["Price"]
print("\nDataFrame with Total Column:")
print(df)

# Step 3: Summary Statistics
print("\nSummary Statistics:")
print(df.describe())

# Step 4: Total Sales by City
sales_city = df.groupby("City")["Total"].sum()
print("\nTotal Sales by City:")
print(sales_city)

# Step 5: Count Products by Category
category_count = df["Category"].value_counts()
print("\nProduct Count by Category:")
print(category_count)

# Step 6: Filter Orders with Total > 2000
high_sales = df[df["Total"] > 2000]
print("\nOrders with Total > 2000:")
print(high_sales)

# Step 7: Sorting by Total Sales (Descending Order)
sorted_df = df.sort_values(by="Total", ascending=False)
print("\nSorted Data by Total Sales (Descending):")
print(sorted_df)

# Step 8: Export the sorted data to CSV (Optional)
sorted_df.to_csv("Sorted_Sales_Report.csv", index=False)
print("\nCSV Export Done: Sorted_Sales_Report.csv Created Successfully.")
