import streamlit as st
import pandas as pd

# DATA DE GOOGLE SHEETS
csv_url = 'https://docs.google.com/spreadsheets/d/{key}/export?format=csv&gid={gid}'
key = '1YL0nCg1JmwXOC25kymnRPVE7isqOIEI5'

@st.cache_data
def carga_marcas():
   gid = '496417927'
   marcas_df = pd.read_csv(csv_url.format(key=key, gid=gid))
   return marcas_df.set_index('Marca')

@st.cache_data
def carga_preciario():
   gid = '1152069563'
   preciario_df = pd.read_csv(csv_url.format(key=key, gid=gid))
   return preciario_df.set_index('Artículo')

# Cargando la data
marcas = carga_marcas()
preciario = carga_preciario()

# Generando listas para dropdown
lista_marcas = sorted(list(marcas.index))
lista_articulos = sorted(list(preciario.index))

def buscar_categoria(marca):
   return marcas.loc[marca, 'Categoria']

def buscar_precio(marca, articulo):
   return preciario.loc[articulo, buscar_categoria(marca)]

# Callback functions for buttons
def on_click_busca():
   st.session_state['show_results'] = True
   st.session_state['selected_marca'] = st.session_state['marca']
   st.session_state['selected_articulo'] = st.session_state['articulo']

def on_click_busca_otro():
   st.session_state['show_results'] = False

# Initialize session state variables
if 'show_results' not in st.session_state:
   st.session_state['show_results'] = False
if 'marca' not in st.session_state:
   st.session_state['marca'] = lista_marcas[0]
if 'articulo' not in st.session_state:
   st.session_state['articulo'] = lista_articulos[0]

# APP DISPLAY
st.header('CUDECA', divider='rainbow')

# Show initial selection interface
if not st.session_state['show_results']:
   st.title('Buscador de precios')
   st.session_state['marca'] = st.selectbox(label='Selecciona Marca', options=lista_marcas, index=lista_marcas.index(st.session_state['marca']))
   st.session_state['articulo'] = st.selectbox(label='Selecciona el tipo de articulo', options=lista_articulos, index=lista_articulos.index(st.session_state['articulo']))
   if st.button('Encuéntralo', on_click=on_click_busca):
       pass
else:
   # Show results and the new button
   st.title('Resultado')
   st.write(f'Has seleccionado {st.session_state["selected_marca"]} - {st.session_state["selected_articulo"]}')
   col1, col2 = st.columns(2)
   with col1:
       st.header(f':green[{buscar_categoria(st.session_state["selected_marca"])}]')

   with col2:
       st.header(f':green[{buscar_precio(st.session_state["selected_marca"], st.session_state["selected_articulo"])}]')

   if st.button('Busca otro articulo', on_click=on_click_busca_otro):
       pass
