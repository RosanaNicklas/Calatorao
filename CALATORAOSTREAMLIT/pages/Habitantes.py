import matplotlib.pyplot as plt
import pandas as pd
#import plotly.figure_factory as ff
import plotly.express as px
import pandas as pd
#import plotly.express as px
import streamlit as st
from PIL import Image

image = Image.open('Graph11.png')
st.image(image, caption='Habitantes')


Años = [1800, 1900, 1930, 1960, 1995, 2023]
Nacimientos = [62, 88, 104, 70, 18, 30]
Habitantes = [1437, 2351, 3506, 3400, 2700, 2900]
dati = pd.DataFrame({'Años': [1800, 1900, 1930, 1960, 1995, 2023],
'Habitantes': [1437, 2351, 3506, 3400, 2700, 2900]})
data = pd.DataFrame({'Años': [1800, 1900, 1930, 1960, 1995, 2023],
'Nacimientos': [62, 88, 104, 70, 18, 30],
'Habitantes': [1437, 2351, 3506, 3400, 2700, 2900]
 })
dato = pd.DataFrame({'Años': [1800, 1900, 1930, 1960, 1995, 2023],
'Nacimientos': [62, 88, 104, 70, 18, 30]}) 
st.bar_chart(dati)