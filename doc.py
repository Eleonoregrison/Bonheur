import pandas as pd
df = pd.read_excel('DataForTable2.1WHR2023 (1).xls')
df

df['Life Ladder']=df['Life Ladder']/10
df

df['Log GDP per capita'].max()

df['Log GDP per capita']=df['Log GDP per capita']/df['Log GDP per capita'].max()

df

df['Healthy life expectancy at birth']=df['Healthy life expectancy at birth']/100
df

df['Generosi

df['Generosity']=df['Generosity'] + 0.5 - df['Generosity'].median()

df

df['Generosity'].describe()

df['Generosity']=df['Generosity']/df['Generosity'].max()

df

df['Generosity'].describe()


