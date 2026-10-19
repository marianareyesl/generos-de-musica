import streamlit as st
import pandas as pd 

st.title("Géneros de música")

#Dataframe#
dataframe = pd.read_csv("https://raw.githubusercontent.com/marianareyesl/generos-de-musica/main/music_genre.csv",
encoding="latin1",)

#Sidebar
sidebar = st.sidebar
#titulo de la barra
sidebar.title("Busqueda")

#Mostrar todos los generos de música#
mostrar_todos = sidebar.checkbox("Mostrar todos los datos")

if mostrar_todos:

    # Mostramos todos los datos
    st.subheader("Todos los datos")

    st.dataframe(dataframe)


# Texto que escribirá el usuario
titulo = sidebar.text_input("Nombre de la canción:")


# Botón para buscar
buscar = sidebar.button("Buscar canción")


if buscar:

    # Buscamos la canción dentro de la columna
    resultado = dataframe[
        dataframe["track_name"].str.contains(titulo, case=False, na=False)
    ]

    st.subheader("Canción buscada")

    st.dataframe(resultado)


# Obtenemos los artistas del dataframe
artistas = dataframe["artist_name"].dropna().unique()


# Creamos el menú para seleccionar un género de música
artista_seleccionado = sidebar.selectbox(
    "Seleccionar artista",
    artistas
)


# BOTON
filtrar = sidebar.button("Filtrar artista")


if filtrar:

    # Filtramos las canciones del artista
    resultado = dataframe[
        dataframe["artist_name"] == artista_seleccionado
    ]

    # Mostramos las canciones
    st.subheader("Canciones del artista")

    st.dataframe(resultado)


selected_town = st.radio("Select Embark Town",
titanic_data['embark_town'].unique())
st.write("Selected Embark Town:", selected_town)


st.dataframe(dataframe)
st.write ("Hecho por:")
st.write ("Mariana Reyes Lobato ")
