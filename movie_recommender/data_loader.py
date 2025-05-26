import os
import pandas as pd

def load_movie_data():
    base_dir = os.path.dirname(os.path.dirname(__file__))  # Go up to project root
    file_path = os.path.join(base_dir, "data", "movies.csv")
    return pd.read_csv(file_path)
