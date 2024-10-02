# Import libraries
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from datetime import datetime

# Load dataset
day_data = pd.read_csv('day.csv')
hour_data = pd.read_csv('hour.csv')

# Data Wrangling
day_data['dteday'] = pd.to_datetime(day_data['dteday'])

# Sidebar
st.sidebar.title('Bike Sharing Dashboard')
st.sidebar.write("Pilih Fitur untuk menjelajahi data:")

# Sidebar untuk memilih opsi
analysis_type = st.sidebar.selectbox("Pilih Tipe Analisis", ['Exploratory Data Analysis', 'Correlation Matrix', 'Dampak Cuaca', 'Dampak Hari Libur'])

# Exploratory Data Analysis
if analysis_type == 'Exploratory Data Analysis':
    st.title("Exploratory Data Analysis")
    
    # preview beberapa data dari datasets 
    st.write("### Preview data:")
    st.write(day_data.head())

    # ringkasan parameter statistik
    st.write("### Ringkasan Parameter Statistik:")
    st.write(day_data.describe())

    # menunjukkan missing values
    st.write("### Missing Values di Dataset:")
    st.write(day_data.isnull().sum())

# Correlation Matrix
elif analysis_type == 'Correlation Matrix':
    st.title("Correlation Matrix of Day Dataset")

    # menghitung korelasi
    correlation_matrix = day_data.corr()

    # buat Plot untuk heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', annot_kws={"size": 10})
    plt.title('Correlation Matrix of Day Dataset')
    st.pyplot(plt)

# Dampak Cuaca
elif analysis_type == 'Dampak Cuaca':
    st.title("Dampak Cuaca terhadap Penyewaan Sepeda")

    # Scatter plots untuk kondisi Cuaca
    st.write("### Suhu, Kelembapan, and Kecepatan Angin vs Penyewaan Sepeda")

    # Suhu vs. Penyewaan Sepeda
    fig, ax = plt.subplots(1, 3, figsize=(15, 5))

    sns.scatterplot(x='temp', y='cnt', data=day_data, ax=ax[0], color='orange')
    ax[0].set_title('Suhu vs. Penyewaan Sepeda')

    # Kelembapan vs. Penyewaan Sepeda
    sns.scatterplot(x='hum', y='cnt', data=day_data, ax=ax[1], color='blue')
    ax[1].set_title('Kelembapan vs. Penyewaan Sepeda')

    # Kecepatan Angin vs. Penyewaan Sepeda
    sns.scatterplot(x='windspeed', y='cnt', data=day_data, ax=ax[2], color='green')
    ax[2].set_title('Kecepatan Angin vs. Penyewaan Sepeda')

    st.pyplot(fig)

# Dampak Liburan dan Akhir Pekan
elif analysis_type == 'Dampak Hari Libur':
    st.title("Dampak Hari Libur dan Akhir Pekan terhadap Penyewaan Sepeda")

    # Bar plot untuk Pengguna Biasa vs Pengguna Terdaftar pada Hari Libur
    st.write("### Pengguna Biasa vs Pengguna Terdaftar pada Hari Libur")

    fig, ax = plt.subplots(figsize=(10, 6))

    sns.barplot(x='holiday', y='casual', data=day_data, color='red', label='Casual', ax=ax)
    sns.barplot(x='holiday', y='registered', data=day_data, color='blue', label='Registered', ax=ax)
    ax.set_title('Penyewaan Sepeda di Hari Libur (Santai vs Terdaftar)')
    ax.legend()
    st.pyplot(fig)

    # Bar plot untuk Penyewaan pada Hari Kerja vs Hari Non-kerja
    st.write("### Penyewaan pada Hari Kerja vs Hari Non-kerja")

    fig, ax = plt.subplots(figsize=(10, 6))

    sns.barplot(x='workingday', y='cnt', data=day_data, hue='holiday', ax=ax)
    ax.set_title('Penyewaan Sepeda pada Hari Kerja vs Hari Non-kerja')
    st.pyplot(fig)

# Footer
st.sidebar.write("Dasbor untuk Analisis Data pada Dataset Bike Sharing")
