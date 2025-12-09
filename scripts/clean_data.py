import pandas as pd
import ast

RAW_PATH = "data/booksummaries.txt"
CLEAN_PATH = "data/books_clean.csv"

def safe_parse_genres(g):
    """Convert the weird {"/m/...": "Genre"} mapping into a comma-separated list."""
    if pd.isna(g):
        return ""
    try:
        d = ast.literal_eval(g)
        if isinstance(d, dict):
            return ", ".join(d.values())
        return ""
    except:
        return ""

# --- IMPORTANT: read the file with correct settings ---
df = pd.read_csv(
    RAW_PATH,
    sep="\t",                 # TAB-separated
    header=None,              # No header row in raw file
    names=["book_id", "freebase_id", "title", "author", "date", "genres", "summary"],
    quoting=3,                # Ignore quotes
    engine="python",          # More tolerant parser
)

# --- Clean data ---
df = df.dropna(subset=["title"])        # remove entirely empty lines
df["title"] = df["title"].str.strip()
df["author"] = df["author"].str.strip()
df["summary"] = df["summary"].fillna("").str.strip()

# genres: convert dict → comma-separated list
df["genres"] = df["genres"].apply(safe_parse_genres)

# drop duplicates
df = df.drop_duplicates(subset=["title", "author"])

# save cleaned file
df.to_csv(CLEAN_PATH, index=False)
print("Cleaned data saved to:", CLEAN_PATH)
