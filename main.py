import streamlit as st
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl
import pandas as pd
import pydeck as pdk
import numpy as np

# data ingestion
df = pd.read_csv(
    'https://raw.githubusercontent.com/Jens-baekelmans/Streamlit_location/main/LocationsCollibra_lat_lon.csv')

# styling
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
st.header('Guess the Location of all the Collibra offices with our guessing game!')
st.subheader(
    'Collibra is located in six countries at the moment. Below you will find six text boxes where you can enter '
    'your location guesses. Afterwards, you can show the correct countries on your map.')

# lists
answer_list = []
Countries = ['United States of America', 'Belgium', 'Czech republic', 'France', 'Poland', 'United Kingdom']

col1, col2, col3 = st.columns(3)
# question 1
with col1:
    answer = st.text_input("Country 1",
                           "")

    if answer:
        st.write("You entered: ", answer)
        answer_list.append(answer)

# question 2
with col2:
    answer = st.text_input("Country 2",
                           "")

    if answer:
        st.write("You entered: ", answer)
        answer_list.append(answer)

# question 3
with col3:
    answer = st.text_input("Country 3",
                           "")

    if answer:
        st.write("You entered: ", answer)
        answer_list.append(answer)

# another row of columns
col4, col5, col6 = st.columns(3)

# question 4
with col4:
    answer = st.text_input("Country 4",
                           "")

    if answer:
        st.write("You entered: ", answer)
        answer_list.append(answer)

# question 5
with col5:
    answer = st.text_input("Country 5",
                           "")

    if answer:
        st.write("You entered: ", answer)
        answer_list.append(answer)

# question 6
with col6:
    answer = st.text_input("Country 6",
                           "")

    if answer:
        st.write("You entered: ", answer)
        answer_list.append(answer)

# score
if len(answer_list) == 6:
    p = set(answer_list) & set(Countries)
    total_score = len(p)
    st.write('Your total score is', str(total_score), " out of 6")
    if total_score < 3:
        st.write('You need fresh up on the location of our offices')
    if total_score >= 3:
        st.write('Well done, you know your stuff!')
    st.subheader('These are all the countries where there are Collibra offices located: ')

    st.write('United States of America')
    st.write('Belgium')
    st.write('Czech republic')
    st.write('France')
    st.write('Poland')
    st.write('United Kingdom')

    st.subheader("Let's show our locations on a map ")
    st.map(df)
# st.write('Add a new layer on the left hand side of the application. '
#          'Use points to show our locations. '
#          'Add latitude and longitude to their respective row. '
#          'Choose a green color and make the radius 25 '
#          'Add our office to the label row and see all locations of Collibra')
# test map

# df_pydeck = pd.DataFrame([-40.070, -74.01], [33.787,-84.3831], columns='Coordinates')

custom_config = {
    "version": "v1",
    "config": {
        "visState": {
            "filters": [],
            "layers": [
                {
                    "id": "1iirg9",
                    "type": "heatmap",
                    "config": {
                        "dataId": "yj996aeb",
                        "label": "point",
                        "color": [
                            255,
                            203,
                            153
                        ],
                        "highlightColor": [
                            252,
                            242,
                            26,
                            255
                        ],
                        "columns": {
                            "lat": "Latitude ",
                            "lng": "Longitude "
                        },
                        "isVisible": True,
                        "visConfig": {
                            "opacity": 0.8,
                            "colorRange": {
                                "name": "Global Warming",
                                "type": "sequential",
                                "category": "Uber",
                                "colors": [
                                    "#5A1846",
                                    "#900C3F",
                                    "#C70039",
                                    "#E3611C",
                                    "#F1920E",
                                    "#FFC300"
                                ]
                            },
                            "radius": 100
                        },
                        "hidden": False,
                        "textLabel": [
                            {
                                "field": None,
                                "color": [
                                    255,
                                    255,
                                    255
                                ],
                                "size": 18,
                                "offset": [
                                    0,
                                    0
                                ],
                                "anchor": "start",
                                "alignment": "center"
                            }
                        ]
                    },
                    "visualChannels": {
                        "weightField": None,
                        "weightScale": "linear"
                    }
                }
            ],
            "interactionConfig": {
                "tooltip": {
                    "fieldsToShow": {
                        "yj996aeb": [
                            {
                                "name": "Country",
                                "format": None
                            },
                            {
                                "name": "Office ",
                                "format": None
                            },
                            {
                                "name": "Address",
                                "format": None
                            },
                            {
                                "name": "Latitude ",
                                "format": None
                            },
                            {
                                "name": "Longitude ",
                                "format": None
                            }
                        ]
                    },
                    "compareMode": False,
                    "compareType": "absolute",
                    "enabled": True
                },
                "brush": {
                    "size": 0.5,
                    "enabled": False
                },
                "geocoder": {
                    "enabled": False
                },
                "coordinate": {
                    "enabled": False
                }
            },
            "layerBlending": "normal",
            "splitMaps": [],
            "animationConfig": {
                "currentTime": None,
                "speed": 1
            }
        },
        "mapState": {
            "bearing": 0,
            "dragRotate": False,
            "latitude": 42.6526,
            "longitude": -33.67819,
            "pitch": 0,
            "zoom": 3,
            "isSplit": False
        },
        "mapStyle": {
            "styleType": "dark",
            "topLayerGroups": {},
            "visibleLayerGroups": {
                "label": True,
                "road": True,
                "border": False,
                "building": True,
                "water": True,
                "land": True,
                "3d building": False
            },
            "threeDBuildingColor": [
                9.665468314072013,
                17.18305478057247,
                31.1442867897876
            ],
            "mapStyles": {}
        }
    }
}
#
# map_1 = KeplerGl(height=500, data={'data_1': df}, config=custom_config)
# # map_1.add_data(df, name='Collibra Locations')
# keplergl_static(map_1)



# st.pydeck_chart(pdk.Deck(
#
#     initial_view_state=pdk.ViewState(
#
#         latitude=40,
#
#         longitude=-35,
#
#         zoom=10,
#
#         pitch=0,
#
#     ),
#
#     layers=[
#
#         pdk.Layer(
#
#             'HexagonLayer',
#
#             data=df,
#
#             get_position='[lon, lat]',
#
#             radius=200,
#
#             elevation_scale=4,
#
#             elevation_range=[0, 1000],
#
#             pickable=True,
#
#             extruded=True,
#
#         ),
#
#         pdk.Layer(
#
#             'ScatterplotLayer',
#
#             data=df,
#
#             get_position='[lon, lat]',
#
#             get_radius=200,
#
#         ),
#
#     ],
#
# ))
#
# data = [['40.7072','-74.01253'],['33.7876','-84.3831'], ['38.8992','-77.01405'], ['50.8651','4.34529'], ['50.0924','14.43386'],
#         ['48.8872','2.25021'], ['51.1088','17.02672'], ['51.5176','-0.09745']]
# df_2 = pd.DataFrame(data, columns=['lat', 'lon'])
# st.dataframe(df_2)
# #chart from streamlit
# chart_data = pd.DataFrame(
#    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#    columns=['lat', 'lon'])
# st.dataframe(chart_data)
# st.pydeck_chart(pdk.Deck(
#     map_style=None,
#     initial_view_state=pdk.ViewState(
#         latitude=37.76,
#         longitude=-122.4,
#         zoom=11,
#         pitch=90,
#     ),
#     layers=[
#         pdk.Layer(
#             'ScatterplotLayer',
#             data=df_2,
#             get_position='[lon, lat]',
#             get_color='[200, 30, 0, 160]',
#             get_radius=200,
#         ),
#     ],
# ))