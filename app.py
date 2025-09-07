# # import pickle
# # import streamlit as st
# # import requests
# #
# # def fetch_poster(movie_id):
# #     url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
# #     data = requests.get(url)
# #     data = data.json()
# #     poster_path = data['poster_path']
# #     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
# #     return full_path
# #
# # def recommend(movie):
# #     index = movies[movies['title'] == movie].index[0]
# #     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
# #     recommended_movie_names = []
# #     recommended_movie_posters = []
# #     for i in distances[1:6]:
# #         # fetch the movie poster
# #         movie_id = movies.iloc[i[0]].movie_id
# #         recommended_movie_posters.append(fetch_poster(movie_id))
# #         recommended_movie_names.append(movies.iloc[i[0]].title)
# #
# #     return recommended_movie_names,recommended_movie_posters
# #
# #
# # st.header('Movie Recommender System')
# # movies = pickle.load(open('movie_list.pkl','rb'))
# # similarity = pickle.load(open('similarity.pkl','rb'))
# #
# # movie_list = movies['title'].values
# # selected_movie = st.selectbox(
# #     "Type or select a movie from the dropdown",
# #     movie_list
# # )
# #
# # if st.button('Show Recommendation'):
# #     recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
# #     col1, col2, col3, col4, col5 = st.columns(5)
# #     with col1:
# #         st.text(recommended_movie_names[0])
# #         st.image(recommended_movie_posters[0])
# #     with col2:
# #         st.text(recommended_movie_names[1])
# #         st.image(recommended_movie_posters[1])
# #
# #     with col3:
# #         st.text(recommended_movie_names[2])
# #         st.image(recommended_movie_posters[2])
# #     with col4:
# #         st.text(recommended_movie_names[3])
# #         st.image(recommended_movie_posters[3])
# #     with col5:
# #         st.text(recommended_movie_names[4])
# #         st.image(recommended_movie_posters[4])
# #
# #
# #
# import pickle
# import streamlit as st
# import requests
# import streamlit.components.v1 as components
#
# st.set_page_config(page_title="Movie Recommender", layout="wide")
#
# # ---------------- Fetch Poster ----------------
# def fetch_poster(movie_id):
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
#     data = requests.get(url).json()
#     poster_path = data['poster_path']
#     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
#     return full_path
#
# # ---------------- Recommendation Logic ----------------
# def recommend(movie):
#     index = movies[movies['title'] == movie].index[0]
#     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
#     recommended_movie_names = []
#     recommended_movie_posters = []
#     for i in distances[1:11]:  # top 10 movies
#         movie_id = movies.iloc[i[0]].movie_id
#         recommended_movie_posters.append(fetch_poster(movie_id))
#         recommended_movie_names.append(movies.iloc[i[0]].title)
#     return recommended_movie_names, recommended_movie_posters
#
#
# # ---------------- UI ----------------
# st.markdown("<h1 style='text-align: center; color: #E50914;'>🍿 Movie Recommender System</h1>", unsafe_allow_html=True)
#
# # Load data
# movies = pickle.load(open('movie_list.pkl', 'rb'))
# similarity = pickle.load(open('similarity.pkl', 'rb'))
#
# movie_list = movies['title'].values
# selected_movie = st.selectbox("🎥 Select a movie to get recommendations:", movie_list)
#
# if st.button('✨ Show Recommendation'):
#     names, posters = recommend(selected_movie)
#
#     # Build cards
#     cards = ""
#     for name, poster in zip(names, posters):
#         cards += f"""
#         <div class="card">
#             <img src="{poster}" alt="{name}">
#             <p>{name}</p>
#         </div>
#         """
#
#     # Render Netflix-style scrollable carousel
#     components.html(
#         f"""
#         <style>
#         .scroll-container {{
#             display: flex;
#             overflow-x: auto;
#             padding: 20px;
#         }}
#         .card {{
#             flex: 0 0 auto;
#             margin-right: 15px;
#             border-radius: 15px;
#             overflow: hidden;
#             background-color: #111;
#             box-shadow: 0px 4px 10px rgba(0,0,0,0.6);
#             transition: transform 0.3s;
#             text-align: center;
#             width: 200px;
#         }}
#         .card:hover {{
#             transform: scale(1.1);
#         }}
#         .card img {{
#             width: 100%;
#             height: 300px;
#             object-fit: cover;
#         }}
#         .card p {{
#             color: white;
#             padding: 10px;
#             font-weight: bold;
#         }}
#         </style>
#
#         <div class='scroll-container'>
#             {cards}
#         </div>
#         """,
#         height=500,
#         scrolling=True
#     )
#
# import pickle
# import streamlit as st
# import requests
# import streamlit.components.v1 as components
# from concurrent.futures import ThreadPoolExecutor
#
# # ---------------- Page Config ----------------
# st.set_page_config(page_title="Movie Recommender", layout="wide")
#
# API_KEY = "8265bd1679663a7ea12ac168da84d2e8"
#
# # ---------------- Fetch Helper ----------------
# @st.cache_data
# def fetch_poster(movie_id):
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
#     data = requests.get(url).json()
#     poster_path = data.get("poster_path")
#     return f"https://image.tmdb.org/t/p/w500/{poster_path}" if poster_path else None
#
# @st.cache_data
# def fetch_details(movie_id):
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
#     data = requests.get(url).json()
#     cast_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={API_KEY}&language=en-US"
#     cast_data = requests.get(cast_url).json()
#     cast = [actor["name"] for actor in cast_data.get("cast", [])[:5]]
#
#     return {
#         "poster": f"https://image.tmdb.org/t/p/w500/{data.get('poster_path')}" if data.get("poster_path") else None,
#         "title": data.get("title", "Unknown"),
#         "overview": data.get("overview", "No description available."),
#         "language": data.get("original_language", "N/A"),
#         "release_date": data.get("release_date", "N/A"),
#         "cast": cast
#     }
#
# # ---------------- Recommendation Logic ----------------
# def recommend(movie):
#     index = movies[movies['title'] == movie].index[0]
#     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
#     movie_ids = [movies.iloc[i[0]].movie_id for i in distances[1:11]]
#     with ThreadPoolExecutor() as executor:
#         recommended_movies = list(executor.map(fetch_details, movie_ids))
#     return recommended_movies
#
# # ---------------- Category Rows ----------------
# def fetch_category_movies(genre_id):
#     """Fetch popular movies from a specific genre"""
#     url = f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&with_genres={genre_id}&language=en-US&sort_by=popularity.desc"
#     data = requests.get(url).json()
#     movies = data.get("results", [])[:10]
#     return [(m["title"], f"https://image.tmdb.org/t/p/w500/{m['poster_path']}") for m in movies if m.get("poster_path")]
#
# def render_row(title, movies):
#     """Render a horizontal row of posters"""
#     posters_html = "".join(
#         [f"""
#         <div class="card">
#             <img src="{poster}" alt="{name}">
#             <p>{name}</p>
#         </div>
#         """ for name, poster in movies]
#     )
#     components.html(
#         f"""
#         <style>
#         .row-title {{
#             color: #E50914;
#             font-size: 22px;
#             font-weight: bold;
#             margin: 20px 0 10px 10px;
#         }}
#         .scroll-container {{
#             display: flex;
#             overflow-x: auto;
#             padding: 10px;
#         }}
#         .card {{
#             flex: 0 0 auto;
#             margin-right: 15px;
#             border-radius: 12px;
#             overflow: hidden;
#             background-color: #111;
#             text-align: center;
#             transition: transform 0.3s;
#             width: 180px;
#         }}
#         .card:hover {{
#             transform: scale(1.1);
#         }}
#         .card img {{
#             width: 100%;
#             height: 250px;
#             object-fit: cover;
#         }}
#         .card p {{
#             color: white;
#             font-size: 14px;
#             margin: 5px 0;
#         }}
#         </style>
#         <div class="row-title">{title}</div>
#         <div class="scroll-container">{posters_html}</div>
#         """,
#         height=350,
#     )
#
# # ---------------- CSS Styling ----------------
# st.markdown(
#     """
#     <style>
#     body {
#         background: linear-gradient(135deg, #0f0f0f, #1c1c1c, #111);
#         color: white;
#     }
#     .stSelectbox label {
#         font-size: 18px;
#         color: #E50914;
#     }
#     .stButton>button {
#         background-color: #E50914;
#         color: white;
#         border-radius: 10px;
#         padding: 10px 20px;
#         font-weight: bold;
#         transition: 0.3s;
#     }
#     .stButton>button:hover {
#         background-color: #b20710;
#         transform: scale(1.05);
#     }
#     .movie-card {
#         background-color: #1c1c1c;
#         border-radius: 15px;
#         padding: 15px;
#         margin: 10px;
#         text-align: center;
#         box-shadow: 0 4px 15px rgba(0,0,0,0.7);
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )
#
# # ---------------- UI ----------------
# st.markdown("<h1 style='text-align: center; color: #E50914;'>🍿 Movie Recommender System</h1>", unsafe_allow_html=True)
#
# # Load data
# movies = pickle.load(open('movie_list.pkl', 'rb'))
# similarity = pickle.load(open('similarity.pkl', 'rb'))
#
# # --- Search + Recommendation FIRST ---
# st.subheader("🎥 Search Your Movie")
# movie_list = movies['title'].values
# selected_movie = st.selectbox("Select a movie:", movie_list)
#
# if st.button("✨ Show Recommendation"):
#     with st.spinner("🔍 Finding best recommendations..."):
#         recommended_movies = recommend(selected_movie)
#
#     st.success("✅ Here are your recommendations!")
#
#     cols = st.columns(2)
#     for i, details in enumerate(recommended_movies):
#         with cols[i % 2]:
#             st.markdown(
#                 f"""
#                 <div class="movie-card">
#                     <img src="{details['poster']}" width="250">
#                     <h3>{details['title']}</h3>
#                     <p><b>Release Date:</b> {details['release_date']}</p>
#                     <p><b>Language:</b> {details['language']}</p>
#                     <p><b>Cast:</b> {', '.join(details['cast'])}</p>
#                     <p style="text-align: justify;">{details['overview']}</p>
#                 </div>
#                 """,
#                 unsafe_allow_html=True
#             )
#
# # --- Category Rows AFTER recommendations ---
# st.markdown("<h2 style='color:#E50914;'>🔥 Explore by Genre</h2>", unsafe_allow_html=True)
# render_row("😂 Funny Movies", fetch_category_movies(35))      # Comedy
# render_row("👻 Horror Movies", fetch_category_movies(27))    # Horror
# render_row("🧙 Fantasy Movies", fetch_category_movies(14))   # Fantasy
# render_row("🔥 Action Movies", fetch_category_movies(28))    # Action


import pickle
import streamlit as st
import requests

# ---------------- Streamlit Config ----------------
st.set_page_config(page_title="🎬 Movie Recommender System", layout="wide")

# ---------------- API Key ----------------
API_KEY = st.secrets["TMDB_API_KEY"]  # <- API key yahan se read hogi (add in secrets.toml)

# ---------------- Fetch Movies from TMDB ----------------
def fetch_movies_from_category(category="popular"):
    url = f"https://api.themoviedb.org/3/movie/{category}?api_key={API_KEY}&language=en-US&page=1"
    data = requests.get(url).json()
    return data.get("results", [])

def fetch_movies_by_genre(genre_id):
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&language=en-US&with_genres={genre_id}&page=1"
    data = requests.get(url).json()
    return data.get("results", [])

def fetch_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    data = requests.get(url).json()

    poster_path = data.get("poster_path")
    poster_url = f"https://image.tmdb.org/t/p/w500/{poster_path}" if poster_path else None
    title = data.get("title", "Unknown")
    overview = data.get("overview", "No description available.")
    language = data.get("original_language", "N/A")
    release_date = data.get("release_date", "N/A")

    # Cast
    cast_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={API_KEY}&language=en-US"
    cast_data = requests.get(cast_url).json()
    cast = [actor["name"] for actor in cast_data.get("cast", [])[:5]]

    return {
        "poster": poster_url,
        "title": title,
        "overview": overview,
        "language": language,
        "release_date": release_date,
        "cast": cast
    }

# ---------------- Recommendation Logic ----------------
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies = []
    for i in distances[1:7]:
        movie_id = movies.iloc[i[0]].movie_id
        details = fetch_details(movie_id)
        recommended_movies.append(details)
    return recommended_movies

# ---------------- CSS Styling ----------------
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #0f0f0f, #1c1c1c, #111);
        color: white;
    }
    .stSelectbox label {
        font-size: 18px;
        color: #E50914;
    }
    .stButton>button {
        background-color: #E50914;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #b20710;
        transform: scale(1.05);
    }
    .movie-card {
        background-color: #1c1c1c;
        border-radius: 15px;
        padding: 15px;
        margin: 10px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.7);
    }
    .movie-card img {
        border-radius: 10px;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- UI Header ----------------
st.markdown("<h1 style='text-align: center; color: #E50914;'>🍿 Movie Recommender System </h1>", unsafe_allow_html=True)

# ---------------- Load Data ----------------
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# ---------------- Search + Recommend ----------------
movie_list = movies['title'].values
selected_movie = st.selectbox("🎥 Search a movie:", movie_list)

if st.button("✨ Show Recommendation"):
    recommended_movies = recommend(selected_movie)
    cols = st.columns(2)
    for i, details in enumerate(recommended_movies):
        with cols[i % 2]:
            st.markdown(
                f"""
                <div class="movie-card">
                    <img src="{details['poster']}" width="250">
                    <h3>{details['title']}</h3>
                    <p><b>Release Date:</b> {details['release_date']}</p>
                    <p><b>Language:</b> {details['language']}</p>
                    <p><b>Cast:</b> {', '.join(details['cast'])}</p>
                    <p style="text-align: justify;">{details['overview']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

# ---------------- Netflix-Style Categories ----------------
st.subheader("🔥 Trending Now")
trending_movies = fetch_movies_from_category("popular")
cols = st.columns(5)
for i, m in enumerate(trending_movies[:10]):
    with cols[i % 5]:
        st.image(f"https://image.tmdb.org/t/p/w200{m['poster_path']}", caption=m['title'])

st.subheader("😂 Comedy Movies")
comedy_movies = fetch_movies_by_genre(35)  # 35 = Comedy
cols = st.columns(5)
for i, m in enumerate(comedy_movies[:10]):
    with cols[i % 5]:
        st.image(f"https://image.tmdb.org/t/p/w200{m['poster_path']}", caption=m['title'])

st.subheader("👻 Horror Movies")
horror_movies = fetch_movies_by_genre(27)  # 27 = Horror
cols = st.columns(5)
for i, m in enumerate(horror_movies[:10]):
    with cols[i % 5]:
        st.image(f"https://image.tmdb.org/t/p/w200{m['poster_path']}", caption=m['title'])

st.subheader("🧙 Fantasy Movies")
fantasy_movies = fetch_movies_by_genre(14)  # 14 = Fantasy
cols = st.columns(5)
for i, m in enumerate(fantasy_movies[:10]):
    with cols[i % 5]:
        st.image(f"https://image.tmdb.org/t/p/w200{m['poster_path']}", caption=m['title'])
