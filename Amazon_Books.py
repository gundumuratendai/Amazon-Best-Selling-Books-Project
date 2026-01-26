import pandas as pd

books = pd.read_csv('bestsellers.csv')
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
print(books.head(20))
print(books.shape)
print(books.columns)
print(books.describe())

books.drop_duplicates(inplace=True)
books.rename(columns={'Name': 'Title', 'Year': 'Publication Year', 'User Rating': 'Rating'}, inplace=True)

print(books.columns)
print(books.head())

books['Price'] = books['Price'].astype(float)
print(books.columns)
print(books.head(30))
author_counts = books['Author'].value_counts()
print(author_counts)
avg_rating_by_genre = books.groupby("Genre")["Rating"].mean()
print(avg_rating_by_genre)

author_counts.head(10).to_csv("bestsellers.csv")
avg_rating_by_genre.to_csv("avg_rating_by_genre.csv")



