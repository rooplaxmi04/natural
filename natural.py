import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set page config for Streamlit
st.set_page_config(page_title="Disaster Data Dashboard", page_icon="🌎", layout="wide")

# Load data
disaster = pd.read_csv("/content/1900_2021_DISASTERS.xlsx - emdat data.csv")

# Sidebar for additional options
st.sidebar.header("Dashboard Navigation")
st.sidebar.write("Use the navigation to explore different sections of the disaster data.")
st.sidebar.write("Icons used to make sections visually appealing.")

# Dashboard title and introduction
st.title("🌎 Disaster Data Dashboard")
st.write("""
Welcome to the Disaster Data Dashboard! This interactive dashboard allows you to explore data on natural disasters worldwide.
Each section is enhanced with icons and color to make the data more engaging.
""")

# Yearly Disaster Count Trend
st.write("### 📈 Yearly Disaster Count Trend")
plt.figure(figsize=(10, 5))
sns.lineplot(data=disaster, x='Year', y='Disaster Type', color="#1f77b4")
plt.title('Yearly Disaster Count Trend')
st.pyplot(plt)

# Count of Each Disaster Type
st.write("### 🌪️ Count of Each Disaster Type")
disaster_counts = disaster['Disaster Type'].value_counts()
plt.figure(figsize=(10, 5))
disaster_counts.plot(kind='bar', color='#4c72b0')
plt.title("Count of Each Disaster Type")
plt.xlabel("Disaster Type")
plt.ylabel("Count")
st.pyplot(plt)

# Top 10 Countries with Most Deaths Due to Natural Disasters
st.write("### 🏴 Top 10 Countries with Most Deaths Due to Natural Disasters")
deaths_by_country = disaster.groupby('Country')['Total Deaths'].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 5))
deaths_by_country.head(10).plot(kind='bar', color='#dd8452')
plt.title('Top 10 Countries with Most Deaths Due to Natural Disasters')
plt.xlabel('Country')
plt.ylabel('Total Deaths')
st.pyplot(plt)

# Total Deaths by Disaster Type
st.write("### ⚰️ Total Deaths by Disaster Type")
deaths_by_disaster = disaster.groupby('Disaster Type')['Total Deaths'].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 5))
deaths_by_disaster.plot(kind='bar', color='#55a868')
plt.title('Total Deaths by Disaster Type')
plt.xlabel('Disaster Type')
plt.ylabel('Total Deaths')
st.pyplot(plt)

# Total Deaths in China by Disaster Type
st.write("### 🇨🇳 Total Deaths in China by Disaster Type")
china_data = disaster[disaster['Country'] == 'China']
china_deaths_by_disaster = china_data.groupby('Disaster Type')['Total Deaths'].sum()
plt.figure(figsize=(10, 5))
china_deaths_by_disaster.plot(kind='bar', color='#c44e52')
plt.title('Total Deaths in China by Disaster Type')
plt.xlabel('Disaster Type')
plt.ylabel('Total Deaths')
st.pyplot(plt)

# Disaster Subgroups for Each Disaster Group
st.write("### 🌋 Disaster Subgroups by Disaster Group")
disaster_subgroup_count = disaster.groupby(['Disaster Group', 'Disaster Subgroup']).size().unstack()
for disaster_type in disaster_subgroup_count.index:
    plt.figure(figsize=(6, 6))
    disaster_subgroup_count.loc[disaster_type].plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=sns.color_palette("pastel"))
    plt.title(f'Disaster Subgroups for {disaster_type}')
    plt.ylabel('')
    st.pyplot(plt)

# Footer
st.write("---")
st.write("💡 *Tip*: You can use the sidebar to explore different sections quickly.")

# Optional: Customize color palette and add theme consistency with Matplotlib and Seaborn
sns.set_palette("Set2")
plt.style.use('seaborn-whitegrid')