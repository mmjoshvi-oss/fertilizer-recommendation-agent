import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Fertilizer Prediction", page_icon="🌱", layout="wide")

# ── Load Model (cached once) ──────────────────────────────
@st.cache_resource
def load_model():
    with open("fertilizer_prediction_model.pkl", "rb") as f:
        saved = pickle.load(f)
    return saved["model"], saved["encoders"], list(saved["model"].feature_names_in_)

model, encoders, feature_order = load_model()

# ── Cache encoder classes ─────────────────────────────────
@st.cache_data
def get_classes(key):
    return list(encoders[key].classes_)

# ── UI ────────────────────────────────────────────────────
st.title("🌱 Fertilizer Recommendation System")
st.write("Enter the required details below.")

with st.form("prediction_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        Temperature  = st.number_input("Temperature (°C)", min_value=0.0, step=0.1)
        Humidity     = st.number_input("Humidity (%)", min_value=0.0, step=0.1)
        Moisture     = st.number_input("Moisture (%)", min_value=0.0, step=0.1)

    with col2:
        Soil = st.selectbox("Soil Type", get_classes("Soil Type"))
        Crop = st.selectbox("Crop Type", get_classes("Crop Type"))

    with col3:
        Nitrogen    = st.number_input("Nitrogen",    min_value=0.0, step=0.1)
        Potassium   = st.number_input("Potassium",   min_value=0.0, step=0.1)
        Phosphorous = st.number_input("Phosphorous", min_value=0.0, step=0.1)

    submitted = st.form_submit_button("Predict Fertilizer", type="primary", use_container_width=True)

if submitted:
    soil_enc = encoders["Soil Type"].transform([Soil])[0]
    crop_enc = encoders["Crop Type"].transform([Crop])[0]

    sample = pd.DataFrame(
        data=[[Temperature, Humidity, Moisture, soil_enc, crop_enc, Nitrogen, Potassium, Phosphorous]],
        columns=feature_order          # guaranteed correct order
    )

    pred = model.predict(sample)[0]
    fertilizer = encoders["Fertilizer Name"].inverse_transform([pred])[0]
    st.success(f"✅ Recommended Fertilizer: **{fertilizer}**")
