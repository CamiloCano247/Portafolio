import streamlit as st
from PIL import Image

# Configuración inicial de la página
st.set_page_config(
    page_title="Portafolio - Camilo Cano",
    page_icon="💻",
    layout="wide"
)

# Aplicar estilos CSS personalizados: Fuente Montserrat y color de la barra lateral (#D0F5C8)
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap');

        html, body, [class*="css"], [class*="st-"] {
            font-family: 'Montserrat', sans-serif !important;
        }

        [data-testid="stSidebar"] {
            background-color: #D0F5C8;
        }
    </style>
""", unsafe_allow_html=True)

# Título principal de la página
st.title("Portafolio: Aplicaciones de Streamlit - Camilo Cano")

# Contenido de la barra lateral
with st.sidebar:
  st.subheader("Portafolio: Aplicaciones de Streamlit")
  parrafo = (
    "En este portafolio encontrarás las aplicaciones de Streamlit en las que he trabajado "
    "a lo largo de las clases. Cada proyecto aborda diferentes temáticas como álgebra lineal, "
    "optimización, análisis de datos, modelos de regresión, series de tiempo, calidad del aire e Internet de las Cosas (IoT)."
  )
  st.write(parrafo)

# Enlace principal del curso
url_curso = "https://sites.google.com/view/computacinavanzada/inicio?pli=1&authuser=0"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_curso})")

# Distribución del portafolio en 3 columnas
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("1. Vectores y Matrices")
    image1 = Image.open('01_vectores_matrices.jpg')
    st.image(image1, use_container_width=True)
    st.write("En el siguiente enlace explorarás la aplicación interactiva sobre Vectores y Matrices.") 
    st.write("Vectores y Matrices: [Enlace](https://clasfruta.streamlit.app/)")

    st.subheader("4. Preparación de datos")
    image4 = Image.open('04_preparacion_datos.jpg')
    st.image(image4, use_container_width=True)
    st.write("En el siguiente enlace verás las técnicas aplicadas para la preparación y limpieza de datos.") 
    st.write("Preparación de datos: [Enlace](https://puentegeom-trico.streamlit.app/)")

    st.subheader("7. Series de Tiempo")
    image7 = Image.open('07_series_de_tiempo.jpg')
    st.image(image7, use_container_width=True)
    st.write("En el siguiente enlace podrás analizar modelos predictivos para series temporales.") 
    st.write("Series de Tiempo: [Enlace](https://seriesdetiempo-hh7vhsdevg3fbcuh9th4ob.streamlit.app/)")

    st.subheader("10. De la regresión lineal a la logística")
    image10 = Image.open('10_regresion_logistica.jpg')
    st.image(image10, use_container_width=True)
    st.write("En el siguiente enlace verás el paso de modelos de regresión lineal a clasificación logística.") 
    st.write("Regresión Logística: [Enlace](https://regresionlogistica-xbfpnr5ny8tgjulestszdu.streamlit.app/)")

with col2: 
    st.subheader("2. Cálculo aplicado, gradiente")
    image2 = Image.open('02_calculo_gradiente.jpg')
    st.image(image2, use_container_width=True)
    st.write("En el siguiente enlace verás el cálculo aplicado y la optimización por gradiente descendente.") 
    st.write("Gradiente: [Enlace](https://gradiente-exe.streamlit.app/)")

    st.subheader("5. Aplicación Preparación de datos")
    image5 = Image.open('05_app_preparacion_datos.jpg')
    st.image(image5, use_container_width=True)
    st.write("En el siguiente enlace explorarás un caso práctico de preparación avanzada de datos.") 
    st.write("App Preparación de datos: [Enlace](https://marco-cornare-mejora.streamlit.app/)")

    st.subheader("8. Predicción y calidad del aire")
    image8 = Image.open('08_calidad_aire.jpg')
    st.image(image8, use_container_width=True)
    st.write("En el siguiente enlace evaluarás el modelo de predicción para calidad del aire.") 
    st.write("Calidad de aire: [Enlace](https://calidadaire-bhqjufxnwosckvs4gsn6we.streamlit.app/)")

    st.subheader("11. Clasificación KNN")
    image11 = Image.open('11_clasificacion_knn.jpg')
    st.image(image11, use_container_width=True)
    st.write("En el siguiente enlace verás el algoritmo de clasificación por vecinos más cercanos (KNN).") 
    st.write("Clasificación KNN: [Enlace](https://clasificacionfertilidadsuelos-lhxgvoijgxkwsuty5ijbej.streamlit.app/)")

with col3: 
    st.subheader("3. Lógica, Big-O y Vectorización")
    image3 = Image.open('03_logica_bigo_vectorizacion.jpg')
    st.image(image3, use_container_width=True)
    st.write("En el siguiente enlace verás análisis de complejidad algorítmica y vectorización.") 
    st.write("Big-O y Vectorización: [Enlace](https://detectordeanomalias-123.streamlit.app/)")

    st.subheader("6. Regresión Lineal")
    image6 = Image.open('06_regresion_lineal.jpg')
    st.image(image6, use_container_width=True)
    st.write("En el siguiente enlace explorarás la implementación del modelo de regresión lineal.") 
    st.write("Regresión Lineal: [Enlace](https://regresionlineal-el24vrs3exgv8d4rnmri6t.streamlit.app/)")

    st.subheader("9. Sistema de IoT")
    image9 = Image.open('09_sistema_iot.jpg')
    st.image(image9, use_container_width=True)
    st.write("En el siguiente enlace verás la interacción con sistemas de Internet de las Cosas.") 
    st.write("Sistema IoT: [Enlace](https://talleriot-dtgvyh6nzaykts7qsodepz.streamlit.app/)")
