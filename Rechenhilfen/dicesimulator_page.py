import warnings 
import sys 
import streamlit as st
import Rechenhilfen.dicesimulator as ds

st.header("Würfelsimulator")

col1, col2, col3 = st.columns([1,3,1])

with col2:
    st.write("")
    st.write("")
    
    st.image("Rechenhilfen/wuerfel.png", width=250)

    anzahl = st.number_input("Wie viele Würfe sollen simuliert werden?  ", min_value = 0, step = 1)

    if anzahl:
        würfe = ds.wurf_simulator(anzahl)
        st.write(f"Berechneter Mittelwert:    {round(ds.mittelwert(würfe),6)}")
        st.write("Theoretischer Mittelwert:  3.5")