import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "Date": [
        "2025-01-01", "2025-01-01",
        "2025-01-02", "2025-01-02",
        "2025-01-03", "2025-01-03",
        "2025-01-04", "2025-01-04"
    ],
    "Product": [
        "Pen", "Notebook",
        "Pen", "Eraser",
        "Notebook", "Pen",
        "Eraser", "Notebook"
    ],
    "Quantity": [10, 5, 20, 15, 8, 12, 20, 6],
    "Price": [5, 40, 5, 3, 40, 5, 3, 40]
}

df = pd.DataFrame(data)

df.to_csv("sales_data.csv", index=False)

df["Total_Sales"] = df["Quantity"] * df["Price"]

print("Total Sales:", np.sum(df["Total_Sales"]))

sales_by_product = df.groupby("Product")["Total_Sales"].sum()
print(sales_by_product)

plt.figure()
sales_by_product.plot(kind="bar")
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.show()

sales_by_date = df.groupby("Date")["Total_Sales"].sum()

plt.figure()
plt.plot(sales_by_date.index, sales_by_date.values)
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.show()

plt.figure()
sales_by_product.plot(kind="pie", autopct='%1.1f%%')
plt.title("Product Contribution")
plt.ylabel("")
plt.show()
