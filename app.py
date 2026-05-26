import streamlit as st
import numpy as np
import joblib
from huggingface_hub import hf_hub_download

# ---------------------------
# Streamlit Page Config
# ---------------------------
st.set_page_config(
    page_title="Fire Type Classifier",
    layout="centered"
)

# ---------------------------
# Cache Model Loading
# ---------------------------
@st.cache_resource
def load_model_and_scaler():

    # Download model from Hugging Face
    model_path = hf_hub_download(
        repo_id="Monaljain/fire-detection-model",
        filename="best_fire_detection_model.pkl"
    )

    # Download scaler
    scaler_path = hf_hub_download(
        repo_id="Monaljain/fire-detection-model",
        filename="scaler.pkl"
    )

    # Load files
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)

    return model, scaler


# Load model and scaler
model, scaler = load_model_and_scaler()

# ---------------------------
# App Title
# ---------------------------
st.title("🔥 Fire Type Classification")
st.markdown("Predict fire type based on MODIS satellite readings.")

# ---------------------------
# User Inputs
# ---------------------------
brightness = st.number_input("Brightness", value=300.0)

bright_t31 = st.number_input(
    "Brightness T31",
    value=290.0
)

frp = st.number_input(
    "Fire Radiative Power (FRP)",
    value=15.0
)

scan = st.number_input(
    "Scan",
    value=1.0
)

track = st.number_input(
    "Track",
    value=1.0
)

confidence = st.selectbox(
    "Confidence Level",
    ["low", "nominal", "high"]
)

# ---------------------------
# Confidence Encoding
# ---------------------------
confidence_map = {
    "low": 0,
    "nominal": 1,
    "high": 2
}

confidence_val = confidence_map[confidence]

# ---------------------------
# Prepare Input
# ---------------------------
input_data = np.array([
    [
        brightness,
        bright_t31,
        frp,
        scan,
        track,
        confidence_val
    ]
])

scaled_input = scaler.transform(input_data)

# ---------------------------
# Prediction
# ---------------------------
if st.button("Predict Fire Type"):

    prediction = model.predict(scaled_input)[0]

    fire_types = {
        0: "Vegetation Fire",
        2: "Other Static Land Source",
        3: "Offshore Fire"
    }

    result = fire_types.get(prediction, "Unknown")

    st.success(f"Predicted Fire Type: {result}")