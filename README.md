# 🏡 House Price Predictor - Bengaluru

This is a Machine Learning-powered web app built with **Streamlit** that predicts the estimated price of a house in Bengaluru based on:

- Location
- Total square feet
- Number of bathrooms
- Number of bedrooms (BHK)

The app also displays the predicted location on a **map using Folium**!

---

## 🚀 Features

- Trained using **Random Forest Regressor** for better accuracy
- Encodes location data dynamically
- Visualizes predicted location with **interactive map**
- Simple and fast UI using **Streamlit**

---

## 🧠 Model

The model was trained on a cleaned version of the Bengaluru housing dataset with the following features:

- `location`
- `total_sqft`
- `bath`
- `bhk`

Saved models:
- `model.pkl` – Trained Random Forest model
- `features.pkl` – Feature columns used in training

---

## 🛠️ Run Locally

### Prerequisites
- Python 3.x installed
- `pip` installed (use a virtual environment recommended)

### Setup

```bash
# 1. Clone the repo
git clone https://github.com/your-username/house-price-predictor.git
cd house-price-predictor

# 2. (Optional) Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Streamlit app
streamlit run app.py
