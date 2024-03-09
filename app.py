"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd

@st.cache_data
def carga_marcas():
    return pd.read_csv('marcas.csv').set_index('marca')

@st.cache_data
def carga_preciario():
    return pd.read_csv('preciario.csv').set_index('Artículo')


# buscador de categoria de marcga
def buscar_categoria(marca):
  return  marcas.loc[marca,'categoria']

# buscador de precios
def buscar_precio(marca, articulo):
  return preciario.loc[articulo,buscar_categoria(marca)]

marcas = carga_marcas()
preciario = carga_preciario()

lista_marcas = sorted(list(marcas.index))
lista_articulos = sorted(list(preciario.index))


st.title('CUDECA - Buscador de precios')

marca = st.selectbox(label = 'Selecciona Marca', options = lista_marcas, key=None)
articulo = st.selectbox(label = 'Selecciona el tipo de articulo', options = lista_articulos, key=None)
st.divider()

if marca is not None and articulo is not None:
    st.write(f'Has seleccionado {marca} - {articulo}')
    col1, col2 = st.columns(2)
    with col1:
        st.header("Categoria de marca")
        st.write(f'{buscar_categoria(marca)}')

    with col2:
        st.header("Recomendacion")
        st.write(f'{buscar_precio(marca,articulo)}')
    
