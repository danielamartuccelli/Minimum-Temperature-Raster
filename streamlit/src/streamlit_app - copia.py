import streamlit as st
import pandas as pd
import geopandas as gpd
import folium
import os
import matplotlib
matplotlib.use('Agg')  # Backend para Streamlit

# Configuración de página
st.set_page_config(
    page_title="Análisis del nivel de temperatura en los distritos del Perú utilizando imágenes raster",
    page_icon="❄️🔥",
    layout="wide"
)

# Título principal
st.title("❄️🔥 Análisis del nivel de temperatura en los distritos del Perú utilizando imágenes raster")

# Crear tabs
tab1, tab2, tab3 = st.tabs(["📊 Distribución de temperaturas", "🥈 🏅 🏆 🥉 🥇 Ranking", "🌍 Mapas de distribución geográfica de temperaturas mínimas"])

# TAB 1: Distribución de temperaturas 
with tab1:
    st.header("📋 Distribución de temperaturas")
    
    # Mostrar imagen
st.image('streamlit/assets/01_distribucion.png', use_container_width=True)

    # Segunda imagen
st.image('streamlit/assets/01b_distribucion.png', use_container_width=True)
    
st.divider()
    


# TAB 2: 🥈 🏅 🏆 🥉 🥇 Ranking
with tab2:
    st.header("🥇 Ranking de los distritos con temperaturas mínimas y máximas")


    # Mostrar imagen
st.image('streamlit/assets/02_ranking_v2.png', use_container_width=True)


    # Segunda imagen
st.image('streamlit/assets/01b_distribucion.png', use_container_width=True)

st.divider()


# TAB 3: Mapas Estáticos
with tab3:
    st.header("🌍 Mapa de temperatura mínima por distrito")

    # Mostrar imagen
st.image('streamlit/assets/03_mapa.png', use_container_width=True)


    # Botón para descargar CSV # Ajusta el nombre del archivo
csv_path = 'data/estadisticas_completas.csv'
try:
        with open(csv_path, 'rb') as f:
            csv_data = f.read()
        
        st.download_button(
            label="📥 Descargar datos (CSV)",
            data=csv_data,
            file_name="datos_temperatura.csv",
            mime="text/csv"
        )
except FileNotFoundError:
    st.error(f"No se encontró el archivo: {csv_path}")



    
