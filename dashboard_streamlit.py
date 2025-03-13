# -*- coding: utf-8 -*-
"""dashboard_streamlit.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/github/suhaodatascichem/dashboard-streamlit/blob/main/dashboard_streamlit.ipynb
"""

pip install streamlit

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
# Replace 'your_data.csv' with your actual data file
url = 'https://github.com/suhaodatascichem/dashboard-streamlit/raw/refs/heads/main/Soybean%20meal.xlsx'
data = pd.read_excel(url, engine="openpyxl")

# Streamlit app title
st.title('Interactive Data Visualization Dashboard')

# Sidebar for selecting features
st.sidebar.header('Select Features')

# Select columns for the x-axis and y-axis for scatter plots
x_axis = st.sidebar.selectbox('Select X-axis:', data.columns)
y_axis = st.sidebar.selectbox('Select Y-axis:', data.columns)

# Select a categorical column for bar charts
categorical_column = st.sidebar.selectbox('Select Categorical Column for Bar Chart:', data.select_dtypes(include=['object']).columns)

# Show the selected data
st.subheader('Data Preview')
st.write(data.head())

# Scatter plot
st.subheader('Scatter Plot')
fig, ax = plt.subplots()
sns.scatterplot(data=data, x=x_axis, y=y_axis, ax=ax)
st.pyplot(fig)

# Bar chart
st.subheader('Bar Chart')
fig, ax = plt.subplots()
sns.countplot(data=data, x=categorical_column, ax=ax)
st.pyplot(fig)

# Optional: Add more charts or features as needed
# For example, a histogram of a selected numerical column
numerical_column = st.sidebar.selectbox('Select Numerical Column for Histogram:', data.select_dtypes(include=['number']).columns)

st.subheader('Histogram')
fig, ax = plt.subplots()
sns.histplot(data[numerical_column], bins=30, kde=True, ax=ax)
st.pyplot(fig)

# Run the Streamlit app
if __name__ == '__main__':
    st.write("Use the sidebar to select features and visualize the data.")