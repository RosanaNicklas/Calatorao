import matplotlib.pyplot as plt
import pandas as pd
#import plotly.figure_factory as ff
import plotly.express as px
import pandas as pd
#import plotly.express as px
import streamlit as st
from PIL import Image


st.write("# CALATORAO GRÁFICOS ❃")



image = Image.open('Graph11.png')
st.image(image, caption='Habitantes')

image = Image.open('Graph122.png')
st.image(image, caption='Nacimientos')
