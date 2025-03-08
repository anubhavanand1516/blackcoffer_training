# Sales Data Documentation

## 1. Dataset Overview

The dataset contains sales transaction records, including financial metrics, product details, and geographic information. It can be used for sales analysis, profitability tracking, and regional performance evaluation.

## 2. Loading Data

To load the dataset in Python:

```python
i
```

import pandas as pd



\# Load the Excel file

df = pd.read\_excel("Sales.xlsx")



\# Total Sales, Profit, and Cost of Sales

total\_sales = df["Sales"].sum()

total\_profit = df["Profit"].sum()

total\_cost\_of\_sales = df["Cost of Sales"].sum()



\# Top performing countries by profit

top\_countries = df.groupby("Country")["Profit"].sum().nlargest(5)



\# Best-selling products

top\_products = df.groupby("Product Name")["Order Qty"].sum().nlargest(5)



\# Most profitable promotions

top\_promotions = df.groupby("Promotion Name")["Profit"].sum().nlargest(5)



\# Compute average unit cost and price

average\_unit\_cost = df["Unit Cost"].mean()

average\_price = df["Price"].mean()



\# Prepare computed insights

computed\_insights = {

&#x20;   "Total Sales": total\_sales,

&#x20;   "Total Profit": total\_profit,

&#x20;   "Total Cost of Sales": total\_cost\_of\_sales,

&#x20;   "Average Unit Cost": average\_unit\_cost,

&#x20;   "Average Price": average\_price,

&#x20;   "Top Countries by Profit": top\_countries.to\_dict(),

&#x20;   "Top Selling Products": top\_products.to\_dict(),

&#x20;   "Most Profitable Promotions": top\_promotions.to\_dict(),

}



computed\_insights



To load the dataset into a SQL database:

```python
from sqlalchemy import create_engine

# Create a database connection (modify with your DB credentials)
engine = create_engine("sqlite:///sales_data.db")

df.to_sql("sales_data", con=engine, if_exists="replace", index=False)
```

## 3. Column Descriptions

### Order Details:

- **Order ID**: Unique identifier for each sales transaction.
- **Order Date**: The date when the order was placed.
- **Channel**: Sales channel used (e.g., Online, Retail).
- **Promotion Name**: Name of the promotion applied (if any).

### Financial Metrics:

- **Unit Cost**: Cost per unit of the product sold.
- **Price**: Selling price per unit.
- **Order Qty**: Number of units sold in the order.
- **Cost of Sales**: Total cost incurred for the order (Unit Cost \* Order Qty).
- **Sales**: Total revenue from the order (Price \* Order Qty).
- **Profit**: Profit earned from the order (Sales - Cost of Sales).

### Product Information:

- **Product Name**: Name of the product sold.
- **Manufacturer**: Company that manufactured the product.
- **Product Sub Category**: Sub-category under which the product falls.
- **Product Category**: Broad category of the product.

### Geographic Data:

- **Region**: Geographic region of the sale.
- **City**: City where the sale occurred.
- **Country**: Country where the sale occurred.

## 4. Data Computations & Insights

### Key Metrics:

- **Total Sales**: \$55.39M
- **Total Profit**: \$31.58M
- **Total Cost of Sales**: \$23.80M
- **Average Unit Cost**: \$124.43
- **Average Price**: \$296.51

### Top 5 Countries by Profit:

1. **United States**: \$18M
2. **China**: \$4.39M
3. **Germany**: \$2.47M
4. **France**: \$1.40M
5. **United Kingdom**: \$0.73M

### Top 5 Best-Selling Products:

1. Contoso In-Line Coupler E180 Silver - 6780 units
2. Headphone Adapter for Contoso Phone E130 Silver - 4680 units
3. Contoso Rubberized Snap-On Cover Hard Case Cell Phone Protector E160 Silver - 4580 units
4. Contoso In-Line Coupler E180 White - 4060 units
5. Contoso Rubberized Skin BlackBerry E100 Silver - 3560 units

### Most Profitable Promotions:

1. **No Discount**: \$10.60M
2. **North America Back-to-School Promotion**: \$4.80M
3. **North America Holiday Promotion**: \$3.57M
4. **North America Spring Promotion**: \$3.56M
5. **Asian Holiday Promotion**: \$2.08M

## 5. Data Usage & Analysis Guide

### Key Insights & Metrics:

- **Profitability Analysis**: Compute total profit by product, category, or region.
- **Sales Trends**: Analyze revenue trends over time.
- **Regional Performance**: Compare sales across different locations.
- **Promotion Effectiveness**: Assess how promotions impact sales and profitability.

### Sample Queries:

1. **Total Sales and Profit by Country**

   ```sql
   SELECT Country, SUM(Sales) AS Total_Sales, SUM(Profit) AS Total_Profit
   FROM sales_data
   GROUP BY Country
   ORDER BY Total_Profit DESC;
   ```

2. **Top 5 Best-Selling Products**

   ```sql
   SELECT Product_Name, SUM(Order_Qty) AS Total_Units_Sold
   FROM sales_data
   GROUP BY Product_Name
   ORDER BY Total_Units_Sold DESC
   LIMIT 5;
   ```

3. **Promotion Impact on Sales**

   ```sql
   SELECT Promotion_Name, SUM(Sales) AS Total_Sales, SUM(Profit) AS Total_Profit
   FROM sales_data
   GROUP BY Promotion_Name
   ORDER BY Total_Sales DESC;
   ```

## 6. Additional Notes

- Data can be used to build a **Sales Analytics Dashboard** in Google Looker Studio or Power BI.
- Ensure data consistency and handle missing values before performing deep analysis.
- Future improvements may include customer segmentation and demand forecasting.

---

*End of Documentation*

