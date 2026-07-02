import warnings 
import sys 
import streamlit as st

st.header("Taschenrechner")

col1, col2, col3 = st.columns([1,3,1])

with col2:
    zahl1 = st.number_input("Gib die erste Zahl ein: ")
    zeichen = st.selectbox("Wähle ein Rechenzeichen: ", ["+", "-", "*", "/", "//", "%", "**"])
    zahl2 = st.number_input("Gib die zweite Zahl ein: ")

    if zahl1 and zeichen and zahl2:
        rechnung = f"{zahl1} {zeichen} {zahl2}"

        st.write("")
        st.write("")
        
        st.write(F"Ergebnis: {rechnung} = {round(eval(rechnung), 8)}")