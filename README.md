# movie-recommender-suite

A versatile movie recommendation system supporting both **content-based** and **collaborative filtering** methods.  
This project offers three interfaces to suit your preference and workflow:  
- Command-Line Interface (CLI)  
- Flask Web Application  
- Streamlit Interactive App   

---

## Features

- Hybrid recommendation approach combining content-based and collaborative filtering  
- Flexible usage with CLI, Flask, and Streamlit interfaces  
- Easy to extend and customize  

---

## Project Structure

movie-recommender-suite/
│
├── movie_recommender/
│ ├── init.py
│ ├── data_loader.py
│ ├── feature_engineering.py
│ ├── content_recommender.py
│ ├── collaborative_recommender.py
│ └── utils.py
│
├── web_flask/
│ └── app.py
│
├── web_streamlit/
│ └── app.py
│
├── cli.py
├── data/
│ └── movies.csv
│
├── requirements.txt
├── README.md
└── .gitignore

yaml
Copy
Edit

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/BALADURGAG24/movie-recommender-suite.git
   cd movie-recommender-suite
Create and activate a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv env
source env/bin/activate    # On Windows use `env\Scripts\activate`
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Usage
1. Command Line Interface (CLI)
Run the CLI tool to get movie recommendations directly in your terminal:

bash
Copy
Edit
python cli.py --movie "The Matrix" --method content
Options for --method:

content — content-based filtering

collaborative — collaborative filtering

hybrid — combined approach

2. Flask Web Application
Start the Flask server:

bash
Copy
Edit
python web_flask/app.py
Open your browser and go to http://localhost:5000 to use the web interface.

3. Streamlit Interactive App
Run the Streamlit app:

bash
Copy
Edit
streamlit run web_streamlit/app.py
A browser window will open with a sleek interactive UI for movie recommendations.

Data
Place your movies.csv file inside the data/ folder.
The CSV should contain movie metadata such as titles, overviews, and user ratings (for collaborative filtering).

