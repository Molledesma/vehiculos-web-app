import streamlit as st
import pandas as pd
import plotly.express as px

# importación de datos
car_data = pd.read_csv('vehicles_us.csv')

# Crear un encabezado para la aplicación
st.header('Análisis de Datos de Vehículos Usados')

# Crear un botón
hist_button = st.button('Construir histograma')

# Cuando se hace clic en el botón
if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Crear el histograma con plotly
    fig = px.histogram(car_data, x="odometer", title="Distribución del Odómetro")
    
    # Mostrar el gráfico
    st.plotly_chart(fig, use_container_width=True)




# crear una casilla de verificación
scatter_button = st.checkbox('Construir gráfico de dispersión')

# Cuando se hace clic en el botón
if scatter_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # Crear el histograma con plotly
    fig = px.scatter_3d(car_data, x="odometer", y="model_year", title="Relación entre Odómetro, precio y Año del Modelo", z="price")
    
    # Mostrar el gráfico
    st.plotly_chart(fig, use_container_width=True)