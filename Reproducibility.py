import pandas as pd
from scipy.stats import chi2_contingency

file_location = 'C:\\Python310\\nyts2021.xlsx'

df = pd.read_excel(file_location, engine='openpyxl')

df['QN11L'] = df['QN11L'].fillna(0)
df['QN11A'] = df['QN11A'].fillna(0)

df['QN12L'] = df['QN12L'].fillna(0)
df['QN12A'] = df['QN12A'].fillna(0)



CrosstabResult1 = pd.crosstab(index=df['QN11L'],columns=df['QN11A'])
print(CrosstabResult1)

CrosstabResult2 = pd.crosstab(index=df['QN12L'],columns=df['QN12A'])
print(CrosstabResult2)

result1 = chi2_contingency(CrosstabResult1)
print(result1[1])

result2 = chi2_contingency(CrosstabResult2)
print(result2[1])
