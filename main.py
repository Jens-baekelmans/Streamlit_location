import streamlit as st
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl
import pandas as pd

# data ingestion
df = pd.read_csv('/Users/jens.baekelmans/PycharmProjects/covid/Locations_Collibra.csv')

#styling
st.markdown("""
<style>
.stApp {
    background-color: #E0FFDB;
    font-family: Helvetica;
}
p {
  font-size: 20px;
}

</style>""", unsafe_allow_html=True)

# header and subheader
st.header('Guess the countries of all the Collibra offices with our guessing game!')
st.subheader('Collibra is located in six countries at the moment. Below you will find six text boxes where you can enter '
             'your guesses. Afterwards, you can show the correct countries on your map.')

# lists
answer_list = []
Countries = ['United States of America', 'Belgium', 'Czech republic', 'France', 'Poland', 'United Kingdom']

col1, col2, col3 = st.columns(3)
#question 1
with col1:
    answer = st.text_input("Country 1",
        "")

    if answer:
        st.write("You entered: ", answer)
        answer_list.append(answer)

#question 2
with col2:
    answer = st.text_input("Country 2",
        "")

    if answer:
        st.write("You entered: ", answer)
        answer_list.append(answer)

#question 3
with col3:
    answer = st.text_input("Country 3",
        "")

    if answer:
        st.write("You entered: ", answer)
        answer_list.append(answer)

#another row of columns
col4, col5, col6 = st.columns(3)

#question 4
with col4:
    answer = st.text_input("Country 4",
        "")

    if answer:
        st.write("You entered: ", answer)
        answer_list.append(answer)

#question 5
with col5:
    answer = st.text_input("Country 5",
        "")

    if answer:
        st.write("You entered: ", answer)
        answer_list.append(answer)

#question 6
with col6:
    answer = st.text_input("Country 6",
        "")

    if answer:
        st.write("You entered: ", answer)
        answer_list.append(answer)


#score
if len(answer_list) == 6:
    p = set(answer_list) & set(Countries)
    total_score = len(p)
    st.write('Your total score is', str(total_score), " out of 6")
    if total_score < 3:
        st.write('You need fresh up on your location offices')
    if total_score >= 3:
        st.write('Well done, you know your stuff!')
    st.subheader('These are all the countries where there are Collibra offices located: ')

    st.write('United States of America')
    st.write('Belgium')
    st.write('Czech republic')
    st.write('France')
    st.write('Poland')
    st.write('United Kingdom')

    st.subheader('Let us show all the location on our beautifully created map')

st.subheader("Let's create our locations on a keplergl map ")
st.write('Add a new layer on the left hand side of the application. '
         'Use points to show our locations. '
         'Add latitude and longitude to their respective row. '
         'Choose a green color and make the radius 25 '
         'Add our office to the label row and see all locations of Collibra')
# test map

custom_config = {
  "version": "v1",
  "config": {
    "visState": {
      "filters": [],
      "layers": [],
      "interactionConfig": {}
    },
    "mapState": {
      "bearing": 0,
      "dragRotate": True,
      "latitude": 40.0,
      "longitude": -30.0,
      "isSplit": False,
      "zoom": 2
    },
    "mapStyle": {
      "styleType": "dark",
      "topLayerGroups": {},
      "visibleLayerGroups": {
        "label": True,
        "road": False,
        "border": True,
        "building": False,
        "water": True,
        "land": True
      }
    }
  }
}

map_1 = KeplerGl(height=500, config=custom_config)
map_1.add_data(df, name='Collibra Locations')
keplergl_static(map_1)




