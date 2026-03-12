import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("models/bike_rental_model.pkl","rb"))

st.title("🚴 Bike Rental Prediction")
st.write("⚠️ Please enter values within the allowed range")

# ---- ROW 1 ----
col1, col2 = st.columns(2)

with col1:
    day = st.number_input("Day (1 - 31)", min_value=1, max_value=31)

with col2:
    month = st.number_input("Month (1 - 12)", min_value=1, max_value=12)


# ---- ROW 2 ----
col3, col4 = st.columns(2)

with col3:
    year = st.selectbox("Year", [2011, 2012])

with col4:
    season = st.selectbox(
        "Season",
        [1,2,3,4],
        help="1=Spring, 2=Summer, 3=Fall, 4=Winter"
    )


# ---- ROW 3 ----
col5, col6 = st.columns(2)

with col5:
    holiday = st.selectbox("Holiday", [0,1], help="0 = No, 1 = Yes")

with col6:
    weekday = st.slider("Weekday (0=Sun, 6=Sat)",0,6)


# ---- ROW 4 ----
col7, col8 = st.columns(2)

with col7:
    workingday = st.selectbox("Working Day",[0,1])

with col8:
    weather = st.selectbox(
        "Weather Situation",
        [1,2,3],
        help="1=Clear, 2=Mist, 3=Light Snow/Rain"
    )


# ---- ROW 5 ----
col9, col10 = st.columns(2)

with col9:
    temp = st.slider("Temperature",0.05,0.86)

with col10:
    atemp = st.slider("Feels Like Temperature",0.07,0.88)


# ---- ROW 6 ----
col11, col12 = st.columns(2)

with col11:
    humidity = st.slider("Humidity",0.0,0.97)

with col12:
    windspeed = st.slider("Wind Speed",0.02,0.50)


# ---- PREDICTION ----
if st.button("Predict Bike Rentals"):

    features = np.array([[day,month,year,season,holiday,
                          weekday,workingday,weather,
                          temp,atemp,humidity,windspeed]])

    prediction = model.predict(features)

    st.success(f"🚴 Predicted Bike Rentals: {int(prediction[0])}")