import pandas as pd

RAW_PATH = "data/booksummaries.txt"
CLEAN_PATH = "data/books_clean.csv"

# which columns should be capitalized properly
TITLE_COL = "title"
AUTHOR_COL = "author"
GENRE_COL = "genre"
DESCRIPTION_COL = "description"


df = pd.read_csv(RAW_PATH)

# basic cleaning

# remove entirely blank rows
df = df.dropna(how="all")

# strip whitespace from all string cells
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# capitalize title and author properly
if TITLE_COL in df.columns:
    df[TITLE_COL] = df[TITLE_COL].str.title()

if AUTHOR_COL in df.columns:
    df[AUTHOR_COL] = df[AUTHOR_COL].str.title()

# normalize genres (title case)
if GENRE_COL in df.columns:
    df[GENRE_COL] = df[GENRE_COL].str.title()

# replace missing descriptions
if DESCRIPTION_COL in df.columns:
    df[DESCRIPTION_COL] = df[DESCRIPTION_COL].fillna("No description available.")

# remove duplicates by title + author
df = df.drop_duplicates(subset=[TITLE_COL, AUTHOR_COL], keep="first")

# save

df.to_csv(CLEAN_PATH, index=False)

print("Cleaning complete!")
print("Saved cleaned data to:", CLEAN_PATH)
