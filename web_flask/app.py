from flask import Flask, render_template, request
from movie_recommender.data_loader import load_movie_data
from movie_recommender.feature_engineering import preprocess_overview
from movie_recommender.content_recommender import MovieRecommender

app = Flask(__name__)

df = load_movie_data()
tfidf_matrix = preprocess_overview(df)
recommender = MovieRecommender(df, tfidf_matrix)

@app.route('/', methods=['GET', 'POST'])
def home():
    recommendations = []
    movie_title = ''
    if request.method == 'POST':
        movie_title = request.form['movie']
        try:
            result_df = recommender.recommend(movie_title)
            recommendations = result_df['title'].tolist()
        except ValueError as e:
            recommendations = [str(e)]
    return render_template('index.html', recommendations=recommendations, movie=movie_title)

if __name__ == '__main__':
    app.run(debug=True)