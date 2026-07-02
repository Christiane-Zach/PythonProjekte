import warnings 
import sys 
import streamlit as st

st.set_page_config(
    page_title="Projekte mit Python",
    layout="wide"
)

def start():
    
    st.header("Willkommen!")
    
    st.subheader("Möchtest du spielen?")
    
    spiele_col1, spiele_col2, _, _ = st.columns(4)
    
    with spiele_col1:
        st.image("Spiele/ssp.png", width = "stretch")
        if st.button("Schere Stein Papier"):
            st.switch_page("Spiele/schere_stein_papier_page.py")
    
    with spiele_col2:
        st.image("Spiele/ttt.png", width = "stretch")
        if st.button("Tic Tac Toe"):
            st.switch_page("Spiele/tictactoe.py")
            
    st.subheader("Möchtest du rechnen?")
    
    rechen_col1, rechen_col2, rechen_col3, _ = st.columns(4)
    
    with rechen_col1:
        st.image("Rechenhilfen/Taschenrechner.png", width = "stretch")
        if st.button("Einfacher Taschenrechner"):
            st.switch_page("Rechenhilfen/taschenrechner.py")
    
    with rechen_col2:
        st.image("Rechenhilfen/wuerfel.png", width = "stretch")
        if st.button("Würfelsimulator"):
            st.switch_page("Rechenhilfen/dicesimulator_page.py")
            
    with rechen_col3:
        st.image("Rechenhilfen/caesar.png", width = "stretch")
        if st.button("Cäsar Verschlüsselung"):
            st.switch_page("Rechenhilfen/caesar.py")


start_seite = st.Page(start, title="Übersicht", icon=":material/dashboard:", default=True)
ssp = st.Page("Spiele/schere_stein_papier_page.py", title="Schere Stein Papier", icon=":material/content_cut:")
ttt = st.Page("Spiele/tictactoe.py", title="Tic Tac Toe", icon=":material/content_cut:")
dicesimulator = st.Page("Rechenhilfen/dicesimulator_page.py", title="Würfelsimulator", icon=":material/casino:")
caesar = st.Page("Rechenhilfen/caesar.py", title="Cäsar Verschlüsselung", icon=":material/lock:")
taschenrechner = st.Page("Rechenhilfen/taschenrechner.py", title="Taschenrechner", icon=":material/calculate:")

pg = st.navigation(
        {
            "":[start_seite],
            "Spiele": [ssp, ttt],
            "Rechenhilfen": [taschenrechner, dicesimulator, caesar]
        }
    )

pg.run()