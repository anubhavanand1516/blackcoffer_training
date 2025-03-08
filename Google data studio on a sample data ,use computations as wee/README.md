# Sales Data Documentation

## 1. Dataset Overview

The dataset contains sales transaction records, including financial metrics, product details, and geographic information. It can be used for sales analysis, profitability tracking, and regional performance evaluation.

## 2. Loading Data

To load the dataset in Python:

<img width="352" alt="Screenshot 2025-03-08 at 10 31 34 AM" src="https://github.com/user-attachments/assets/e3664935-1e05-48b4-b4b0-790c76093c5d" />

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

## 5. **Sales Analytics Dashboard** using Google Looker Studio
live link->https://lookerstudio.google.com/reporting/27a8ced6-ecb7-4839-8493-5a01550c0c28



