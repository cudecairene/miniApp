"""
# My first app
"""
# Libraries
import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection


# DATA DE GOOGLE SHEETS
csv_url = 'https://docs.google.com/spreadsheets/d/{key}/export?format=csv&gid={gid}'
key = '1YL0nCg1JmwXOC25kymnRPVE7isqOIEI5'

# Arrancando connector
conn = st.connection("gsheets", type=GSheetsConnection)

# Funciones cacheadas
@st.cache_data
def carga_marcas():
    gid = '496417927'
    marcas_df = pd.read_csv(csv_url.format(key = key, gid = gid))
    return marcas_df.set_index('Marca')

@st.cache_data
def carga_preciario():
    gid = '1152069563'
    preciario_df = pd.read_csv(csv_url.format(key = key, gid = gid))
    return preciario_df.set_index('Artículo')


# Cargando la data
marcas = carga_marcas()
preciario = carga_preciario()

# Generando listas para dropdown
lista_marcas = sorted(list(marcas.index))
lista_articulos = sorted(list(preciario.index))


# OTRAS FUNCIONES

# buscador de categoria de marcga
def buscar_categoria(marca):
  return  marcas.loc[marca,'Categoria']

# buscador de precios
def buscar_precio(marca, articulo):
  return preciario.loc[articulo,buscar_categoria(marca)]


# APP DISPLAY

st.header(':blue[CUDECA] :sunglasses:', divider='rainbow')
st.title('Buscador de precios')

marca = st.selectbox(label = 'Selecciona Marca', options = lista_marcas, key=None)
articulo = st.selectbox(label = 'Selecciona el tipo de articulo', options = lista_articulos, key=None)
busca = st.button('Busca')

if busca:
    st.divider()
    st.write(f'Has seleccionado {marca} - {articulo}')
    col1, col2 = st.columns(2)
    with col1:
        st.write("Categoria de marca")
        st.header(f'{buscar_categoria(marca)}')

    with col2:
        st.write("Recomendacion")
        st.header(f'{buscar_precio(marca,articulo)}')
  

