import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
payment_df = pd.read_csv('Data/payment.csv')
customer_df = pd.read_csv('Data/customer.csv')

# Title
st.title("🎬 Movie Rental Analytics Dashboard")

# Total revenue
total_revenue = payment_df['amount'].sum()
st.metric("💰 Total Revenue", f"${total_revenue:,.2f}")

# Revenue by month
payment_df['payment_date'] = pd.to_datetime(payment_df['payment_date'])
payment_df['month'] = payment_df['payment_date'].dt.to_period('M').astype(str)

monthly_revenue = payment_df.groupby('month')['amount'].sum().reset_index()
fig = px.bar(monthly_revenue, x='month', y='amount', title='Monthly Revenue')
st.plotly_chart(fig)

# Add more pages, filters, or visuals...
