# -*- coding: utf-8 -*-
## Importar librerías

import pandas as pd
import streamlit as st

###############################################
###############################################

## Preparación de archivos

verbos = open('verbos.xlsx')
verbos = pd.read_excel('verbos.xlsx')
tiyay = open('tiyay.xlsx')
tiyay = pd.read_excel('tiyay.xlsx')
tiyay = pd.ExcelFile('tiyay.xlsx')

## CONJUGADOR ##
## Diccionario para los pronombres
## Creo un ciclo for que lea solo la hoja en la que coloqué los pronombres y la convierta a diccionario

pronombre = pd.read_excel('tiyay.xlsx', sheet_name = 'pronombres')
col = pronombre.columns
pronombre.set_index(col[0], inplace = True)
dict_pronombres = pronombre.to_dict()

## Diccionario para los sufijos

D = {}

for hoja in tiyay.sheet_names:
  df = pd.read_excel('tiyay.xlsx', sheet_name = hoja)
  c = df.columns
  df.set_index(c[0], inplace = True)
  print(f'Hoja: {hoja}')
  print(df.head())

  d = df.to_dict()
  D[hoja] = d

## Función para conjugar la base
## Se llegará al sufijo "abriendo" las distintas entradas en el orden según el que aparecen en el diccionario (tiempo > nro > persona)

def conjuga(base, tiempo, numero, persona):
    return str(dict_pronombres[numero][persona]) + ' ' + base + str(D[tiempo][numero][persona])

## Diccionario para los verbos
  
quechua = list(verbos['quechua'])
espanol = list(verbos['espanol'])

dict_que_esp = dict(zip(quechua, espanol))

###############################################
###############################################

## CONJUGADOR INVERSO ##
## Objetivo: Guardar todas las conjugaciones posibles en un excel

tiempos = ['presente simple', 'presente progresivo', 'presente habitual', 'pasado experimentado simple', 'pasado experimentado progresivo', 'pasado experimentado habitual', 'pasado no experimentado simple', 'pasado no exp. progresivo', 'pasado no exp. habitual']
numeros = ['singular', 'plural']
personas = ['primera', 'segunda', 'tercera', 'cuarta']

## Lista para agregar todas las combinaciones

conjugaciones = []

for base in quechua:
  for tiempo in tiempos:
    for numero in numeros:
      for persona in personas:
        conjugacion = conjuga(base, tiempo, numero, persona)
        conjugaciones.append({
                    'Raíz verbal quechua': base,
                    'Raiz verbal español': dict(zip(quechua, espanol))[base],
                    'Persona': persona,
                    'Número': numero,
                    'Tiempo': tiempo,
                    'Conjugación': conjugacion
                })

###############################################
###############################################

## INTERFAZ EN STREAMLIT ##
## Título usando CSS para cambiar la fuente del título
        
st.markdown(
    """
    <style>
    .comic-font {
        font-family: 'Garamond', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título con la clase CSS personalizada
st.markdown('<h1 class="comic-font">Conjugador de verbos en quechua</h1>', unsafe_allow_html=True)

st.write('**Juega con las distintas maneras de conjugar verbos en quechua y conoce más sobre su morfología** ✏️')

## seleccion de la base
base = st.selectbox(
    'Selecciona un verbo en quechua', quechua)
st.write('Seleccionaste ' + base + ', que en español es "' + dict_que_esp[base] + '".')

## imagenes
imagenes = {'tiyay': 'tiyay.jpg', 'mikuy': 'mikuy.jpg', 'puri': 'puri.jpg', 'tusuy': 'tusuy.jpg'}
imagen_seleccionada = imagenes[base]
st.image(imagen_seleccionada)

## seleccion del tiempo
tiempo = st.selectbox(
    'Selecciona un tiempo gramatical en quechua', ('presente simple', 'presente progresivo', 'presente habitual', 'pasado experimentado simple', 'pasado experimentado progresivo', 'pasado experimentado habitual', 'pasado no experimentado simple', 'pasado no exp. progresivo', 'pasado no exp. habitual'))

explicacion = {'presente simple': 'En el quechua, este es el tiempo no recibe una marca explícita. Por ende, aquí solo agregamos las marcas de persona a la raíz verbal.', 'presente progresivo': 'Este tiempo se emplea cuando nos referimos a eventos que están ocurriendo mientras dicha oración es pronunciada. Aquí anteponemos la marca -chka.', 'presente habitual': 'Utilizamos este tiempo cuando el evento descrito es cotidiano, es decir, cuando se realiza con cierta regularidad. Aquí añadiremos el sufijo –q al verbo principal y emplearemos el verbo ser, kay, conjugado en presente simple, a manera de auxiliar.', 'pasado experimentado simple': 'Esta forma de pasado se emplea cuando narramos hechos de los cuales hemos sido testigos directos, es decir, hechos que nos constan. Para formularlo, agregamos el sufijo -rqa a la raíz verbal.', 'pasado experimentado progresivo': 'Además de ser testigos directos de los hechos, esta forma de pasado refiere a eventos que estaban en progreso en un periodo determinado del pasado. A -rqa debemos anteponerle la marca progresiva -chka.', 'pasado experimentado habitual': 'Este tiempo refiere a los eventos pasados de los que hemos sido testigos directos. Además, se utiliza para describir hechos cotidianos, es decir, que fueron realizados con cierta regularidad. Por ello, antes de la marca -rqa, añadimos el sufijo -q al verbo principal y el verbo ser, kay, conjugado en presente simple, a manera de auxiliar.', 'pasado no experimentado simple': 'Esta forma de pasado se emplea cuando se quiere hablar de hechos de los cuales no hemos sido testigos directos, es decir hechos sobre los cuales no estamos seguros porque no nos constan. Para formularlo, agregamos el sufijo -sqa a la raíz verbal.', 'pasado no exp. progresivo': 'Además de ser testigos no directos de los hechos, esta forma de pasado refiere a eventos que estaban en progreso en un periodo determinado del pasado. A -sqa debemos anteponerle la marca progresiva -chka.', 'pasado no exp. habitual': 'Este tiempo refiere a los eventos pasados de los que no hemos sido testigos directos. Además, se utiliza para describir hechos cotidianos, es decir, que fueron realizados con cierta regularidad. Por ello, antes de la marca -sqa, añadimos el sufijo -q al verbo principal y el verbo ser, kay, conjugado en presente simple, a manera de auxiliar.'}

with st.popover("💭 Acerca de este tiempo gramatical"):
    st.markdown(explicacion[tiempo])

## seleccion del nro
numero = st.selectbox(
    'Selecciona un numero gramatical en quechua', ('singular', 'plural'))

## seleccion de la persona
persona = st.selectbox(
    'Selecciona una persona gramatical en quechua', ('primera', 'segunda', 'tercera', 'cuarta'))

if st.button('Resultado'):
  if numero == 'singular' and persona == 'cuarta':
      st.write('No existe la cuarta persona (primera exclusiva) en quechua.')
  else:
      st.write('El verbo conjugado es ' + pronombre(tiempo, numero, persona) + ' ' + conjuga(base, tiempo, numero, persona) + '.')


