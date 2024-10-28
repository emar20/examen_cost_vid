# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 21:43:26 2024

@author: PC
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
datos= pd.read_csv('living.csv')
print(datos.info())

print(datos.columns)
print(datos.head)

nro_filas = datos.shape[0]  
nro_columnas = datos.shape[1]  
print("Número de Filas:", nro_filas)
print("Número de Columnas:", nro_columnas)

costo_vid_prom = datos["Cost of living, 2017"].mean()
print("Costo de vida promedio:", costo_vid_prom)

pais_costo_vida_mayor = datos.loc[datos["Cost of living, 2017"].idxmax(), ["Countries", "Cost of living, 2017"]]
print("País con el costo de vida más alto:", pais_costo_vida_mayor["Countries"], "-", pais_costo_vida_mayor["Cost of living, 2017"])

pais_costo_vida_menor = datos.loc[datos["Cost of living, 2017"].idxmin(), ["Countries", "Cost of living, 2017"]]
print("País con el costo de vida más bajo:", pais_costo_vida_menor["Countries"], "-", pais_costo_vida_menor["Cost of living, 2017"])

cost_vida_peru = datos[datos["Countries"] == "Peru"][["Cost of living, 2017", "Global rank"]]
if not cost_vida_peru.empty:
    print("Costo de vida en Perú:", cost_vida_peru["Cost of living, 2017"].values[0])
    print("Ranking de Perú:", cost_vida_peru["Global rank"].values[0])
else:
    print("No se encontró información para Perú")
    
top_10_vida_alto = datos.nlargest(10, "Cost of living, 2017")[["Countries", "Cost of living, 2017"]]

top_10_vida_bajo = datos.nsmallest(10, "Cost of living, 2017")[["Countries", "Cost of living, 2017"]]

cost_vida_america = datos[datos["Continent"] == "America"][["Countries", "Cost of living, 2017"]]

#Los 10 países con el costo de vida más alto

top_10_cost_of_living = datos[['Countries', 'Cost of living, 2017']].nlargest(10, 'Cost of living, 2017')

# Visualizar
plt.figure(figsize=(10, 6))
plt.barh(top_10_cost_of_living['Countries'], top_10_cost_of_living['Cost of living, 2017'], color='skyblue')
plt.xlabel('Costo de Vida')
plt.title('Top 10 Países con el Costo de Vida Más Alto')
plt.gca().invert_yaxis()
plt.show()


#Los 10 países con el costo de vida más bajo

bottom_10_cost_of_living = datos[['Countries', 'Cost of living, 2017']].nsmallest(10, 'Cost of living, 2017')

# Visualizar
plt.figure(figsize=(10, 6))
plt.barh(bottom_10_cost_of_living['Countries'], bottom_10_cost_of_living['Cost of living, 2017'], color='lightgreen')
plt.xlabel('Costo de Vida')
plt.title('Top 10 Países con el Costo de Vida Más Bajo')
plt.gca().invert_yaxis()  # Para que el país con el costo más bajo esté en la parte superior
plt.show()


# Filtrar los datos para obtener solo los países de America
america_countries = datos[datos['Continent'] == 'America'][['Countries', 'Cost of living, 2017']]

# Ordenar los países de América por costo de vida

america_countries = america_countries.sort_values(by='Cost of living, 2017', ascending=False)

# Visualizar
plt.figure(figsize=(10, 6))
plt.barh(america_countries['Countries'], america_countries['Cost of living, 2017'], color='coral')
plt.xlabel('Costo de Vida')
plt.title('Costo de Vida en los Países de America')
plt.gca().invert_yaxis()
plt.show()