# Retool Order Management Dashboard

## Overview
This Retool application is a customizable order management dashboard that displays customer orders, product details, order statuses, and shipping destinations. It allows users to interact with the data in real-time, filter results, and perform administrative actions efficiently.

## Features
- **Data Table**: Displays customer orders with product names, order statuses, and destination facilities.
- **Conditional Formatting**: Color-coded statuses for quick visualization (e.g., "Refunded" in green, "Shipping" in red, etc.).
- **Search & Filters**: Quickly find orders based on customer name, product, or order status.
- **Database/API Integration**: Fetch data dynamically from a PostgreSQL/MySQL database or REST API.
- **Export & Refresh**: Download data as CSV and refresh table content dynamically.

## Setup Instructions
1. **Sign Up on Retool**
   - Go to [Retool](https://retool.com/) and create an account.

2. **Create a New App**
   - Click on **Create New App** and name it "Order Management Dashboard."

3. **Connect to a Data Source**
   - Navigate to **Resources** → **Create a New Resource**.
   - Choose a database (PostgreSQL, MySQL) or connect to an API.
   - Enter connection credentials and test the connection.

4. **Add a Table Component**
   - Drag and drop the **Table** component onto the canvas.
   - Bind it to a database query or API endpoint.
   - Example SQL Query:
     ```sql
     SELECT id, customer_name, product, quantity, unit_price, order_date, order_status, destination_facility
     FROM orders;
     ```

5. **Implement Conditional Formatting**
   - Configure the **Order Status** column to show color-coded labels:
     - `Refunded` → Green
     - `Delivered` → Orange
     - `Shipping` → Red

6. **Add Search & Filtering**
   - Drag a **Search Bar** and bind it to the table filter.
   - Example JavaScript filter:
     ```js
     table1.filter({customer_name: {contains: searchInput.value}});
     ```

7. **Deploy & Share**
   - Click **Deploy** and adjust user permissions as needed.

## Customization
- Modify the SQL query to include additional order details.
- Add new filters (e.g., by date range or price).
- Integrate with third-party services like Stripe or Shopify.

## Troubleshooting
- **Data not loading?** Check API/database connection settings.
- **Conditional formatting not applying?** Ensure column mapping is correct.
- **Filters not working?** Debug using the Retool **Inspector** tool.

## Screenshots
<img width="1440" alt="Screenshot 2025-03-26 at 11 41 44 PM" src="https://github.com/user-attachments/assets/b3482379-0aed-4b67-80a5-811587928a3e" />

## For live demo
go to https://anandanubhav1516.retool.com/editor/6a886adc-0a65-11f0-ae11-b3f7d11ce3f2/new_poject/page1

