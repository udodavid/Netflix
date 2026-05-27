# ============================================
# Netflix Movie Data Analysis Project
# Dataset: mymoviedb.csv
# ============================================

import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------
# Load Dataset
# --------------------------------------------
def load_data(file_path):
    try:
        df = pd.read_csv(file_path, engine='python')
        print("Dataset loaded successfully.\n")
        return df
    except Exception as e:
        print("Error loading dataset:", e)
        return None

# --------------------------------------------
# Explore Dataset
# --------------------------------------------
def explore_data(df):
    print("First 5 rows:\n", df.head(), "\n")
    print("Columns:\n", df.columns, "\n")
    print("Summary:\n", df.describe(), "\n")

# --------------------------------------------
# Clean Data
# --------------------------------------------
def clean_data(df):
    df = df.drop_duplicates()
    df = df.dropna()

    # Convert columns to correct types
    df['Vote_Average'] = pd.to_numeric(df['Vote_Average'], errors='coerce')
    df['Popularity'] = pd.to_numeric(df['Popularity'], errors='coerce')

    # Drop rows that became NaN after conversion
    df = df.dropna(subset=['Vote_Average', 'Popularity'])

    print("Data cleaned.\n")
    return df
    #print(df.dtypes)

# --------------------------------------------
# Top Rated Movies
# --------------------------------------------
def top_rated_movies(df):
    top_movies = df.sort_values(by='Vote_Average', ascending=False).head(10)
    print("Top 10 Highest Rated Movies:\n")
    print(top_movies[['Title', 'Vote_Average']], "\n")
    return top_movies

# --------------------------------------------
# Popularity vs Rating
# --------------------------------------------
def popularity_vs_rating(df):
    correlation = df['Popularity'].corr(df['Vote_Average'])
    print("Correlation between popularity and rating:", correlation, "\n")
    if correlation > 0.5:
        print("Strong positive relationship between popularity and ratings.")
    elif correlation > 0:
        print("Weak positive relationship between popularity and ratings.")
    else:
        print("No significant relationship or negative correlation.")
    return correlation

# --------------------------------------------
# Movies Per Year
# --------------------------------------------
def movies_per_year(df):
    df['Release_Year'] = pd.to_datetime(df['Release_Date']).dt.year
    yearly = df.groupby('Release_Year').size()
    print("Movies released per year:\n", yearly, "\n")
    return yearly

# --------------------------------------------
# Average Rating
# --------------------------------------------
def average_rating(df):
    avg = df['Vote_Average'].mean()
    print("Average Movie Rating:", avg, "\n")
    return avg

# --------------------------------------------
# Filter Popular Movies
# --------------------------------------------
def filter_popular_movies(df):
    avg_popularity = df['Popularity'].mean()
    popular = df[df['Popularity'] > avg_popularity]
    print("Movies above average popularity:\n")
    print(popular[['Title', 'Popularity']].head(), "\n")
    return popular

# --------------------------------------------
# Movies by Language
# --------------------------------------------
def movies_by_language(df):
    language_count = df['Original_Language'].value_counts()
    print("Movies by language:\n", language_count.head(), "\n")
    return language_count

# --------------------------------------------
# Plot Top Movies
# --------------------------------------------
def plot_top_movies(df):
    top_movies = df.sort_values(by='Vote_Average', ascending=False).head(10)
    plt.figure()
    plt.barh(top_movies['Title'], top_movies['Vote_Average'])
    plt.xlabel("Rating")
    plt.ylabel("Movie Title")
    plt.title("Top 10 Highest Rated Movies")
    plt.gca().invert_yaxis()
    plt.show()

# --------------------------------------------
# Plot Movies Per Year
# --------------------------------------------
def plot_movies_per_year(yearly):
    plt.figure()
    yearly.plot(kind='line')
    plt.title("Movies Released Per Year")
    plt.xlabel("Year")
    plt.ylabel("Number of Movies")
    plt.show()

# --------------------------------------------
# Plot Popularity vs Rating
# --------------------------------------------
def plot_popularity_vs_rating(df):
    plt.figure()
    plt.scatter(df['Popularity'], df['Vote_Average'])
    plt.xlabel("Popularity")
    plt.ylabel("Rating")
    plt.title("Popularity vs Rating")
    plt.show()

# --------------------------------------------
# Main Function
# --------------------------------------------
def main():
    file_path = "data/mymoviedb.csv"

    df = load_data(file_path)

    if df is not None:
        explore_data(df)

        df = clean_data(df)

        # Analysis
        top_movies = top_rated_movies(df)
        correlation = popularity_vs_rating(df)
        yearly = movies_per_year(df)
        avg_rating = average_rating(df)
        popular_movies = filter_popular_movies(df)
        language_data = movies_by_language(df)

        # Plots
        plot_top_movies(df)
        plot_movies_per_year(yearly)
        plot_popularity_vs_rating(df)

# Run Program
if __name__ == "__main__":
    main()