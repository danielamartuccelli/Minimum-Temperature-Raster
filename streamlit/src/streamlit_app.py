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
tab1, tab2, tab3, tab4 = st.tabs(["📊 Distribución de temperaturas", "🥈 🏅 🏆 🥉 🥇 Ranking", "🌍 Mapas de distribución geográfica de temperaturas mínimas", "Propuesta de política pública"])

# TAB 1: Distribución de temperaturas 
with tab1:
    st.header("📋 Distribución de temperaturas")
    
    # Mostrar imagen
    st.image('streamlit/assets/01_distribucion_v2.png', use_container_width=True)

    # Segunda imagen
    st.image('streamlit/assets/01b_distribucion.png', use_container_width=True)
    
    st.divider()
    


# TAB 2: 🥈 🏅 🏆 🥉 🥇 Ranking
with tab2:
    st.header("🥇 Ranking de los 15 distritos con temperaturas mínimas y máximas")


    # Mostrar imagen
    st.image('streamlit/assets/02_ranking_v2.png', use_container_width=True)


    # Segunda imagen
    st.image('streamlit/assets/02b_ranking_V2.png', use_container_width=True)


    st.divider()


# TAB 3: Mapas Estáticos
with tab3:
    st.header("🌍 Mapa de temperatura mínima por distrito")

    # Mostrar imagen
    st.image('streamlit/assets/03_mapa_v2.png', use_container_width=True)


    #Segunda imagen
    st.image('streamlit/assets/04_mapa_frio_extremo.png', use_container_width=True)


    # Botón para descargar CSV
    csv_path = 'data/estadisticas_completas.csv'  # Ajusta el nombre del archivo
    
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
    
    
    st.divider()


# TAB 4: Propuestas de política pública
with tab4:
     st.header("Propuestas de política pública ante el frío extremo")

     st.markdown("""
     Considerando el diagnóstico de distritos con menor temperatura promedio, se proponen las siguientes 3 intervenciones enfocadas en las localidades de la sierra sur y antiplánica del país.""") 

     st.markdown("""
    Política 1""")
     
     st.markdown("""
    **Programa de Viviendas Térmicas Rurales (ISUR Ampliado)***""")
     
     st.markdown("""
    Objetivo: Reducir en un treinta por cierto (30%) los casos de infecciones respiratorias agudas (IRA) en población infantil en zonas altoandinas con temperaturas promedio menor a 0 °C""")
     
     st.markdown("""
    Territorio y población objetivo: Distritos rurales en Puno, Arequipa, Cusco, Tacna, Moquegua y Huancavelica identificados como los más fríos (temperatura anual promedio por debajo de los 0 grados). Población meta: 50 000 hogares rurales en altitudes""")
     
     st.markdown("""
    Intervención""")
     
     st.markdown("""
    1.Implementación de viviendas térmicamente mejoradas (paredes aislantes, techos dobles, sistemas pasivos de calefacción solar).""")
     
     st.markdown("""
    2.Complementario al programa “Mi Abrigo” (FONCODES), pero con criterios geoespaciales basados en análisis raster.""")
     
     st.markdown("""
    Costo estimado: S/ 8 000 por vivienda con una meta de 50 000 hogares. El costo total de la intervención asciende a S/ 400 millones.""")
     
     st.markdown("""
    KPIn/
    1.Disminucion en un 30 % de casos IRA en la población infantil en temporada de friaje (Fuente: ESSALUD/MINSA).n/
    2. Aumento de un 20 % de confort térmico reportado por hogares (Fuente: SISFOH).n/
    3. Aumento de un 15 % de asistencia escolar en invierno (Fuente: MINEDU).""")
     
     st.markdown("""
    Política 2/n
    ***Fondo de Adaptación Agropecuaria al Friaje***n/
    Objetivo: Reducir pérdidas agrícolas y ganaderas en 25 % en distritos de la sierra sur expuestos a heladas recurrentes.n/
    Territorio y población objetivo: Distritos agrícolas en Puno, Cusco y Arequipa con temperatura promedio menor a ≤ 0 °C (105 distritos). Población meta: 30 000 productores agropecuarios familiares.n/
    Intervención:n/
    1. Entrega de kits antiheladas (módulos de riego nocturno, mantas térmicas agrícolas).n/
    2. Capacitación en calendarios agrícolas adaptativos.n/
    3. Construcción de módulos de refugio ganadero para alpacas y ovinos.n/
    Costo estimado: S/ 8 000 por agricultor con una meta de 30 000 trabajadores. El costo total de la intervención asciende a S/ 240 millones.n/
    KPIn/
    1. Disminuación en un 25 % de pérdidas reportadas en cultivos andinos (Fuente: MINAGRI).n/
    2. Disminución en un 15 % de mortalidad de alpacas y ovinos en época de heladas(Fuente: SENASA).n/
    3. 80% de agricultores capacitados adoptan prácticas agrícolas adaptadas al clima (Fuente: MINAGRI).""")
     
     st.markdown("""
    Política 3""")


    
