import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

url = 'https://raw.githubusercontent.com/your-username/your-repository/main/Parking_Meters.csv'
df = pd.read_csv(url)

st.title("San Jose Parking Meter Data Analysis")
st.write("""
This dashboard displays different visualizations and insights about parking meters across San Jose.
""")

st.subheader("Parking Types vs Meter Types")
img_path = '/content/parking_types_vs_meter_types.svg'
st.image(img_path, caption="Parking Types vs Meter Types", use_column_width=True)

st.subheader("Number of Parking Meters by District")
img_path = '/content/parking_meters_by_district_shortened.svg'
st.image(img_path, caption="Number of Parking Meters by District", use_column_width=True)

st.subheader("Map of Parking Meters")
st.markdown("""
    <iframe src="/content/parking_meters_map.html" width="100%" height="600px"></iframe>
""", unsafe_allow_html=True)

st.write("The app shows visualizations related to parking meters in San Jose.")
