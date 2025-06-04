
# 🎬 Netflix Data Analysis & Visualization

This project performs an in-depth analysis of Netflix content using a dataset of titles available on the platform. The project covers data cleaning, exploration, and a range of visualizations to uncover trends in content type, genre, release years, and more.

---

## 📁 Dataset Overview

- **Source**: netflix1 Dataset  
- **Records**: ~8,790 entries  
- **Features**: show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in  
- **Time Span**: Titles from 1925 to 2021

---

## 🧰 Tools & Libraries Used

- Python (Pandas, NumPy)
- Seaborn & Matplotlib for Visualization
- WordCloud for visualizing frequent movie titles

---

## 🔍 Project Workflow

### 1. Data Cleaning
- Removed duplicate rows
- Dropped rows with missing `director`, `cast`, and `country`
- Converted `date_added` to datetime format

### 2. Feature Engineering
- Extracted `year_added` and `month_added` from `date_added`
- Split `listed_in` into a list of genres

### 3. Exploratory Data Analysis

- **Content Type Distribution**: Breakdown of Movies vs TV Shows
- **Genre Analysis**: Top 10 most frequent genres
- **Yearly Trends**: Number of titles added by year
- **Top Directors**: Most frequently featured directors
- **Word Cloud**: Popular movie titles
- **Ratings Distribution**: Frequency of content ratings (e.g., TV-MA, PG-13)
- **Monthly Releases**: Comparison of monthly release frequency for Movies vs TV Shows

---

## 📊 Visual Insights

- Bar plots for content type, genres, directors, and ratings
- Line plots for time-series trends
- Word cloud of movie titles
- Comparative monthly trends for movie and TV show additions

---

## 🚀 How to Run

1. Download or clone the project.
2. Install dependencies with:
   ```bash
   pip install pandas matplotlib seaborn wordcloud
   ```
3. Place `netflix_titles.csv` in the project directory.
4. Run the notebook/script in your Python IDE.

---

## 🔮 Possible Extensions

- Add NLP analysis of descriptions/titles for sentiment or category prediction
- Use clustering or association rules for genre pattern mining
- Create interactive dashboards using Streamlit or Plotly

---

## 📎 References

- Netflix Dataset: [Kaggle – Netflix Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows)
