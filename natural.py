import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Set page configuration for Streamlit
st.set_page_config(page_title="Enhanced Disaster Data ", page_icon="🌎", layout="wide")

# Load data
try:
    disaster = pd.read_csv("1900_2021_DISASTERS.xlsx - emdat data.csv")
except FileNotFoundError:
    st.error("The dataset file was not found. Please check the file path and format.")

# Custom CSS for improved styling
st.markdown("""
    <style>
        .reportview-container { background: #f4f4f9; color: #333; }
        .sidebar .sidebar-content { background: #2d3a4b; color: white; }
        .stButton>button { background-color: #4caf50; color: white; border-radius: 8px; font-size: 16px; }
        .stButton>button:hover { background-color: #45a049; }
        .stSelectbox { font-size: 16px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.header("Dashboard Navigation")
section = st.sidebar.selectbox(
    "Explore Disaster Data:", 
    [
        "Dataset Overview", 
        "Disaster Trends Over Time", 
        "Top Countries by Deaths and Damage", 
        "Deaths by Disaster Type", 
        "Geographical Map of Disasters", 
        "Correlations in Data"
    ]
)

# Main title
st.title("🌎 Enhanced Disaster Data Dashboard")
st.markdown("This dashboard provides an in-depth analysis of global disaster data from 1900 to 2021.")

# Check if data is loaded
if 'disaster' in locals():

    # Dataset Overview
    if section == "Dataset Overview":
        st.write("### 📊 Dataset Overview and Summary Statistics")
        st.write(disaster.head())
        st.write("**Summary Statistics:**")
        st.write(disaster.describe())
        st.write(f"**Total Records:** {disaster.shape[0]}")
        st.write(f"**Columns:** {', '.join(disaster.columns)}")

    # Disaster Trends Over Time
    elif section == "Disaster Trends Over Time":
        st.write("### 📈 Disaster Trends Over Time")
        if 'Year' in disaster.columns:
            year_trends = disaster.groupby('Year').size()
            plt.figure(figsize=(12, 6))
            sns.lineplot(x=year_trends.index, y=year_trends.values, color='blue')
            plt.title("Trend of Disaster Frequency Over Time")
            plt.xlabel("Year")
            plt.ylabel("Number of Disasters")
            st.pyplot(plt)
            plt.clf()

    # Top Countries by Deaths and Damage
    elif section == "Top Countries by Deaths and Damage":
        st.write("### 🏆 Top 10 Countries by Deaths and Economic Damage")
        deaths_by_country = disaster.groupby('Country')['Total Deaths'].sum().nlargest(10)
        damage_by_country = disaster.groupby('Country')['Total Damages'].sum().nlargest(10)

        # Plot Deaths
        fig1, ax1 = plt.subplots(figsize=(10, 5))
        deaths_by_country.plot(kind='bar', ax=ax1, color='#dd8452')
        ax1.set_title("Top 10 Countries by Total Deaths")
        ax1.set_xlabel("Country")
        ax1.set_ylabel("Total Deaths")
        st.pyplot(fig1)
        
        # Plot Economic Damage
        fig2, ax2 = plt.subplots(figsize=(10, 5))
        damage_by_country.plot(kind='bar', ax=ax2, color='#55a868')
        ax2.set_title("Top 10 Countries by Economic Damage")
        ax2.set_xlabel("Country")
        ax2.set_ylabel("Total Damages (in USD)")
        st.pyplot(fig2)

    # Deaths by Disaster Type
    elif section == "Deaths by Disaster Type":
        st.write("### ⚰️ Total Deaths by Disaster Type")
        deaths_by_disaster = disaster.groupby('Disaster Type')['Total Deaths'].sum().sort_values(ascending=False)
        plt.figure(figsize=(12, 6))
        sns.barplot(x=deaths_by_disaster.index, y=deaths_by_disaster.values, palette="viridis")
        plt.title("Total Deaths by Disaster Type")
        plt.xlabel("Disaster Type")
        plt.ylabel("Total Deaths")
        st.pyplot(plt)
        plt.clf()

    # Geographical Map of Disasters
    elif section == "Geographical Map of Disasters":
        st.write("### 🗺️ Geographical Distribution of Disasters")
        if 'Country' in disaster.columns:
            disaster_map = disaster['Country'].value_counts()
            disaster_map_df = pd.DataFrame({
                'Country': disaster_map.index,
                'Disaster Count': disaster_map.values
            })
            fig_map = px.choropleth(
                disaster_map_df, 
                locations="Country", 
                locationmode="country names",
                color="Disaster Count", 
                color_continuous_scale="Blues",
                title="Disaster Frequency by Country"
            )
            st.plotly_chart(fig_map)

    # Correlations in Data
    elif section == "Correlations in Data":
        st.write("### 🔍 Correlations Between Variables")
        if disaster.select_dtypes(include=['float64', 'int64']).shape[1] > 1:
            corr = disaster.corr()
            fig, ax = plt.subplots(figsize=(10, 8))
            sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
            plt.title("Correlation Heatmap")
            st.pyplot(fig)
        else:
            st.warning("Not enough numerical columns for correlation analysis.")

    # Footer
    st.write("---")
    st.write("💡 *Tip*: Use the sidebar to navigate and explore different analyses.")

else:
    st.error("Data not loaded. Please verify the dataset path and format.")

# Set seaborn style
sns.set_style("whitegrid")
