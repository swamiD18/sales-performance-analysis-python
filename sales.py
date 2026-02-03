import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams["figure.figsize"] = (10,5)
sns.set_style("whitegrid")

df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")
df.head()

df.info()
df.describe()
df.isnull().sum()

# Convert date columns
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# Create new columns
df["Order Month"] = df["Order Date"].dt.month
df["Order Year"] = df["Order Date"].dt.year
df["Order YearMonth"] = df["Order Date"].dt.to_period("M")

df.head()

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()

print("Total Sales:", total_sales)
print("Total Profit:", total_profit)

category_sales = df.groupby("Category")["Sales"].sum().reset_index()

sns.barplot(x="Category", y="Sales", data=category_sales)
plt.title("Sales by Category")
plt.show()

monthly_sales = df.groupby("Order YearMonth")["Sales"].sum().reset_index()
monthly_sales["Order YearMonth"] = monthly_sales["Order YearMonth"].astype(str)

plt.plot(monthly_sales["Order YearMonth"], monthly_sales["Sales"])
plt.xticks(rotation=90)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

top_products.plot(kind="barh")
plt.title("Top 10 Products by Sales")
plt.show()

region_sales = df.groupby("Region")[["Sales", "Profit"]].sum().reset_index()

sns.barplot(x="Region", y="Sales", data=region_sales)
plt.title("Sales by Region")
plt.show()

sns.scatterplot(x="Discount", y="Profit", data=df)
plt.title("Discount vs Profit")
plt.show()

df.to_csv("Cleaned_Superstore_Data.csv", index=False)
