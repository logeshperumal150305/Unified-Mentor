# Import Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Set visual style
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# Load the Dataset
file_path= "C:\\Users\\loges\\OneDrive\\Documents\\VSCodes\\PYTHON\\Unified Mentor\\Netflix Data_ Cleaning, Analysis and Visualization_ _ ML _ FA _ DA projects\\netflix1.csv"  # Replace with your actual file path
df = pd.read_csv(file_path)  # Replace with your actual file path
print(df.head())

# Data Cleaning
df.drop_duplicates(inplace=True)
df.dropna(subset=['director', 'title', 'country'], inplace=True)

# Convert 'date_added' to datetime
df['date_added'] = pd.to_datetime(df['date_added'])

# Split genres for analysis
df['genres'] = df['listed_in'].apply(lambda x: x.split(', ') if isinstance(x, str) else [])

# Feature Engineering
df['year_added'] = df['date_added'].dt.year
df['month_added'] = df['date_added'].dt.month

# Content Type Distribution
type_counts = df['type'].value_counts()
sns.barplot(x=type_counts.index, y=type_counts.values, palette='Set2')
plt.title('Distribution of Content by Type')
plt.xlabel('Type')
plt.ylabel('Count')
plt.show()

# Most Common Genres
all_genres = sum(df['genres'], [])
genre_counts = pd.Series(all_genres).value_counts().head(10)
sns.barplot(x=genre_counts.values, y=genre_counts.index, palette='Set3')
plt.title('Most Common Genres on Netflix')
plt.xlabel('Count')
plt.ylabel('Genre')
plt.show()

# Content Added Over the Years
sns.countplot(x='year_added', data=df, palette='coolwarm')
plt.title('Content Added Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Additions')
plt.xticks(rotation=45)
plt.show()

# Top Directors
top_directors = df['director'].value_counts().head(10)
sns.barplot(x=top_directors.values, y=top_directors.index, palette='Blues_d')
plt.title('Top 10 Directors by Number of Titles')
plt.xlabel('Number of Titles')
plt.ylabel('Director')
plt.show()

# Word Cloud of Movie Titles
movie_titles = df[df['type'] == 'Movie']['title']
wordcloud = WordCloud(width=800, height=400, background_color='black').generate(' '.join(movie_titles))

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Movie Titles on Netflix')
plt.show()

# Ratings Distribution
rating_counts = df['rating'].value_counts()
sns.barplot(x=rating_counts.index, y=rating_counts.values)
plt.xticks(rotation=45)
plt.title('Ratings Distribution')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()

# Monthly Releases (Movies vs. TV Shows)
monthly_movie = df[df['type'] == 'Movie']['month_added'].value_counts().sort_index()
monthly_show = df[df['type'] == 'TV Show']['month_added'].value_counts().sort_index()

plt.plot(monthly_movie.index, monthly_movie.values, label='Movies')
plt.plot(monthly_show.index, monthly_show.values, label='TV Shows')
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.xlabel('Month')
plt.ylabel('Number of Releases')
plt.legend()
plt.title('Monthly Content Releases')
plt.grid(True)
plt.show()
