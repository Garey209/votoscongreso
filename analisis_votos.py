import pandas as pd
import numpy as np

# Simular Wnominate (dummy function)
class Wnominate:
    def fit(self, votos):
        return votos.mean(axis=0)  # Solo para ilustración, no es Wnominate real

# Leer el archivo de Excel
file_path = 'Votos.xlsx'
df = pd.read_excel(file_path)

# Mapear los valores de los tipos de votos
voto_map = {
    'A FAVOR': 1,
    'EN CONTRA': -1,
    'AUSENTE': -0.5,
    'LICENCIA': 0
}

# Aplicar el mapeo a los datos
for column in df.columns[1:]:  # Suponiendo que la primera columna es el identificador del diputado
    df[column] = df[column].map(voto_map)

# Asegúrate de que no haya valores NaN después del mapeo
df.fillna(0, inplace=True)

# Separar los datos de los diputados (identificadores) y los votos
diputados = df.iloc[:, 0]
votos = df.iloc[:, 1:]

# Inicializar y ajustar el modelo W-NOMINATE (simulado)
w_nom = Wnominate()
resultados = w_nom.fit(votos)

# Imprimir los resultados
print(resultados)

