# Sales Analysis of Artisan Sandwiches

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Display text summary
st.title('Sales Insights')
st.write('''A total of 27 artisan sandwiches were sold, generating a revenue of $385.00. The average price per sandwich is $14.26, suggesting a potential pricing strategy adjustment to maximize profits. Further analysis of sales trends, customer preferences, and ingredient costs can provide more detailed insights.''')

# Sample sales data (replace with actual data from receipts)
data = {'Sandwich Type': ['Artisan Chicken', 'Artisan Veggie', 'Artisan Turkey', 'Artisan Chicken', 'Artisan Veggie', 'Artisan Turkey', 'Artisan Chicken', 'Artisan Veggie', 'Artisan Turkey', 'Artisan Chicken', 'Artisan Veggie', 'Artisan Turkey', 'Artisan Chicken', 'Artisan Veggie', 'Artisan Turkey', 'Artisan Chicken', 'Artisan Veggie', 'Artisan Turkey', 'Artisan Chicken', 'Artisan Veggie', 'Artisan Turkey', 'Artisan Chicken', 'Artisan Veggie', 'Artisan Turkey', 'Artisan Chicken', 'Artisan Veggie', 'Artisan Turkey'],
        'Quantity': [1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 1, 1],
        'Price': [15.50, 14.00, 16.00, 15.50, 14.00, 16.00, 15.50, 14.00, 16.00, 15.50, 14.00, 16.00, 15.50, 14.00, 16.00, 15.50, 14.00, 16.00, 15.50, 14.00, 16.00, 15.50, 14.00, 16.00, 12.50, 13.00, 12.50]}

df = pd.DataFrame(data)

# Calculate total sales and average price
total_sales = df['Price'].sum()
average_price = total_sales / df['Quantity'].sum()

# Display key metrics
st.write(f'**Total Artisan Sandwiches Sold:** {df["Quantity"].sum()}')
st.write(f'**Total Revenue from Artisan Sandwiches:** ${total_sales:.2f}')
st.write(f'**Average Price per Artisan Sandwich:** ${average_price:.2f}')

# Create and display bar chart of sales by sandwich type
sales_by_type = df.groupby('Sandwich Type')['Quantity'].sum().reset_index()
fig, ax = plt.subplots()
ax.bar(sales_by_type['Sandwich Type'], sales_by_type['Quantity'])
ax.set_xlabel('Sandwich Type')
ax.set_ylabel('Quantity Sold')
ax.set_title('Sales by Sandwich Type')
st.pyplot(fig)

# Create and display pie chart of sales distribution by sandwich type
fig1, ax1 = plt.subplots()
ax1.pie(sales_by_type['Quantity'], labels=sales_by_type['Sandwich Type'], autopct='%1.1f%%')
ax1.set_title('Sales Distribution by Sandwich Type')
st.pyplot(fig1)

