from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

class MovieRecommender:
    def __init__(self, df, tfidf_matrix):
        self.df = df
        self.tfidf_matrix = tfidf_matrix
        self.similarity = cosine_similarity(tfidf_matrix)

    def recommend(self, movie_title, top_n=10):
        indices = pd.Series(self.df.index, index=self.df['title']).drop_duplicates()

        if movie_title not in indices:
            raise ValueError(f"Movie '{movie_title}' not found in dataset.")

        idx = indices[movie_title]
        sim_scores = list(enumerate(self.similarity[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
        movie_indices = [i[0] for i in sim_scores]

        return self.df.iloc[movie_indices][['title']]