import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading dataset
df = pd.read_csv("netflix_titles.csv")

# Showing basic info
print("Shape of dataset:", df.shape)
print("\nMissing values:\n", df.isnull().sum())

# Convert date column
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['year_added'] = df['date_added'].dt.year

# 1. Movies vs TV Shows
plt.figure()
sns.countplot(x='type', data=df)
plt.title("Movies vs TV Shows on Netflix")
plt.savefig("chart1.png")
plt.show()

# 2. Content added per year
year_counts = df['year_added'].value_counts().sort_index()
plt.figure()
year_counts.plot(kind='line')
plt.title("Content Growth Over Years")
plt.savefig("chart2.png")
plt.show()

# 3. Top Genres
genres = df['listed_in'].str.split(', ', expand=True).stack()
top_genres = genres.value_counts().head(10)

plt.figure()
top_genres.plot(kind='bar')
plt.title("Top Genres on Netflix")
plt.savefig("chart3.png")
plt.show()

# Insights
print("\nINSIGHTS:")
print("1. Movies dominate Netflix catalog.")
print("2. Content growth increased rapidly after 2016.")
print("3. Certain genres dominate the platform.")