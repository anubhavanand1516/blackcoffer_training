import pandas as pd

# Load the Excel file
df = pd.read_excel("Sales.xlsx")

# Compute key financial metrics
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_cost_of_sales = df["Cost of Sales"].sum()

# Identify top-performing countries by profit
top_countries = df.groupby("Country")["Profit"].sum().nlargest(5)

# Identify best-selling products by quantity sold
top_products = df.groupby("Product Name")["Order Qty"].sum().nlargest(5)

# Identify most profitable promotions
top_promotions = df.groupby("Promotion Name")["Profit"].sum().nlargest(5)

# Compute average unit cost and price
average_unit_cost = df["Unit Cost"].mean()
average_price = df["Price"].mean()

# Store computed insights in a dictionary
computed_insights = {
    "Total Sales": total_sales,
    "Total Profit": total_profit,
    "Total Cost of Sales": total_cost_of_sales,
    "Average Unit Cost": average_unit_cost,
    "Average Price": average_price,
    "Top Countries by Profit": top_countries.to_dict(),
    "Top Selling Products": top_products.to_dict(),
    "Most Profitable Promotions": top_promotions.to_dict(),
}

# Display computed insights
for key, value in computed_insights.items():
    print(f"{key}: {value}")
