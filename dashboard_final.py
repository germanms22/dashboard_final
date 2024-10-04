import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

day_df = pd.read_csv('day.csv')
weekday_cnt = day_df.groupby(by='weekday').cnt.sum().sort_values(ascending=False).reset_index()
workday_cnt = day_df.groupby(by='workingday').cnt.sum().sort_values(ascending=False).reset_index()
weather_cnt = day_df.groupby(by='weathersit').cnt.sum().sort_values(ascending=False).reset_index()

st.header('Hasil Analisis Data Eksploratori Bike-Sharing')

st.subheader('Perbandingan Perubahan Cuaca tiap Bulan antara 2011 dan 2012')

col1, col2 = st.columns(2)
#Membagi dataset menjadi tahun 2011 dan 2012
year_0 = day_df[day_df['yr']==0]
year_1 = day_df[day_df['yr']==1]
#Mengambil subset data untuk visualisasi perbandingan bulan dengan jumlah rental
month_cnt_0 = year_0.groupby(by='mnth')['cnt'].sum().reset_index()
month_cnt_1 = year_1.groupby(by='mnth')['cnt'].sum().reset_index()

fig, ax = plt.subplots(1, 2, figsize=(24, 6))
#Tahun 2011
sns.lineplot(x='mnth', y='temp', data=year_0,ax=ax[0], label='Temprature')
sns.lineplot(x='mnth', y='atemp', data=year_0, ax=ax[0], label='Apparent Temperature')
sns.lineplot(x='mnth', y='hum', data=year_0, ax=ax[0], label='Humidity')
sns.lineplot(x='mnth', y='windspeed', data=year_0, ax=ax[0], label= 'Windspeed')
ax[0].set_title("Perubahan cuaca tiap bulan pada Tahun 2011")
ax[0].legend()
ax[0].set_ylabel(None)

#Tahun 2012
sns.lineplot(x='mnth', y='temp', data=year_1,ax=ax[1], label='Temprature')
sns.lineplot(x='mnth', y='atemp', data=year_1, ax=ax[1], label='Apparent Temperature')
sns.lineplot(x='mnth', y='hum', data=year_1, ax=ax[1], label='Humidity')
sns.lineplot(x='mnth', y='windspeed', data=year_1, ax=ax[1], label= 'Windspeed')
ax[1].set_title("Perubahan cuaca tiap bulan pada Tahun 2012")
ax[1].legend()
ax[1].set_ylabel(None)
st.pyplot(fig)

st.subheader('Perbandingan Jumlah Rental tiap Bulan antara 2011 dan 2012')
#Visualisasi perubahan jumlah rentalnya tiap bulan
fig, ax= plt.subplots(1, 2, figsize=(24,6))

#Tahun 2011
sns.barplot(x='mnth', y='cnt', data=month_cnt_0, ax=ax[0])
ax[0].set_title('Perubahan jumlah rental tiap bulan pada tahun 2011')
ax[0].set_ylabel('Count')
ax[0].grid(True, axis='y', linestyle='--', alpha=0.6)

#Tahun 2012
sns.barplot(x='mnth', y='cnt', data=month_cnt_1, ax=ax[1])
ax[1].set_title('Perubahan jumlah rental tiap bulan pada tahun 2012')
ax[1].set_ylabel(None)
ax[1].grid(True, axis='y', linestyle='--', alpha=0.6)

st.pyplot(fig)

st.caption('Dilihat dari grafik perubahan cuaca dengan perubahan jumlah rental tiap bulan dapat memperlihatkan bahwa jumlah rental bike-sharing meningkat juga ketika temperatur, atemp, humidity meningkat pada rentang bulan 6 dan bulan 8.')

st.subheader('Korelasi antar Fitur Cuaca')
#Melihat korelasi antar fitur cuaca
plt.figure(figsize=(16, 6))
selected_col = ['mnth','temp','atemp','hum','windspeed', 'cnt']

heatmap = sns.heatmap(day_df[selected_col].corr(), vmin=-1, vmax=1, annot=True, cmap='BrBG')
st.pyplot(plt)
st.caption('Grafik korelasi juga menunjukkan ada korelasi yang cukup tinggi antara temp dan atemp dengan jumlah rental')

st.subheader('Perbandingan Jumlah Rental pada Hari-Hari Tertentu')

tab1, tab2, tab3 = st.tabs(["Hari Umumnya", "Hari Kerja", "Berdasarkan Cuaca"])
with tab1:
    fig, ax = plt.subplots()
    
    colors = ["#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#72BCD4", "#D3D3D3"]
    # Subplot pertama: Weekday vs Cnt
    sns.barplot(x='weekday', y='cnt', data=weekday_cnt, ax=ax, palette=colors)
    ax.set_title('Total Count per Weekday', fontsize=16)
    ax.set_xlabel('Weekday', fontsize=14)
    ax.set_ylabel('Count', fontsize=14)
    ax.grid(True, axis='y', linestyle='--', alpha=0.6)

    # Display the plot in Streamlit
    st.pyplot(fig)

with tab2:
    fig, ax = plt.subplots()
    
    colors_ = ["#D3D3D3", "#72BCD4"]
    # Subplot kedua: Workingday vs Cnt
    sns.barplot(x='workingday', y='cnt', data=workday_cnt, ax=ax, palette=colors_)
    ax.set_title('Total Count per Working Day', fontsize=16)
    ax.set_xlabel('Working Day', fontsize=14)
    ax.set_ylabel('Count', fontsize=14)
    ax.grid(True, axis='y', linestyle='--', alpha=0.6)
    st.pyplot(fig)

with tab3:
    fig, ax = plt.subplots()
    
    colors__ = ["#72BCD4", "#D3D3D3", "#D3D3D3"]
    # Visualisasi jumlah rental pada kondisi cuaca tertentu
    sns.barplot(x='weathersit', y='cnt', data=weather_cnt, ax=ax, palette=colors__)
    ax.set_title('Total Count per Weathersit', fontsize=16)
    ax.set_xlabel('Weathersit', fontsize=14)
    ax.set_ylabel('Count', fontsize=14)
    ax.grid(True, axis='y', linestyle='--', alpha=0.6)
    st.pyplot(fig)
st.caption('Grafik perubahan jumlah rental pada hari-hari tertentu melihat bahwa jumlah rental terbanyak cenderung pada hari Sabtu.')

st.subheader('Conclusion') 
st.markdown(
    """
    1. Perubahan cuaca bersesuaian dengan pola berubahan jumlah rental bike-sharing sehingga dapat disimpulkan bahwa perubahan cuaca berpengaruh terhadap jumlah rental.\n
    2. Sejalan dengan itu, hari dengan jumlah terbanyak rental-bike sharing adalah ketika hari libur atau weekend dengan cuaca yang baik.
    """
)