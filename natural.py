import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Load Data
disaster = pd.read_csv("/content/1900_2021_DISASTERS.xlsx - emdat data.csv")

# Set the title of the app
st.title("Global Natural Disaster Analysis")

# Sidebar with options
st.sidebar.title("Dashboard Filters")
disaster_type = st.sidebar.selectbox("Select Disaster Type", disaster['Disaster Type'].unique())
country = st.sidebar.selectbox("Select Country", disaster['Country'].unique())

# Display the DataFrame (optional)
st.write("Disaster Data Overview", disaster.head())

# Create a line plot for yearly disaster count trend
st.subheader('Yearly Disaster Count Trend')
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(data=disaster, x='Year', y='Disaster Type', ax=ax)
ax.set_title('Yearly Disaster Count Trend')
st.pyplot(fig)

# Display total counts of disaster types as a bar plot
st.subheader('Count of Each Disaster Type')
disaster_counts = disaster['Disaster Type'].value_counts()
fig, ax = plt.subplots(figsize=(10, 6))
disaster_counts.plot(kind='bar', color='skyblue', ax=ax)
ax.set_title("Count of Each Disaster Type")
ax.set_xlabel("Disaster Type")
ax.set_ylabel("Count")
st.pyplot(fig)

# Top 10 countries with most deaths due to natural disasters
st.subheader('Top 10 Countries with Most Deaths Due to Natural Disasters')
deaths_by_country = disaster.groupby('Country')['Total Deaths'].sum().sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(10, 6))
deaths_by_country.head(10).plot(kind='bar', color='skyblue', ax=ax)
ax.set_title('Top 10 Countries with Most Deaths Due to Natural Disasters')
ax.set_xlabel('Country')
ax.set_ylabel('Total Deaths')
st.pyplot(fig)

# Total deaths by disaster type
st.subheader('Total Deaths by Disaster Type')
deaths_by_disaster = disaster.groupby('Disaster Type')['Total Deaths'].sum().sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(10, 6))
deaths_by_disaster.plot(kind='bar', color='coral', ax=ax)
ax.set_title('Total Deaths by Disaster Type')
ax.set_xlabel('Disaster Type')
ax.set_ylabel('Total Deaths')
st.pyplot(fig)

# Total deaths in a specific country (e.g., China)
china_data = disaster[disaster['Country'] == 'China']
china_deaths_by_disaster = china_data.groupby('Disaster Type')['Total Deaths'].sum()
st.subheader('Total Deaths in China by Disaster Type')
fig, ax = plt.subplots(figsize=(10, 6))
china_deaths_by_disaster.plot(kind='bar', color='skyblue', ax=ax)
ax.set_title('Total Deaths in China by Disaster Type')
ax.set_xlabel('Disaster Type')
ax.set_ylabel('Total Deaths')
st.pyplot(fig)

# Disaster subgroup analysis
st.subheader('Disaster Subgroups Analysis')
disaster_subgroup_count = disaster.groupby(['Disaster Group', 'Disaster Subgroup']).size().unstack()

for disaster_type in disaster_subgroup_count.index:
    st.write(f"Disaster Subgroups for {disaster_type}")
    fig, ax = plt.subplots(figsize=(6, 6))
    disaster_subgroup_count.loc[disaster_type].plot(kind='pie', autopct='%1.1f%%', startangle=90, ax=ax)
    ax.set_title(f'Disaster Subgroups for {disaster_type}')
    ax.set_ylabel('')
    st.pyplot(fig)

           

           

  
