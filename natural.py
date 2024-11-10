import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set page config for Streamlit
st.set_page_config(page_title="Disaster Data Dashboard", page_icon="🌎", layout="wide")

# Load data
try:
    disaster = pd.read_csv("1900_2021_DISASTERS.xlsx - emdat data.csv")  # Ensure the correct CSV file path here
except FileNotFoundError:
    st.error("The dataset file was not found. Please check the file path and format.")

# Sidebar for additional options
st.sidebar.header("Dashboard Navigation")
st.sidebar.write("Use the navigation to explore different sections of the disaster data.")

# Dashboard title and introduction
st.title("🌎 Disaster Data Dashboard")
st.write("""
Welcome to the Disaster Data Dashboard! This interactive dashboard allows you to explore data on natural disasters worldwide.
Each section is enhanced with icons and color to make the data more engaging.
""")

# Check if data is loaded
if 'disaster' in locals():
    # Yearly Disaster Count Trend
    st.write("### 📈 Yearly Disaster Count Trend")
    yearly_counts = disaster.groupby('Year').size()  # Group by year for counts
    plt.figure(figsize=(10, 5))
    sns.lineplot(x=yearly_counts.index, y=yearly_counts.values, color="#1f77b4")
    plt.title('Yearly Disaster Count Trend')
    plt.xlabel("Year")
    plt.ylabel("Disaster Count")
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
    if 'Total Deaths' in disaster.columns:
        deaths_by_country = disaster.groupby('Country')['Total Deaths'].sum().sort_values(ascending=False)
        plt.figure(figsize=(10, 5))
        deaths_by_country.head(10).plot(kind='bar', color='#dd8452')
        plt.title('Top 10 Countries with Most Deaths Due to Natural Disasters')
        plt.xlabel('Country')
        plt.ylabel('Total Deaths')
        st.pyplot(plt)
    else:
        st.warning("Total Deaths column not found in dataset.")

    # Total Deaths by Disaster Type
    st.write("### ⚰️ Total Deaths by Disaster Type")
    if 'Total Deaths' in disaster.columns:
        deaths_by_disaster = disaster.groupby('Disaster Type')['Total Deaths'].sum().sort_values(ascending=False)
        plt.figure(figsize=(10, 5))
        deaths_by_disaster.plot(kind='bar', color='#55a868')
        plt.title('Total Deaths by Disaster Type')
        plt.xlabel('Disaster Type')
        plt.ylabel('Total Deaths')
        st.pyplot(plt)

    # Total Deaths in China by Disaster Type
    st.write("### 🇨🇳 Total Deaths in China by Disaster Type")
    if 'Total Deaths' in disaster.columns:
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
    if 'Disaster Group' in disaster.columns and 'Disaster Subgroup' in disaster.columns:
        disaster_subgroup_count = disaster.groupby(['Disaster Group', 'Disaster Subgroup']).size().unstack()
        for disaster_type in disaster_subgroup_count.index:
            plt.figure(figsize=(6, 6))
            disaster_subgroup_count.loc[disaster_type].plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=sns.color_palette("pastel"))
            plt.title(f'Disaster Subgroups for {disaster_type}')
            plt.ylabel('')
            st.pyplot(plt)
    else:
        st.warning("Disaster Group or Disaster Subgroup columns not found in dataset.")

    # Footer
    st.write("---")
    st.write("💡 *Tip*: You can use the sidebar to explore different sections quickly.")
else:
    st.error("Failed to load data. Please check the file path and ensure the dataset is correctly formatted.")

# Optional: Customize color palette and add theme consistency with Matplotlib and Seaborn
sns.set_palette("Set2")
plt.style.use('seaborn-whitegrid')
