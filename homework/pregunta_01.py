"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

import pandas as pd

rutaarch = "files/input/clusters_report.txt"

raw_data = pd.read_fwf(rutaarch, widths=[7, 16, 17, 100], names=["Cluster", "Cantidad de palabras clave", "Porcentaje de palabras clave", "Principales palabras clave"], skiprows=4  )


consolidated_data = []
current_cluster = None

for _, row in raw_data.iterrows():
    if not pd.isna(row["Cluster"]): 
        if current_cluster:
            consolidated_data.append(current_cluster)
        current_cluster = {
            "Cluster": int(row["Cluster"]),
            "Cantidad de palabras clave": int(row["Cantidad de palabras clave"]),
            "Porcentaje de palabras clave": row["Porcentaje de palabras clave"],
            "Principales palabras clave": row["Principales palabras clave"].strip()
        }
    else:  
        current_cluster["Principales palabras clave"] += " " + row["Principales palabras clave"].strip()


if current_cluster:
    consolidated_data.append(current_cluster)


df_clusters = pd.DataFrame(consolidated_data)
df_clusters.columns = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave']
df_clusters['porcentaje_de_palabras_clave'] = df_clusters['porcentaje_de_palabras_clave'].str.replace('%', '').str.replace(',', '.').astype(float, errors='ignore')

df_clusters["principales_palabras_clave"] = (
        df_clusters["principales_palabras_clave"]
        .str.replace(r'\s+', ' ', regex=True)  
        .str.replace(r',\s+', ', ') 
        .str.strip()  # Q
        .str.replace(".", "")
    ) 

#print(df_clusters.principales_palabras_clave.to_list()[0])
def pregunta_01():
  return df_clusters