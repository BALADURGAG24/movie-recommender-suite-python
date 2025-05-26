import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split


class CollaborativeRecommender:
    def __init__(self, ratings_path='data/ratings.csv', movies_path='data/movies.csv'):
        # Load ratings and movies
        self.ratings_df = pd.read_csv(ratings_path)
        self.movies_df = pd.read_csv(movies_path)

        # Create Surprise dataset
        reader = Reader(rating_scale=(0.5, 5))
        data = Dataset.load_from_df(self.ratings_df[['userId', 'movieId', 'rating']], reader)

        # Split and train model
        trainset, _ = train_test_split(data, test_size=0.2, random_state=42)
        self.model = SVD()
        self.model.fit(trainset)

    def recommend(self, user_id, top_n=10):
        # Validate user ID
        if user_id not in self.ratings_df['userId'].unique():
            raise ValueError(f"User ID {user_id} not found in dataset.")

        # Get movies the user hasn't rated yet
        user_rated = self.ratings_df[self.ratings_df['userId'] == user_id]['movieId'].tolist()
        all_movies = self.movies_df[~self.movies_df['movieId'].isin(user_rated)].copy()

        # Predict ratings
        all_movies['est_rating'] = all_movies['movieId'].apply(
            lambda movie_id: self.model.predict(user_id, movie_id).est
        )

        # Sort and return top N recommendations
        recommended = all_movies.sort_values('est_rating', ascending=False).head(top_n)
        return recommended[['title', 'est_rating']]
