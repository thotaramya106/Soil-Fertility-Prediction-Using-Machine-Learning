import streamlit as st
import pickle
import pandas as pd

# Load trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🌱 Soil Fertility Prediction App")

# Dropdown & numeric input fields based on your dataset

name = st.selectbox("Crop Name", ["Strawberry","Watermelon","Grapes","Arugula","Beet","Chard","Cress","Endive","Kale","Lettuce","Radicchio","Spinach","Tomatoes""Eggplants""Asparagus","Chilli Peppers","Cabbage","Cucumbers","Potatoes","Cauliflowers","Broccoli","Green Peas"])  # If more crops exist, add them

photoperiod = st.selectbox("Photoperiod", [
    "Day Neutral",
    "Short Day Period",
    "Long Day Period"
])

soil_type = st.selectbox("Soil Type", [
    "Loam", "Sandy", "Clay", "Silty"
])

category_ph = st.selectbox("Category pH", [
    "low_acidic", "neutral", "alkaline"
])

season = st.selectbox("Season", [
    "Summer", "Winter", "Spring", "Autumn"
])

temperature = st.number_input("Temperature", 0.0, 100.0, 20.0)
rainfall = st.number_input("Rainfall", 0.0, 2000.0, 700.0)
ph = st.number_input("pH Value", 0.0, 14.0, 6.5)
light_hours = st.number_input("Light Hours", 0.0, 24.0, 13.0)
light_intensity = st.number_input("Light Intensity", 0.0, 2000.0, 530.0)
rh = st.number_input("Relative Humidity (Rh)", 0.0, 100.0, 90.0)

nitrogen = st.number_input("Nitrogen", 0.0, 500.0, 170.0)
phosphorus = st.number_input("Phosphorus", 0.0, 500.0, 120.0)
potassium = st.number_input("Potassium", 0.0, 500.0, 240.0)

yield_value = st.number_input("Yield", 0.0, 100.0, 20.0)

n_ratio = st.number_input("N_Ratio", 0.0, 100.0, 10.0)
p_ratio = st.number_input("P_Ratio", 0.0, 100.0, 10.0)
k_ratio = st.number_input("K_Ratio", 0.0, 100.0, 10.0)


# Predict button
if st.button("Predict Soil Fertility"):
    input_data = pd.DataFrame([{
        "Name": name,
        "Photoperiod": photoperiod,
        "Temperature": temperature,
        "Rainfall": rainfall,
        "pH": ph,
        "Light_Hours": light_hours,
        "Light_Intensity": light_intensity,
        "Rh": rh,
        "Nitrogen": nitrogen,
        "Phosphorus": phosphorus,
        "Potassium": potassium,
        "Yield": yield_value,
        "Category_pH": category_ph,
        "Soil_Type": soil_type,
        "Season": season,
        "N_Ratio": n_ratio,
        "P_Ratio": p_ratio,
        "K_Ratio": k_ratio
    }])

    prediction = model.predict(input_data)[0]

    st.success(f"Predicted Fertility: {prediction}")
