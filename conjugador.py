## importar
import pandas as pd
verbos = pd.read_excel('verbos.xlsx')

###############################################
###############################################

## archivo

tiyay = pd.ExcelFile('tiyay.xlsx')

## Diccionario para los pronombres
## Creo un ciclo for que lea solo la hoja en la que coloqu� los pronombres y la convierta a diccionario

P = {}

for hoja in tiyay.sheet_names:
  pf = pd.read_excel('tiyay.xlsx', sheet_name = "pronombres")
  pf = pf.set_index(['Unnamed: 0'])
  p = pf.to_dict()
  P[hoja] = p

## Diccionario para los sufijos

D = {}

for hoja in tiyay.sheet_names:
  df = pd.read_excel('tiyay.xlsx', sheet_name = hoja)
  df = df.set_index(['Unnamed: 0'])
  d = df.to_dict()
  D[hoja] = d

## Funci�n para conjugar la base
## Se llegar� al sufijo "abriendo" las distintas entradas en el orden seg�n el que aparecen en el diccionario (tiempo > nro > persona)

def conjuga(base, tiempo, numero, persona):
    return base + D[tiempo][numero][persona]

## Funci�n para agregar el pronombre
## Sigue la misma l�gica que la funci�n anterior

def pronombre(tiempo, numero, persona):
    return P[tiempo][numero][persona]

###############################################
###############################################

## diccionario
quechua = list(verbos['quechua'])
espanol = list(verbos['español'])

dict_que_esp = dict(zip(quechua, espanol))

## importar streamlit
import streamlit as st

##seleccion de la base
base = st.selectbox(
    'Seleccione un verbo en quechua', quechua)
st.write('Seleccionaste', base)

## seleccion del tiempo
tiempo = st.selectbox(
    'Elige un tiempo gramatical en quechua', ('presente simple', 'presente progresivo', 'presente habitual', 'pasado experimentado', 'pasado no experimentado'))

## seleccion del nro
numero = st.selectbox(
    'Seleccione un número gramatical en quechua', ('singular', 'plural'))

## seleccion de la persona
persona = st.selectbox(
    'Seleccione una persona gramatical en quechua', ('primera', 'segunda', 'tercera', 'cuarta (primera exclusiva)'))

st.write('El verbo conjugado es', pronombre(tiempo, numero, persona)

