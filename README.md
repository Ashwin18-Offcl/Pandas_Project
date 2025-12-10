````md
# 📊 Pandas Simple Project – Sales Data Analysis

A beginner–friendly mini project to learn **Pandas** step by step using a small **Sales Dataset**.  
In this project you will:

- Create a `DataFrame` from Python dictionaries  
- Add calculated columns  
- Explore summary statistics  
- Group and aggregate data  
- Filter and sort data  
- Export results to CSV  

---

## 🖼 Thumbnail (Optional)

If you use the project on GitHub / YouTube, add a thumbnail like:

```md
<p align="center">
  <img src="assets/pandas-simple-project-thumbnail.png" alt="Pandas Simple Project Thumbnail" width="80%">
</p>
````

(Replace the path with your actual image location.)

---

## 1️⃣ Project Overview

We analyze a tiny **sales table** that contains:

* Order ID
* Product & Category
* Quantity
* Price
* City

Using Pandas, we will find:

* Total amount for each order
* Total sales by city
* Product count by category
* Orders with high total value
* Sorted sales report

---

## 2️⃣ Technologies Used

* **Language:** Python 3.x
* **Library:** `pandas`
* **Optional:** `Jupyter Notebook` / `VS Code` / `Google Colab`

---

## 3️⃣ Dataset Description

We will manually create a small in-memory dataset:

| Column   | Type   | Description                        |
| -------- | ------ | ---------------------------------- |
| OrderID  | int    | Unique order number                |
| Product  | string | Item name (Laptop, Mouse, etc.)    |
| Category | string | Product category                   |
| Quantity | int    | Number of units sold in that order |
| Price    | int    | Price per unit                     |
| City     | string | City where order was placed        |

---

## 4️⃣ How to Set Up the Project

### Step 4.1 – Create Project Folder

```text
Pandas-Simple-Project/
│
├── sales_analysis.py      # or use a Jupyter notebook
└── README.md
```

### Step 4.2 – Install Pandas

```bash
pip install pandas
```

If you use Jupyter:

```bash
pip install notebook
jupyter notebook
```

---

## 5️⃣ Full Project Code (Step by Step)

Copy–paste this complete script into `sales_analysis.py`
(or into one Jupyter Notebook cell):

```python
# ------------------------------------------
# 1. Import Library
# ------------------------------------------
import pandas as pd

# ------------------------------------------
# 2. Create the Dataset
# ------------------------------------------
data = {
    "OrderID": [101, 102, 103, 104, 105, 106],
    "Product": ["Laptop", "Mouse", "Keyboard", "Laptop", "Monitor", "Mouse"],
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics", "Electronics", "Accessories"],
    "Quantity": [1, 2, 1, 1, 1, 3],
    "Price": [75000, 500, 1500, 76000, 12000, 500],
    "City": ["Pune", "Mumbai", "Pune", "Delhi", "Delhi", "Mumbai"]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)
print("🔹 Original DataFrame:")
print(df)

# ------------------------------------------
# 3. Add Total Column (Quantity * Price)
# ------------------------------------------
df["Total"] = df["Quantity"] * df["Price"]
print("\n🔹 DataFrame with Total Column:")
print(df)

# ------------------------------------------
# 4. Summary Statistics
# ------------------------------------------
print("\n🔹 Summary Statistics for Numeric Columns:")
print(df.describe())

# ------------------------------------------
# 5. Total Sales by City
# ------------------------------------------
sales_city = df.groupby("City")["Total"].sum()
print("\n🔹 Total Sales by City:")
print(sales_city)

# ------------------------------------------
# 6. Product Count by Category
# ------------------------------------------
category_count = df["Category"].value_counts()
print("\n🔹 Product Count by Category:")
print(category_count)

# ------------------------------------------
# 7. Filter Orders with Total > 2000
# ------------------------------------------
high_sales = df[df["Total"] > 2000]
print("\n🔹 Orders with Total > 2000:")
print(high_sales)

# ------------------------------------------
# 8. Sort Data by Total (Descending)
# ------------------------------------------
sorted_df = df.sort_values(by="Total", ascending=False)
print("\n🔹 Sorted Data by Total (Descending):")
print(sorted_df)

# ------------------------------------------
# 9. Export Sorted Data to CSV
# ------------------------------------------
sorted_df.to_csv("Sorted_Sales_Report.csv", index=False)
print("\n✅ CSV Export Done: 'Sorted_Sales_Report.csv' created successfully.")
```

---

## 6️⃣ Explanation – What Each Step Teaches

1. **Create DataFrame**

   * Understand how to convert a Python `dict` into a Pandas `DataFrame`.

2. **Add Calculated Column (`Total`)**

   * Learn vectorized operations: `df["Quantity"] * df["Price"]`.

3. **`describe()` Summary**

   * Quickly see count, mean, min, max, quartiles for numeric columns.

4. **Group by City**

   * `groupby("City")["Total"].sum()` shows which city generates more revenue.

5. **Value Counts by Category**

   * `value_counts()` tells you which product category appears more.

6. **Filtering Rows**

   * `df[df["Total"] > 2000]` gives only high-value orders.

7. **Sorting Data**

   * `sort_values(by="Total", ascending=False)` ranks orders by revenue.

8. **Export to CSV**

   * Generates a file `Sorted_Sales_Report.csv` for sharing / reporting.

---

## 7️⃣ How to Run the Project

### Option A – Run as Python Script

```bash
python sales_analysis.py
```

You will see:

* Original table
* Table with `Total` column
* Summary statistics
* Grouped and filtered results
* Confirmation message about CSV export

### Option B – Run in Jupyter Notebook

1. Open Jupyter Notebook
2. Create a new notebook
3. Copy the code in different cells (step by step)
4. Run each cell and observe the outputs interactively

---

## 8️⃣ Possible Extensions (Next Level)

You can extend this simple project with:

* Add `Date` column and analyze **monthly sales**
* Add a `Discount` column and compute `Net_Total`
* Use `matplotlib` or `seaborn` to plot:

  * Bar chart: City vs Total Sales
  * Pie chart: Category share
* Read data from a real **CSV file** instead of hard-coding the dictionary

---

## 9️⃣ Learning Outcomes

After completing this project, you will be comfortable with:

* Creating and inspecting DataFrames
* Adding new calculated columns
* Using `groupby`, aggregations, and `value_counts()`
* Filtering and sorting data
* Exporting data to CSV for reporting

---

If you want, I can now:

* Add a **visualization section** with ready-to-use plotting code, or
* Convert this entire project into a **Jupyter Notebook template** for you.

```
```
