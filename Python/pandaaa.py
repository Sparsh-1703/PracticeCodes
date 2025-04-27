import pandas as pd
df = pd.read_csv("MoviesData.csv")
(df.head(10))
(df.tail(10))
(df.describe())
sorting = df.sort_values(by='Release Year', ascending=True)
(sorting.head(10))
df.fillna({'Rating': df['Rating'].mean(), 'Budget (in Million $)': df['Budget (in Million $)'].mean()}, inplace=True)
df.dropna(subset=['Rating', 'Budget (in Million $)'], inplace=True)
df.at[98, 'Movie Name'] = 'Harry Potter'
df['Movie Name'] = df['Movie Name'].str.replace('The', ';-;')
print(df)