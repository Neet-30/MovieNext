import streamlit as st
import pandas as pd
import requests
import pickle
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# -----------------------------
# Load preprocessed data
# -----------------------------
with open('movie_data.pkl', 'rb') as file:
    movies, cosine_sim = pickle.load(file)

# -----------------------------
# Get top 10 similar movies
# -----------------------------
def get_recommendations(title, cosine_sim=cosine_sim):
    idx = movies[movies['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]  # top 10
    movie_indices = [i[0] for i in sim_scores]
    return movies[['title', 'movie_id']].iloc[movie_indices]

# -----------------------------
# Fetch movie poster (with retries & error handling)
# -----------------------------
def fetch_poster(movie_id):
    api_key = "7b995d3c6fd91a2284b4ad8cb390c7b8"
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }

    # Retry setup for reliability
    session = requests.Session()
    retry = Retry(
        total=3,
        backoff_factor=2,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET"]
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("https://", adapter)

    try:
        response = session.get(url, headers=headers, timeout=10, verify=False)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get("poster_path")
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"
        else:
            return "https://via.placeholder.com/500x750?text=No+Poster"
    except requests.exceptions.RequestException as e:
        print(f"⚠️ TMDB request failed: {e}")
        return "https://via.placeholder.com/500x750?text=Error"

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("🎬 Movie Recommendation System")

selected_movie = st.selectbox("Select a movie:", movies['title'].values)

if st.button("Recommend"):
    recommendations = get_recommendations(selected_movie)
    st.subheader("Top 10 Recommended Movies:")

    # Display posters in 2 rows × 5 columns
    for i in range(0, 10, 5):
        cols = st.columns(5)
        for col, j in zip(cols, range(i, i+5)):
            if j < len(recommendations):
                movie_title = recommendations.iloc[j]['title']
                movie_id = recommendations.iloc[j]['movie_id']
                poster_url = fetch_poster(movie_id)
                with col:
                    st.image(poster_url, width=130)
                    st.caption(movie_title)

