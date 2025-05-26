import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from movie_recommender.data_loader import load_movie_data
from movie_recommender.feature_engineering import preprocess_overview
from movie_recommender.content_recommender import MovieRecommender


@st.cache_resource
def load():
    df = load_movie_data()
    tfidf_matrix = preprocess_overview(df)
    return MovieRecommender(df, tfidf_matrix)

recommender = load()

st.title("🎬 Movie Recommender (Streamlit)")
movie_title = st.text_input("Enter a movie title:")

if st.button("Recommend", key="recommend_button"):
    try:
        recommendations = recommender.recommend(movie_title)
        st.subheader("Top Recommendations:")
        for title in recommendations['title']:
            st.markdown(f"- {title}")
    except ValueError as e:
        st.error(str(e))
