import streamlit as st
import pickle
import pandas as pd
import requests

st.set_page_config(layout="wide")

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=6c72dcf33d8559368a457d38228be17f&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    recommanded_movie_list = sorted(list(enumerate((distances))), reverse=True, key=lambda x: x[1])[1:11]


    recommended_movies = []
    recommended_movies_poster = []
    for i in recommanded_movie_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from api
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

# Render HTML with unsafe_allow_html set to True
st.markdown(
    "<h1 style='text-align: center; color:#ff5500;' class='focus-in-contract'>BHADRAK ENGINEERING SCHOOL AND TECHNOLOGY (BEST),&nbsp;&nbsp;ASURALI,&nbsp;&nbsp; BHADRAK</h1><h2 style='text-align: center;'>Department Of CSE 💻</h2>", 
    unsafe_allow_html=True
)
#HTMl STYLE

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bungee+Outline&display=swap');

    body
    {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        scroll-behavior: smooth;
    }
    .focus-in-contract {
	-webkit-animation: focus-in-contract 0.7s cubic-bezier(0.250, 0.460, 0.450, 0.940) both;
	        animation: focus-in-contract 0.7s cubic-bezier(0.250, 0.460, 0.450, 0.940) both;
}
    @-webkit-keyframes focus-in-contract {
  0% {
    letter-spacing: 1em;
    -webkit-filter: blur(12px);
            filter: blur(12px);
    opacity: 0;
  }
  100% {
    -webkit-filter: blur(0px);
            filter: blur(0px);
    opacity: 1;
  }
}
@keyframes focus-in-contract {
  0% {
    letter-spacing: 1em;
    -webkit-filter: blur(12px);
            filter: blur(12px);
    opacity: 0;
  }
  100% {
    -webkit-filter: blur(0px);
            filter: blur(0px);
    opacity: 1;
  }
}
    h1.linear {
    text-align: center;
    background: #ff6f00;
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    text-fill-color: transparent;
    background-size: 500% auto;
    font-size: 4rem;
    letter-spacing: 0.5rem;
    animation: textShine 5s ease-in-out infinite alternate;
    font-family: "Bungee Outline", sans-serif;
}
@keyframes textShine {
    0% {
        filter: hue-rotate(0);
    }
    100% {
        filter: hue-rotate(360deg);
    }
}
    </style>
    """, 
    unsafe_allow_html=True
)



# st.header("Bhadrak Engineering School and Technology (BEST), Asurali, Bhadrak")
# st.subheader("Department Of CSE-2024")
st.markdown(
    "<h1 class='linear'>MOVIE RECOMMENDER SYSTEM</h1>",
    unsafe_allow_html=True
)

selected_movies_name = st.selectbox(
"Search for recommended movies",
movies['title'].values)

if st.button('Recommend'):
    names,posters = recommend(selected_movies_name)

    # col1 = st.columns(1)
    # for i in range(0, 9):
    #     cols = st.columns(3)
    #     st.header(names[i])
    #     st.image(posters[i])
    # First "row"
    col1, col2 = st.columns(2)
    with col1:
        col11, col12, col13 = st.columns([1, 2, 1])
        with col12:
            st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])


    # Second "row"
    col3, col4 = st.columns(2)
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])

    # Third "row"
    col5, col6 = st.columns(2)
    with col5:
        st.text(names[4])
        st.image(posters[4])
    with col6:
        st.text(names[5])
        st.image(posters[5])

    # Fourth "row"
    col7, col8 = st.columns(2)
    with col7:
        st.text(names[6])
        st.image(posters[6])
    with col8:
        st.text(names[7])
        st.image(posters[7])

    # Fifth "row"
    col9, col10 = st.columns(2)
    with col9:
        st.text(names[8])
        st.image(posters[8])
    with col10:
        st.text(names[9])
        st.image(posters[9])
    # with row1:
    #     st.header(names[0])
    #     st.image(posters[0])
    # with row2:
    #     st.header(names[1])
    #     st.image(posters[1])
    # with row3:
    #     st.header(names[2])
    #     st.image(posters[2])
    # with row4:
    #     st.header(names[3])
    #     st.image(posters[3])
    # with row5:
    #     st.header(names[4])
    #     st.image(posters[4])
    # with row6:
    #     st.header(names[5])
    #     st.image(posters[5])
    # with row7:
    #     st.header(names[6])
    #     st.image(posters[6])
    # with row8:
    #     st.header(names[7])
    #     st.image(posters[7])
    # with row9:
    #     st.header(names[8])
    #     st.image(posters[8])
    # with row10:
    #     st.header(names[9])
    #     st.image(posters[9])