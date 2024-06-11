import pandas as pd
import os

url = "https://dados.ufrgs.br/dataset/98874d91-7c22-4c5a-bce6-5ec78de5a7d0/resource/560c7bc8-dc73-471c-80be-eba77a0de4f2/download/dadosabertos_graduacao_quantitativo-de-alunos.csv"

df = pd.read_csv(url, sep =";")

colunas = ['NomeCurso', 'Ingressantes', 'Diplomados', 'Evadidos']
df = df[colunas]

cursos = df.groupby(by = "NomeCurso",
                    axis = 0
                    ).sum()

cursos["Formados"] = cursos["Diplomados"]/cursos["Ingressantes"]
cursos["Desistentes"] = cursos["Evadidos"]/cursos["Ingressantes"]
cursos["Remanescentes"] = 1 - cursos["Formados"] - cursos["Desistentes"]

cursos = cursos.sort_values(by = "Formados",
                            ascending = False)
cursos = cursos[cursos["Formados"]<=1]

print(cursos.head())
print(cursos[["Formados", "Desistentes", "Remanescentes"]])

cursos[["Formados", "Desistentes", "Remanescentes"]].to_csv("cursos.csv", sep = ";", encoding="latin-1", decimal =',')
