import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import streamlit.components.v1 as components

url = 'https://raw.githubusercontent.com/kalyanichitre/san-jose-parking-analysis/main/Parking_Meters.csv'
df = pd.read_csv(url)

st.title("San Jose Parking Meter Data Analysis")
st.write("""This dashboard displays different visualizations and insights about parking meters across San Jose.""")

img_url = 'https://raw.githubusercontent.com/kalyanichitre/san-jose-parking-analysis/main/parking_types_vs_meter_types.svg'
st.image(img_url, caption="Parking Types vs Meter Types", use_container_width=True)

img_url = 'https://raw.githubusercontent.com/kalyanichitre/san-jose-parking-analysis/main/parking_meters_by_district.svg'
st.image(img_url, caption="Number of Parking Meters by District", use_container_width=True)

st.subheader("Map of Parking Meters")
components.html("""
<iframe src="https://drive.google.com/uc?export=view&id=1fyNZnr00lIz0aYWhMoq5LtIbpR1-HDp_" width="100%" height="600px"></iframe>
""", height=600)

parking_type = st.selectbox('Select Parking Type', df['PARKINGTYPE'].unique())
filtered_data = df[df['PARKINGTYPE'] == parking_type]
st.write(filtered_data)

st.bar_chart(filtered_data['METERTYPE'].value_counts())

min_rate, max_rate = st.slider("Select Parking Rate Range", float(df['PARKINGRATE'].min()), float(df['PARKINGRATE'].max()), (df['PARKINGRATE'].min(), df['PARKINGRATE'].max()))
filtered_by_rate = df[(df['PARKINGRATE'] >= min_rate) & (df['PARKINGRATE'] <= max_rate)]
st.write(filtered_by_rate)
st.bar_chart(filtered_by_rate['PARKINGTYPE'].value_counts())

st.write("The app shows visualizations related to parking meters in San Jose.")
