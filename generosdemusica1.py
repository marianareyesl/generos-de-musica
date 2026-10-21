import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

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

#sidebar boton para seleccionar una opcion
selected_music_genre = st.sidebar.radio(
    "Selecciona un género de música",
    dataframe['music_genre'].unique()
)
st.write("Género de música seleccionado:", selected_music_genre)

datos_filtrados = dataframe[dataframe['music_genre'] == selected_music_genre]
st.dataframe(datos_filtrados)

#boton delizante
optionals = st.expander("Optional Configurations", True)
popularity_min = optionals.slider(
"Popularidad minima",
min_value=float(dataframe['popularity'].dropna().min()),
max_value=float(dataframe['popularity'].dropna().max())
)
popularity_max = optionals.slider(
"Popularidad máxima",
min_value=float(dataframe['popularity'].dropna().min()),
max_value=float(dataframe['popularity'].dropna().max())
)

subset_popularity = datos_filtrados[
    (datos_filtrados['popularity'] <= popularity_max) &
    (popularity_min <= datos_filtrados['popularity'])
]

st.dataframe(subset_popularity)

st.dataframe(dataframe)

#grafica 1 histograma
fig, ax = plt.subplots()
ax.hist(dataframe.danceability.dropna())
st.header("Histograma Géneros de música")
st.pyplot(fig)

#grafica 2
fig3, ax3 = plt.subplots()
ax3.scatter(dataframe.popularity, dataframe.duration_ms)
ax3.set_xlabel("Popularidad")
ax3.set_ylabel("Duración")
st.header("Popularidad vs duración")
st.pyplot(fig3)

#grafica 3
clases = dataframe["danceability"].value_counts().sort_index()
fig5, ax5 = plt.subplots()
clases.plot(kind="line", marker="o", ax=ax5)
ax5.set_title("Bailabilidad de la música")
ax5.set_xlabel("Bailabilidad")
ax5.set_ylabel("Cantidad de canciones")
st.header("Gráfica de Líneas: Frecuencia de Bailabilidad")
st.pyplot(fig5)

st.write ("Acerca de:")
st.write ("Mariana Reyes Lobato ")
st.write ("Matrícula: S26004566")

#mapa de mi ciudad
map_data = pd.DataFrame(
np.random.randn(100, 2) / [50, 50] + [18.85685, -97.10926],
columns=['lat', 'lon'])

st.map(map_data)
