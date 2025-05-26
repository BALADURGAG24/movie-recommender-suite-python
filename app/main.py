def main():
    print("Select Recommendation Method:")
    print("1. Content-Based")
    print("2. Collaborative Filtering")

    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        from movie_recommender.data_loader import load_movie_data
        from movie_recommender.feature_engineering import preprocess_overview
        from movie_recommender.content_recommender import MovieRecommender

        print("\nLoading content-based model...")
        df = load_movie_data()
        tfidf_matrix = preprocess_overview(df)
        recommender = MovieRecommender(df, tfidf_matrix)

        while True:
            title = input("\nEnter movie title (or 'exit'): ").strip()
            if title.lower() == "exit":
                print("Exiting content-based recommender.")
                break
            try:
                results = recommender.recommend(title)
                print("Recommendations:")
                for t in results['title']:
                    print(" -", t)
            except ValueError as e:
                print("Error:", e)

    elif choice == "2":
        from movie_recommender.collaborative_recommender import CollaborativeRecommender

        print("\nLoading collaborative filtering model...")
        recommender = CollaborativeRecommender()

        try:
            user_id = int(input("Enter User ID (e.g., 1): ").strip())
            results = recommender.recommend(user_id)
            print("Recommendations:")
            for _, row in results.iterrows():
                print(f" - {row['title']} (Predicted Rating: {row['est_rating']:.2f})")
        except ValueError:
            print("Invalid input. Please enter a valid integer for User ID.")
        except Exception as e:
            print("Error:", e)

    else:
        print("Invalid choice. Please enter 1 or 2.")
