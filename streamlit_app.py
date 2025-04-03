import streamlit as st
import pickle

model = pickle.load(open("model.pkl", "rb"))

st.title("IceCream Revenue")
st.markdown(
    "The dataset contains modifications with regards to the original for illustrative & learning purposes"
)
st.markdown(
    "Model Used - Linear Regression"
)
st.write(f"R²: {0.9771}")
st.write(f"Intercept: {46.18}")
st.write(f"Coefficient: {21.38}")

temperature = st.number_input("Define Temperature?", min_value=0.0, max_value=50.0, value=20.0, step=0.1)


user_input = [[temperature]]

if st.button('Predict?'):
    st.write(f"Based on the temperature {temperature} °C, the revenue will be around: ", model.predict(user_input).round(2))


# dataset = 'https://github.com/YBIFoundation/Dataset/raw/main/Ice%20Cream.csv'
