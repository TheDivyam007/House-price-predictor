import streamlit as st
import pickle
import numpy as np
import pandas as pd
import folium
from streamlit_folium import folium_static

# Load model and feature names
model = pickle.load(open('model.pkl', 'rb'))
features = pickle.load(open('features.pkl', 'rb'))

# Extract locations from feature columns
locations = [col.replace('location_', '') for col in features.columns if 'location_' in col]

# Fallback if no locations found
if not locations:
    locations = ['Whitefield', 'HSR Layout', 'Rajaji Nagar', 'Electronic City']  # example defaults

# Function to predict price
def predict_price(location, sqft, bath, bhk):
    x = np.zeros(len(features.columns))
    x[features.columns.get_loc('total_sqft')] = sqft
    x[features.columns.get_loc('bath')] = bath
    x[features.columns.get_loc('bhk')] = bhk
    loc_col = f'location_{location}'
    if loc_col in features.columns:
        x[features.columns.get_loc(loc_col)] = 1
    return model.predict([x])[0]

# Dummy coordinates for a few key locations
location_coords = {
    'Whitefield': (12.9698, 77.7499),
    'Rajaji Nagar': (12.9915, 77.5566),
    'HSR Layout': (12.9109, 77.6446),
    'Electronic City': (12.8452, 77.6600)
}

# Streamlit App UI
st.title("🏡 House Price Predictor - Bengaluru")
st.markdown("Enter the details below to get a price estimate and see it on the map.")

location = st.selectbox("Select Location", sorted(locations), index=0)
sqft = st.number_input("Total Square Feet", min_value=300, max_value=10000, step=50)
bath = st.slider("Bathrooms", 1, 5, 2)
bhk = st.slider("BHK (Bedrooms)", 1, 5, 2)

if st.button("Predict Price"):
    predicted_price = predict_price(location, sqft, bath, bhk)
    st.success(f"🏷️ Estimated Price: ₹ {predicted_price:.2f} Lakhs")

    if location in location_coords:
        lat, lon = location_coords[location]
        m = folium.Map(location=[lat, lon], zoom_start=15)
        popup = folium.Popup(f'₹ {predicted_price:.2f} Lakhs', parse_html=True)
        folium.Marker([lat, lon], popup=popup, tooltip=location).add_to(m)
        folium_static(m)
    else:
        st.warning("⚠️ Map coordinates not available for this location.")
