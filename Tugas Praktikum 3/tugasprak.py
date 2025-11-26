import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Desain Background
st.markdown(
    """
    <style>
    .stApp {
        background-color: #ffe6f0;
    }
    .header-title {
        font-size: 2.5rem;
        font-weight: bold;
        color: #b8005c;
        text-align: center;
        margin-bottom: 0.5em;
    }
    .header-desc {
        font-size: 1.2rem;
        color: #b8005c;
        text-align: center;
        margin-bottom: 1.5em;
    }
    .main-title, .subheader-title {
        color: #b8005c !important;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header dengan gambar dan judul
st.markdown(
    '''
    <div style="display: flex; justify-content: center;">
        <img src="https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=900&q=80" 
             style="width: 250px; max-width: 15vw; border-radius: 20px; box-shadow: 0 4px 16px rgba(184,0,92,0.08);" />
    </div>
    ''', unsafe_allow_html=True)

st.markdown('<div class="header-title">Aplikasi Visualisasi Data Scripto</div>', unsafe_allow_html=True)
st.markdown('<div class="header-desc">Selamat datang di aplikasi visualisasi data Scripto! Jelajahi berbagai fitur, data pengguna, dan karya yang diunggah dengan visualisasi interaktif.</div>', unsafe_allow_html=True)

data = pd.DataFrame({
    "Pengguna": [f"Pengguna {i+1}" for i in range(10)],
    "Domisili": ['Balikpapan', 'Samboja', 'Jakarta', 'Toraja', 'Bali', 'Medan', 'Bandung', 'Papua', 'NTT', 'Korea'],
    "Total Unggahan (Karya)": [7, 50, 50, 60, 80, 95, 47, 70, 100, 95],
})

st.markdown('<span class="subheader-title">Data Pengguna Aplikasi Scripto</span>', unsafe_allow_html=True)
st.dataframe(data)

# Visualisasi Dropdown
st.markdown('<div style="text-align:center;"><span style="color:#b8005c; font-weight:bold; font-size:1.1rem;">Pilih Tipe Visualisasi</span></div>', unsafe_allow_html=True)
tipe = st.selectbox("", ["Pie Chart", "Bar Chart", "Line Chart", "Map Chart", "Area Chart"])

if tipe == "Pie Chart":
    st.markdown('<span class="main-title">Pie Chart Total Unggahan per Pengguna</span>', unsafe_allow_html=True)
    import numpy as np
    colors = ["#ffb3c6", "#ff8fab", "#f7aef8", "#b4f8c8", "#a0e7e5", "#fbe7c6", "#cdb4ff", "#b5ead7", "#f6c1c7", "#ffd6e0"]
    fig, ax = plt.subplots(figsize=(7, 7))
    wedges, texts, autotexts = ax.pie(
        data["Total Unggahan (Karya)"],
        labels=data["Pengguna"],
        autopct='%1.1f%%',
        colors=colors,
        startangle=140,
        pctdistance=0.85,
        wedgeprops={"edgecolor": "white", "linewidth": 2}
    )
    # Style labels
    for text in texts:
        text.set_color('#b8005c')
        text.set_fontsize(12)
        text.set_fontweight('bold')
    for autotext in autotexts:
        autotext.set_color('#b8005c')
        autotext.set_fontsize(12)
        autotext.set_fontweight('bold')
    ax.set_aspect('equal')
    st.pyplot(fig)
    st.markdown('<span style="color:#b8005c;">Pie chart ini menunjukkan proporsi total unggahan karya dari masing-masing pengguna.</span>', unsafe_allow_html=True)

elif tipe == "Bar Chart":
    st.markdown('<span class="main-title">Bar Chart Total Unggahan per Pengguna</span>', unsafe_allow_html=True)
    st.bar_chart(data.set_index("Pengguna")[["Total Unggahan (Karya)"]])
    st.markdown('<span style="color:#b8005c;">Bar chart ini menampilkan jumlah unggahan karya setiap pengguna secara visual.</span>', unsafe_allow_html=True)

elif tipe == "Line Chart":
    st.markdown('<span class="main-title">Line Chart Total Unggahan per Pengguna</span>', unsafe_allow_html=True)
    st.line_chart(data.set_index("Pengguna")[["Total Unggahan (Karya)"]])
    st.markdown('<span style="color:#b8005c;">Line chart ini memperlihatkan tren jumlah unggahan karya dari pengguna 1 hingga 10.</span>', unsafe_allow_html=True)

elif tipe == "Map Chart":
    st.markdown('<span class="main-title">Peta Penyebaran Domisili Pengguna</span>', unsafe_allow_html=True)
    data_peta = pd.DataFrame(data={
        'lokasi': ['Balikpapan', 'Samboja', 'Jakarta', 'Toraja', 'Bali', 'Medan', 'Bandung', 'Papua', 'NTT', 'Korea'],
        'lat': [-1.27, -1.10, -6.20, -3.08, -8.65, 3.59, -6.91, -2.53, -8.65, 37.57],
        'lon': [116.83, 117.00, 106.82, 119.89, 115.22, 98.67, 107.60, 140.70, 120.99, 126.98],
    })
    st.map(data_peta)
    st.markdown('<span style="color:#b8005c;">Map chart ini menampilkan lokasi domisili pengguna pada peta.</span>', unsafe_allow_html=True)

elif tipe == "Area Chart":
    st.markdown('<span class="main-title">Area Chart Total Unggahan per Pengguna</span>', unsafe_allow_html=True)
    st.area_chart(data.set_index("Pengguna")[["Total Unggahan (Karya)"]])
    st.markdown('<span style="color:#b8005c;">Area chart ini menggambarkan distribusi total unggahan karya secara kumulatif.</span>', unsafe_allow_html=True)

# Tambahan Slider
st.markdown('<span style="color:#b8005c;">Tampilkan pengguna dengan unggahan karya minimum:</span>', unsafe_allow_html=True)
nilai = st.slider("", 0, 150, 50)
st.dataframe(data[data["Total Unggahan (Karya)"] >= nilai])


