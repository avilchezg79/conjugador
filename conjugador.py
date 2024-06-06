## importar
import pandas as pd
verbos = pd.read_excel('verbos.xlsx')

## diccionario
quechua = list(verbos['quechua'])
espanol = list(verbos['español'])

dict_que_esp = dict(zip(quechua, espanol))

## importar streamlit
import streamlit as st

##selección de la base
option = st.selectbox(
    'Seleccione un verbo en quechua', quechua)
st.write('Seleccionaste', option)

## selección del tiempo
tiempo = st.selectbox(
    'Elige un tiempo gramatical en quechua', ('presente simple', 'presente progresivo', 'presente habitual', 'pasado experimentado', 'pasado no experimentado'))

## selección del nro
numero = st.selectbox(
    'Seleccione un número gramatical en quechua', ('singular', 'plural'))

## selección de la persona
persona = st.selectbox(
    'Seleccione una persona gramatical en quechua', ('primera', 'segunda', 'tercera', 'cuarta (primera exclusiva)'))
