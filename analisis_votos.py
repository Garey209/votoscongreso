import pandas as pd
import numpy as np

# Simular Wnominate (dummy function)
class Wnominate:
    def fit(self, votos):
        print("Ejecutando W-NOMINATE fit function")  # Añadido
        return votos.mean(axis=0)  # Solo para ilustración, no es Wnominate real

print("Leyendo el archivo de Excel...")  # Añadido
# Leer el archivo de Excel
file_path = 'Votos.xlsx'
df = pd.read_excel(file_path)

print("Archivo de Excel leído correctamente.")  # Añadido

# Mapear los valores de los tipos de votos
voto_map = {
    'A FAVOR': 1,
    'EN CONTRA': -1,
    'AUSENTE': -0.5,
    'LICENCIA': 0
}

print("Aplicando el mapeo a los datos...")  # Añadido
# Aplicar el mapeo a los datos
for column in df.columns[1:]:  # Suponiendo que la primera columna es el identificador del diputado
    df[column] = df[column].map(voto_map)

print("Rellenando valores NaN...")  # Añadido
# Asegúrate de que no haya valores NaN después del mapeo
df.fillna(0, inplace=True)

print("Separando datos de identificadores y votos...")  # Añadido
# Separar los datos de los diputados (identificadores) y los votos
diputados = df.iloc[:, 0]
votos = df.iloc[:, 1:]

print("Inicializando el modelo W-NOMINATE (simulado)...")  # Añadido
# Inicializar y ajustar el modelo W-NOMINATE (simulado)
w_nom = Wnominate()
resultados = w_nom.fit(votos)

print("Resultados del análisis:")  # Añadido
# Imprimir los resultados
print(resultados)
