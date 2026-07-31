import streamlit as st
import joblib

model=joblib.load("model.pkl")

st.title("Iris Flower Prediction")

sl=st.number_input("Sepal Length")
sw=st.number_input("Sepal Width")
pl=st.number_input("Petal Length")
pw=st.number_input("Petal Width")

if st.button("Predict"):

    result=model.predict([[sl,sw,pl,pw]])

    st.success("Prediction : {}".format(result[0]))