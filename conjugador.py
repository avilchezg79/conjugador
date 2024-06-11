# -*- coding: utf-8 -*-
## importar
import pandas as pd
verbos = pd.read_excel('verbos.xlsx')

###############################################
###############################################

## archivo

tiyay = pd.ExcelFile('tiyay.xlsx')

## Diccionario para los pronombres
## Creo un ciclo for que lea solo la hoja en la que coloqué los pronombres y la convierta a diccionario

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

## Función para conjugar la base
## Se llegará al sufijo "abriendo" las distintas entradas en el orden según el que aparecen en el diccionario (tiempo > nro > persona)

vocales = ['a', 'i', 'u']

def conjuga(base, tiempo, numero, persona):
    if base[-1] not in vocales:
      base = base[:-1]
    return base + D[tiempo][numero][persona]

## Función para agregar el pronombre
## Sigue la misma lógica que la función anterior

def pronombre(tiempo, numero, persona):
    return P[tiempo][numero][persona]

###############################################
###############################################

## diccionario
quechua = list(verbos['quechua'])
espanol = list(verbos['espanol'])

dict_que_esp = dict(zip(quechua, espanol)) ## diccionario del excel 'verbos'

## importar streamlit
import streamlit as st

## titulo
st.title(':rainbow[Conjugador de verbos en quechua]')
st.write('**Juega con las distintas maneras de conjugar verbos en quechua y conoce más sobre su morfología** ✏️')

##seleccion de la base
base = st.selectbox(
    ':violet[Seleccione un verbo en quechua]', quechua)
st.write('Seleccionaste ' + base + ', que en español es "' + dict_que_esp[base] + '".')

## seleccion del tiempo
tiempo = st.selectbox(
    ':red[Seleccione un tiempo gramatical en quechua]', ('presente simple', 'presente progresivo', 'presente habitual', 'pasado experimentado simple', 'pasado experimentado progresivo', 'pasado experimentado habitual', 'pasado no experimentado simple', 'pasado no exp. progresivo', 'pasado no exp. habitual'))

explicacion = {'presente simple': 'En el quechua, este es el tiempo no recibe una marca explícita. Por ende, aquí solo agregamos las marcas de persona a la raíz verbal.', 'presente progresivo': 'Este tiempo se emplea cuando nos referimos a eventos que están ocurriendo mientras dicha oración es pronunciada. Aquí anteponemos la marca -chka.', 'presente habitual': 'Utilizamos este tiempo cuando el evento descrito es cotidiano, es decir, cuando se realiza con cierta regularidad. Aquí añadiremos el sufijo –q al verbo principal y emplearemos el verbo ser, kay, conjugado en presente simple, a manera de auxiliar.', 'pasado experimentado simple': 'Esta forma de pasado se emplea cuando narramos hechos de los cuales hemos sido testigos directos, es decir, hechos que nos constan. Para formularlo, agregamos el sufijo -rqa a la raíz verbal.', 'pasado experimentado progresivo': 'Además de ser testigos directos de los hechos, esta forma de pasado refiere a eventos que estaban en progreso en un periodo determinado del pasado. A -rqa debemos anteponerle la marca progresiva -chka.', 'pasado experimentado habitual': 'Este tiempo refiere a los eventos pasados de los que hemos sido testigos directos. Además, se utiliza para describir hechos cotidianos, es decir, que fueron realizados con cierta regularidad. Por ello, antes de la marca -rqa, añadimos el sufijo -q al verbo principal y el verbo ser, kay, conjugado en presente simple, a manera de auxiliar.', 'pasado no experimentado simple': 'Esta forma de pasado se emplea cuando se quiere hablar de hechos de los cuales no hemos sido testigos directos, es decir hechos sobre los cuales no estamos seguros porque no nos constan. Para formularlo, agregamos el sufijo -sqa a la raíz verbal.', 'pasado no exp. progresivo': 'Además de ser testigos no directos de los hechos, esta forma de pasado refiere a eventos que estaban en progreso en un periodo determinado del pasado. A -sqa debemos anteponerle la marca progresiva -chka.', 'pasado no exp. habitual': 'Este tiempo refiere a los eventos pasados de los que no hemos sido testigos directos. Además, se utiliza para describir hechos cotidianos, es decir, que fueron realizados con cierta regularidad. Por ello, antes de la marca -sqa, añadimos el sufijo -q al verbo principal y el verbo ser, kay, conjugado en presente simple, a manera de auxiliar.'}

with st.popover("💭 Acerca de este tiempo gramatical"):
    st.markdown(explicacion[tiempo])

## seleccion del nro
numero = st.selectbox(
    ':green[Seleccione un numero gramatical en quechua]', ('singular', 'plural'))

## seleccion de la persona
persona = st.selectbox(
    ':blue[Seleccione una persona gramatical en quechua]', ('primera', 'segunda', 'tercera', 'cuarta'))

if numero == 'singular' and persona == 'cuarta':
    st.write('No existe la cuarta persona (primera exclusiva) en quechua.')
else:
    st.write('El verbo conjugado es ' + pronombre(tiempo, numero, persona) + ' ' + conjuga(base, tiempo, numero, persona) + '.')


