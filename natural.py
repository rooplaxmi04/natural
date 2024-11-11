import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set page config for Streamlit
st.set_page_config(page_title="Disaster Data Dashboard", page_icon="🌎", layout="wide")

# Load data
try:
    disaster = pd.read_csv("1900_2021_DISASTERS.xlsx - emdat data.csv")  # Make sure this file is in the correct path
except FileNotFoundError:
    st.error("The dataset file was not found. Please check the file path and format.")

# Sidebar for additional options
st.sidebar.header("Dashboard Navigation")
st.sidebar.write("Use the dropdown to explore different sections of the disaster data.")

# Dashboard title and introduction
st.title("🌎 Disaster Data Dashboard")
st.write("""
Welcome to the Disaster Data Dashboard! This interactive dashboard allows you to explore data on natural disasters worldwide.
Use the dropdown menu to select the visualization you want to explore.
""")

# Dropdown menu to select the graph
section = st.selectbox(
    "Select a section to view:",
    ["Top 10 Countries with Most Deaths", 
     "Total Deaths by Disaster Type", 
     "Total Deaths in China by Disaster Type", 
     "Disaster Subgroups by Disaster Group"]
)

# Check if data is loaded
if 'disaster' in locals():
    if section == "Top 10 Countries with Most Deaths":
        st.write("### 🏴 Top 10 Countries with Most Deaths Due to Natural Disasters")
        if 'Total Deaths' in disaster.columns:
            deaths_by_country = disaster.groupby('Country')['Total Deaths'].sum().sort_values(ascending=False)
            plt.figure(figsize=(10, 5))
            deaths_by_country.head(10).plot(kind='bar', color='#dd8452')
            plt.title('Top 10 Countries with Most Deaths Due to Natural Disasters')
            plt.xlabel('Country')
            plt.ylabel('Total Deaths')
            st.pyplot(plt)
            plt.clf()
        else:
            st.warning("Total Deaths column not found in dataset.")

    elif section == "Total Deaths by Disaster Type":
        st.write("### ⚰️ Total Deaths by Disaster Type")
        if 'Total Deaths' in disaster.columns:
            deaths_by_disaster = disaster.groupby('Disaster Type')['Total Deaths'].sum().sort_values(ascending=False)
            plt.figure(figsize=(10, 5))
            deaths_by_disaster.plot(kind='bar', color='#55a868')
            plt.title('Total Deaths by Disaster Type')
            plt.xlabel('Disaster Type')
            plt.ylabel('Total Deaths')
            st.pyplot(plt)
            plt.clf()

    elif section == "Total Deaths in China by Disaster Type":
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
            plt.clf()

    elif section == "Disaster Subgroups by Disaster Group":
        st.write("### 🌋 Disaster Subgroups by Disaster Group")
        if 'Disaster Group' in disaster.columns and 'Disaster Subgroup' in disaster.columns:
            disaster_subgroup_count = disaster.groupby(['Disaster Group', 'Disaster Subgroup']).size().unstack()
            for disaster_type in disaster_subgroup_count.index:
                plt.figure(figsize=(6, 6))
                disaster_subgroup_count.loc[disaster_type].plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=sns.color_palette("pastel"))
                plt.title(f'Disaster Subgroups for {disaster_type}')
                plt.ylabel('')
                st.pyplot(plt)
                plt.clf()
        else:
            st.warning("Disaster Group or Disaster Subgroup columns not found in dataset.")

    # Footer
    st.write("---")
    st.write("💡 *Tip*: Use the dropdown to quickly navigate to different sections.")

else:
    st.error("Failed to load data. Please check the file path and ensure the dataset is correctly formatted.")

# Optional: Customize color palette and add theme consistency with Seaborn
sns.set_palette("Set2")

