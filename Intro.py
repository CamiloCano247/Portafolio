import streamlit as st
from PIL import Image

# Estilos CSS específicos (Solo fuente, color del sidebar y bordes de imagen)
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600&display=swap');
        
        /* Aplicar fuente Montserrat solo a los textos para no dañar los iconos nativos de Streamlit */
        h1, h2, h3, p, div[data-testid="stMarkdownContainer"] {
            font-family: 'Montserrat', sans-serif !important;
        }
        
        /* Color de fondo para la barra lateral */
        [data-testid="stSidebar"] {
            background-color: #D0F5C8 !important;
        }
        
        /* Color de texto oscuro para la barra lateral */
        [data-testid="stSidebar"] h1, 
        [data-testid="stSidebar"] h2, 
        [data-testid="stSidebar"] h3, 
        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] div[data-testid="stMarkdownContainer"] p {
            color: #222222 !important;
        }
        
        /* Bordes redondeados sutiles para las imágenes */
        img {
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Portafolio: Aplicaciones de Streamlit - Camilo Cano")

with st.sidebar:
  st.subheader("Portafolio: Aplicaciones de Streamlit")
  parrafo = (
    "En este portafolio encontrarás las aplicaciones de Streamlit en las que he trabajado "
    "a lo largo de las clases. Cada proyecto aborda diferentes temáticas como álgebra lineal, "
    "optimización, análisis de datos, modelos de regresión, series de tiempo, calidad del aire e Internet de las Cosas (IoT)."
  )
  st.write(parrafo)

url_ia="https://sites.google.com/view/computacinavanzada/inicio?pli=1&authuser=0"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")

col1, col2, col3 = st.columns(3)

with col1:
 st.subheader("1. Vectores y Matrices")
 image = Image.open('01_vectores_matrices.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace explorarás la aplicación interactiva sobre Vectores y Matrices.") 
 url = "https://clasfruta.streamlit.app/"
 st.write(f"[Vectores y Matrices]({url})")

 st.subheader("4. Preparación de datos")
 image = Image.open('04_preparacion_datos.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace verás las técnicas aplicadas para la preparación de datos.") 
 url = "https://puentegeom-trico.streamlit.app/"
 st.write(f"[Preparación de datos]({url})")

 st.subheader("7. Series de Tiempo")
 image = Image.open('07_series_de_tiempo.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace podrás analizar modelos para series temporales.") 
 url = "https://seriesdetiempo-hh7vhsdevg3fbcuh9th4ob.streamlit.app/"
 st.write(f"[Series de Tiempo]({url})")
 
 st.subheader("10. De regresión a logística")
 image = Image.open('10_regresion_logistica.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace verás el paso de modelos lineales a clasificación logística.") 
 url = "https://regresionlogistica-xbfpnr5ny8tgjulestszdu.streamlit.app/"
 st.write(f"[Regresión Logística]({url})")

with col2: 
 st.subheader("2. Cálculo aplicado")
 image = Image.open('02_calculo_gradiente.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace verás la optimización por gradiente descendente.") 
 url = "https://gradiente-exe.streamlit.app/"
 st.write(f"[Cálculo y gradiente]({url})")

 st.subheader("5. App Preparación datos")
 image = Image.open('05_app_preparacion_datos.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace explorarás un caso práctico de preparación de datos.") 
 url = "https://marco-cornare-mejora.streamlit.app/"
 st.write(f"[App Datos]({url})")

 st.subheader("8. Calidad de aire")
 image = Image.open('08_calidad_aire.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace evaluarás la predicción para calidad del aire.") 
 url = "https://calidadaire-bhqjufxnwosckvs4gsn6we.streamlit.app/"
 st.write(f"[Calidad de aire]({url})")

 st.subheader("11. Clasificación Knn")
 image = Image.open('11_clasificacion_knn.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace verás la clasificación por vecinos más cercanos.") 
 url = "https://clasificacionfertilidadsuelos-lhxgvoijgxkwsuty5ijbej.streamlit.app/"
 st.write(f"[Clasificación Knn]({url})")

with col3: 
 st.subheader("3. Lógica y Big-O")
 image = Image.open('03_logica_bigo_vectorizacion.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace verás análisis de complejidad y vectorización.") 
 url = "https://detectordeanomalias-123.streamlit.app/"
 st.write(f"[Big-O]({url})")

 st.subheader("6. Regresión Lineal")
 image = Image.open('06_regresion_lineal.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace explorarás el modelo de regresión lineal.") 
 url = "https://regresionlineal-el24vrs3exgv8d4rnmri6t.streamlit.app/"
 st.write(f"[Regresión Lineal]({url})")

 st.subheader("9. Sistema de IoT")
 image = Image.open('09_sistema_iot.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace verás la interacción con Internet de las Cosas.") 
 url = "https://talleriot-dtgvyh6nzaykts7qsodepz.streamlit.app/"
 st.write(f"[Sistema IoT]({url})")
