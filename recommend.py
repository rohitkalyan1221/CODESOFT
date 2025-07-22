import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


df = pd.read_csv("movies.csv")

# Combine genre and keywords for content-based filtering
df["combined_features"] = df["genre"].fillna('') + " " + df["keywords"].fillna('')

# Convert text to feature vectors
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df["combined_features"])

# Compute cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Movie title to index mapping
indices = pd.Series(df.index, index=df['title']).drop_duplicates()

def recommend(title, top_n=5):
    if title not in indices:
        print(" Movie not found.")
        return
    
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
    movie_indices = [i[0] for i in sim_scores]
    
    print(f"\n Recommendations for '{df['title'][idx]}':")
    for i in df['title'].iloc[movie_indices]:
        print(" -", i)

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    print(" Welcome to the Movie Recommender System!")
    while True:
        user_input = input("\nEnter a movie title (or type 'exit' to quit): ").strip()
        if user_input.lower() == 'exit':
            print(" Exiting the recommender. Goodbye!")
            break
        recommend(user_input)    