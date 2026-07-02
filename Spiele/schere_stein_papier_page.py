import streamlit as st
import warnings
import sys
from streamlit_image_select import image_select
import Spiele.schere_stein_papier as ssp

st.header("Schere Stein Papier")

if "selected" not in st.session_state:
    st.session_state.selected = None
if "spieler" not in st.session_state:
    st.session_state.spieler = 0
if "computer" not in st.session_state:
    st.session_state.computer = 0

spieler_col, computer_col = st.columns([2,1])


## Spieler-Spalte ######################################################
with spieler_col.container():
    
    img = image_select(
        label="Wähle",
        images=[f"Spiele/{value}.png" for value in ssp.zuweisung.values()],
        captions=list(ssp.zuweisung.values()),
        use_container_width=False,
        return_value ="index"
    )
    _, spieler_mitte, _ = spieler_col.columns(3)
    with spieler_mitte:
        if st.button("Auswahl bestätigen"):
            st.session_state.selected = img + 1

## Computer-Spalte ####################################################
with computer_col.container():
    st.write("Der Computer wählt auf dieser Seite")
    
    if st.session_state.selected is not None:
        comp_int = ssp.computer_eingabe()
        _, comp_mitte, _ = computer_col.columns(3)
        with comp_mitte:
            st.image(f"Spiele/{ssp.zuweisung[comp_int]}.png")

            
## Zusammenfassung ####################################################
_, mitte, _ = st.columns(3)

with mitte:
    
    st.write("")
    st.write("")
    
    if st.session_state.selected is not None:
        spieler, computer = ssp.find_the_winner(st.session_state.selected, comp_int)
        st.session_state.spieler += spieler
        st.session_state.computer += computer
        st.session_state.selected = None

    st.write(f"Spieler {st.session_state.spieler} : {st.session_state.computer} Computer")
    
    if mitte.button("Nochmal neu ..."):
        st.session_state.selected = None
        st.session_state.spieler = 0
        st.session_state.computer = 0
        st.rerun()