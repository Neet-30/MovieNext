# MovieNext 🎬 ( a movie recommendation system )

## Overview
This project is a **movie recommendation system** built with **Streamlit** and powered by a **machine learning model**.  
It recommends movies based on a selected title using **cosine similarity** and displays movie posters fetched from the **TMDB API**.

>Dataset can be downloaded from here is [HERE](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

>Some files due to their large sizes are uploaded [HERE](https://huggingface.co/spaces/neet30/MovieNext/tree/main)

## 🚀 Features
- Get top 10 movie recommendations based on similarity.
- Fetch movie posters from TMDB API.
- Simple Streamlit web interface.

## 🧠 Tech Stack
- Python
- Streamlit
- scikit-learn
- TMDB API

## Usage

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Select a movie from the dropdown list and click "Recommend" to get the top 10 recommended movies along with their posters.

## Results

The system provides the top 10 recommended movies for any selected movie title. It also fetches and displays the posters of these recommended movies using the TMDB API.

<img width="1485" height="891" alt="image" src="https://github.com/user-attachments/assets/ed0cf10a-d025-4a22-b0db-f748c076ebbb" />

