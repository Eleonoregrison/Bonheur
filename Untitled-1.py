import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('DataForTable2.1WHR2023 (1).xls')

# Normalisation des colonnes pour n'avoir que des indices entre 0 et 1
df['Life Ladder']=df['Life Ladder']/10
df['Log GDP per capita']=df['Log GDP per capita']/df['Log GDP per capita'].max()
df['Healthy life expectancy at birth']=df['Healthy life expectancy at birth']/100
df['Generosity']=df['Generosity'] + 0.5 - df['Generosity'].median()
df['Generosity']=df['Generosity']/df['Generosity'].max()
df.drop(columns=['year'])

# On moyenne sur les différentes années 
df.set_index('Country name')
df1 = df.groupby(by=df['Country name']).mean()

# On calcule notre indice de bonheur avec la formule suivante
df1['Indice'] = (0.2*df1['Life Ladder']+0.15*df1['Log GDP per capita']+ 0.1* df1['Social support'] + 0.1*df1['Healthy life expectancy at birth'] + 0.15*df1['Freedom to make life choices'] + 0.05*df1['Generosity'] + 0.05*df1['Perceptions of corruption'] + 0.1*df1['Positive affect'] + 0.1*df1['Negative affect'])/9

# On trie les pays selon cet indice (on remarque qu'on a un problème pour certains pays qui n'ont pas rempli certains critères)
df1.sort_values(by = ['Indice'], ascending = False)

#On représente graphiquement le classement des pays les plus heureux (en arc-en-ciel parce que c'est beau)
df3 = df2.head(9)
x = df3.index
y = df3['Indice']
plt.title('Pays les plus heureux')
couleurs = ['red', 'orange', 'salmon', 'pink', 'yellow', 'green', 'skyblue', 'blue', 'purple']
plt.bar(x,y, width = 0.06, color = couleurs)
plt.ylim(0.075,0.0875)
plt.xticks(rotation=90)
plt.show()