import pandas as pd
import sqlalchemy as sqla
import time

start_extraction_time = time.perf_counter()
df = pd.read_csv("cnes_PR_2601.csv", sep=';')
end_extraction_time = time.perf_counter()
elapsed_extraction_time = end_extraction_time - start_extraction_time

print(f"Time taken to extract csv: {elapsed_extraction_time:.4f}s")

import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

# # Transformação
# CBO, CBOUNICO, NOMEPROF, CNS_PROF, CONSELHO, REGISTRO

# df.drop('CPF_PROF', axis=1, inplace=True)
df = df[["CBO", "CBOUNICO", "NOMEPROF", "CNS_PROF", "CONSELHO", "REGISTRO"]]

# df['CNPJ'] = df['CNPJ'].astype(str) #Formatar Cnpj?
# df['CNPJ'] = df['CNPJ'].str[:-2]
# df["CNPJ"] = df["CNPJ"].fillna("(N/D)")


# print(df.isnull().sum())
# CBO             0
# CBOUNICO    95479
# NOMEPROF        0
# CNS_PROF        0
# CONSELHO    86289
# REGISTRO    85936 

df["CBOUNICO"] = df["CBOUNICO"].fillna("(N/D)")
df["CONSELHO"] = df["CONSELHO"].fillna("(N/D)")
df["REGISTRO"] = df["REGISTRO"].fillna("(N/D)")
print(df.isna().sum()) 
# CBO             0
# CBOUNICO    95479
# NOMEPROF        0
# CNS_PROF        0
# CONSELHO    86289
# REGISTRO    85936


# # Data frame tratado
# print(df.head())
# print(df.info())