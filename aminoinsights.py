# -*- coding: utf-8 -*-
"""aminoinsights.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/github/suhaodatascichem/dashboard-streamlit/blob/main/aminoinsights.ipynb
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load your dataset
# Replace 'your_data.csv' with your actual data file
url = 'https://github.com/suhaodatascichem/dashboard-streamlit/raw/refs/heads/main/Soybean%20meal.xlsx'
df = pd.read_excel(url, engine="openpyxl")

# App title
st.title("Customer Data Dashboard")

    # ---- Sidebar Filters ----
    st.sidebar.header("Filters")

    # Ensure "Date" column is in datetime format
    if "Release Date" in df.columns:
        df["Release Date"] = pd.to_datetime(df["Release Date"])

        # Date Range Filter
        min_date, max_date = df["Release Date"].min(), df["Release Date"].max()
        start_date, end_date = st.sidebar.date_input("Select Date Range", [min_date, max_date], min_value=min_date, max_value=max_date)

    # Customer Filter (Dropdown with Multi-selection)
    if "Customer" in df.columns:
        customers = df["Customer"].unique().tolist()
      # Add "Select All" option at the beginning
        all_customers_option = ["Select All"] + customers
      # Display multiselect with "Select All" option
        selected_customers = st.sidebar.multiselect("Select Customer(s)", all_customers_option, default=["Select All"])

    # If "Select All" is chosen, use all customers
    if "Select All" in selected_customers:
        selected_customers = customers  # Reset to all customers
        # Material Type Filter (Dropdown with Multi-selection)
        if "Material" in df.columns:
            material_types = df["Material"].unique()
            selected_materials = st.sidebar.multiselect("Select Material Type(s)", material_types, default=material_types)

        # ---- Apply Filters ----
        filtered_df = df.copy()
        if "Release Date" in df.columns:
            filtered_df = filtered_df[(filtered_df["Release Date"] >= pd.to_datetime(start_date)) & (filtered_df["Release Date"] <= pd.to_datetime(end_date))]
        if "Customer" in df.columns:
            filtered_df = filtered_df[filtered_df["Customer"].isin(selected_customers)]
        if "Material" in df.columns:
            filtered_df = filtered_df[filtered_df["Material"].isin(selected_materials)]

        # ---- Display Filtered Data ----
        st.write("### Filtered Data Preview")
        st.write(f"🔍 **Total Records After Filtering:** {filtered_df.shape[0]}")
        st.dataframe(filtered_df)


      # ---- Charts Section ----
        st.write("## 📊 Data Visualizations")

        # Predefined Charts
        if "Sales" in filtered_df.columns and "Date" in filtered_df.columns:
            fig1 = px.line(filtered_df, x="Date", y="Sales", title="📈 Sales Trend Over Time")
            st.plotly_chart(fig1)

        if "Customer" in filtered_df.columns and "Sales" in filtered_df.columns:
            fig2 = px.bar(filtered_df, x="Customer", y="Sales", title="🏢 Sales by Customer")
            st.plotly_chart(fig2)

        if "Material Type" in filtered_df.columns and "Sales" in filtered_df.columns:
            fig3 = px.bar(filtered_df, x="Material Type", y="Sales", title="📦 Sales by Material Type")
            st.plotly_chart(fig3)

        if "CP" in filtered_df.columns and "NH3" in filtered_df.columns:
            fig4 = px.scatter(filtered_df, x="CP", y="NH3", title="🔍 CP vs NH3")
            st.plotly_chart(fig4)

        if "Date" in filtered_df.columns and "Quantity" in filtered_df.columns:
            fig5 = px.line(filtered_df, x="Date", y="Quantity", title="📆 Quantity Trend Over Time")
            st.plotly_chart(fig5)

        if "Customer" in filtered_df.columns and "Quantity" in filtered_df.columns:
            fig6 = px.bar(filtered_df, x="Customer", y="Quantity", title="👥 Quantity by Customer")
            st.plotly_chart(fig6)

        # ---- Custom Chart Selection ----
        st.write("### 🛠 Create Your Own Chart")

        # Column selection for custom charts
        available_columns = list(filtered_df.select_dtypes(include=["number", "object"]).columns)
        x_axis = st.selectbox("Select X-Axis", available_columns)
        y_axis = st.selectbox("Select Y-Axis", available_columns)

        chart_type = st.radio("Select Chart Type", ["Scatter", "Bar"])

        # Generate custom chart
        if st.button("Generate Chart"):
            if chart_type == "Scatter":
                fig_custom = px.scatter(filtered_df, x=x_axis, y=y_axis, title=f"📊 {x_axis} vs {y_axis}")
            else:
                fig_custom = px.bar(filtered_df, x=x_axis, y=y_axis, title=f"📊 {x_axis} vs {y_axis}")
            st.plotly_chart(fig_custom)

