import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

url = 'https://raw.githubusercontent.com/kalyanichitre/san-jose-parking-analysis/main/Parking_Meters.csv'
df = pd.read_csv(url)

st.title("San Jose Parking Meter Data Analysis")
st.write("""This dashboard displays different visualizations and insights about parking meters across San Jose.""")

st.subheader("Parking Types vs Meter Types")
img_url = 'https://raw.githubusercontent.com/kalyanichitre/san-jose-parking-analysis/main/parking_types_vs_meter_types.svg'
st.image(img_url, caption="Parking Types vs Meter Types", use_container_width=True)

img_url = 'https://raw.githubusercontent.com/kalyanichitre/san-jose-parking-analysis/main/parking_meters_by_district_shortened.svg'
st.image(img_url, caption="Number of Parking Meters by District", use_container_width=True)

st.subheader("Map of Parking Meters")
st.markdown("""<iframe src="https://raw.githubusercontent.com/kalyanichitre/san-jose-parking-analysis/main/parking_meters_map.html" width="100%" height="600px"></iframe>""", unsafe_allow_html=True)

st.write("The app shows visualizations related to parking meters in San Jose.")
