import streamlit as st
import pandas as pd
import pickle

st.set_page_config(
    page_title="Fertilizer Prediction",
    page_icon="🌱",
    layout="wide"
)

# -------------------------
# Load Model
# -------------------------
@st.cache_resource
def load_model():
    try:
        with open("fertilizer_prediction_model.pkl", "rb") as file:
            saved = pickle.load(file)
        return saved["model"], saved["encoders"]
    except FileNotFoundError:
        st.error("❌ Model file 'fertilizer_prediction_model.pkl' not found.")
        st.stop()
    except Exception as e:
        st.error(f"❌ Error loading model: {e}")
        st.stop()

model, encoders = load_model()

st.title("🌱 Fertilizer Recommendation System")
st.write("Enter the required details below.")

col1, col2, col3 = st.columns(3)

with col1:
    Temperature = st.number_input("Temperature (°C)", min_value=0.0, step=0.1)
    Humidity    = st.number_input("Humidity (%)",    min_value=0.0, step=0.1)
    Moisture    = st.number_input("Moisture (%)",    min_value=0.0, step=0.1)

with col2:
    Soil = st.selectbox("Soil Type", encoders["Soil Type"].classes_)
    Crop = st.selectbox("Crop Type", encoders["Crop Type"].classes_)

with col3:
    Nitrogen   = st.number_input("Nitrogen",   min_value=0.0, step=0.1)
    Potassium  = st.number_input("Potassium",  min_value=0.0, step=0.1)
    Phosphorous= st.number_input("Phosphorous", min_value=0.0, step=0.1)

if st.button("Predict Fertilizer", type="primary", use_container_width=True):
    try:
        soil_encoded = encoders["Soil Type"].transform([Soil])[0]
        crop_encoded = encoders["Crop Type"].transform([Crop])[0]

        sample = pd.DataFrame({
            "Temperature":  [Temperature],
            "Humidity":     [Humidity],
            "Moisture":     [Moisture],
            "Soil Type":    [soil_encoded],
            "Crop Type":    [crop_encoded],
            "Nitrogen":     [Nitrogen],
            "Potassium":    [Potassium],
            "Phosphorous":  [Phosphorous]
        })

        # Ensure column order matches training data
        if hasattr(model, "feature_names_in_"):
            sample = sample[model.feature_names_in_]

        prediction = model.predict(sample)
        fertilizer = encoders["Fertilizer Name"].inverse_transform(prediction)

        st.success(f"✅ Recommended Fertilizer: **{fertilizer[0]}**")

    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")
