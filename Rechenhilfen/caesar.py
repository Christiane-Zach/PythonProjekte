import warnings 
import sys 
import streamlit as st

def caesar_verschluesselung(text: str, zahl: int) -> str:
    versch_text = ""
    for elem in text:
        if ord(elem) < 97 or ord(elem) > 122:
            versch_text = versch_text + elem
        else:
            new_ascii = ord(elem) + zahl
            if new_ascii < 122:
                versch_text = versch_text + chr(new_ascii)
            else:
                versch_text = versch_text + chr(new_ascii - 26)
    return versch_text


st.header("Cäsar Verschlüsselung")

text = st.text_input("Bitte gib eine Text ein. Beachte, dass er in Kleinbuchstaben weiterverarbeitet wird: ").lower()
zahl = st.number_input("Bitte gib eine Verschiebung ein: ", min_value = 0, step = 1)

if st.button("Verschlüsseln"):
    
    st.subheader("Der Verschlüsselte Text lautet: ")
    
    st.write(caesar_verschluesselung(text, zahl))