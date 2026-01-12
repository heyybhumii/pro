import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("sales_data.csv")

data["Total_Sales"] = data["Quantity"] * data["Price"]

print("Total Sales:", np.sum(data["Total_Sales"]))

sales_by_product = data.groupby("Product")["Total_Sales"].sum()
print(sales_by_product)

plt.figure()
sales_by_product.plot(kind="bar")
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.show()

sales_by_date = data.groupby("Date")["Total_Sales"].sum()

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