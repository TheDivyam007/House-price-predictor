# 🏡 House Price Predictor - Bengaluru

A Machine Learning-powered web app built with Streamlit that predicts the estimated price of a house in Bengaluru based on:

- 📍 Location  
- 📐 Total Square Feet  
- 🚿 Number of Bathrooms  
- 🛏️ Number of Bedrooms (BHK)  

The app also displays the predicted location on a map using Folium!

---

## 🚀 Features

- ✅ Trained using Random Forest Regressor for better accuracy  
- 🧠 Dynamic encoding of location data  
- 🗺️ Interactive map showing predicted location  
- ⚡ Fast and easy-to-use Streamlit interface  

---

## 🧠 Model

The model was trained on a cleaned version of the Bengaluru housing dataset using these features:

- `location`  
- `total_sqft`  
- `bath`  
- `bhk`

**Saved files**:
- `model.pkl` – Trained Random Forest model  
- `features.pkl` – Feature columns used during training  

---

## 🛠️ Run Locally

### Prerequisites:
- Python 3.x  
- pip (Virtual environment recommended)

### Setup:

```bash
# 1. Clone the repo
git clone https://github.com/your-username/house-price-predictor.git
cd house-price-predictor

# 2. (Optional) Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Streamlit app
streamlit run app.py
```

---

## 📁 Folder Structure

```
house-price-predictor/
├── app.py
├── model.pkl
├── features.pkl
├── data/
│   └── Bengaluru_House_Data.csv
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🙋‍♂️ Author

**Divyam Kumar**  
[GitHub: @TheDivyam007](https://github.com/TheDivyam007)

---
