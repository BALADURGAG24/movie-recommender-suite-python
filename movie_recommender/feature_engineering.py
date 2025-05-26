from sklearn.feature_extraction.text import TfidfVectorizer

def preprocess_overview(df):
    # Rename function or adapt it, for example:
    df['genres'] = df['genres'].fillna('')
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['genres'])
    return tfidf_matrix
