import streamlit as st

# Load custom CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load HTML content
with open("layout.html") as f:
    st.markdown(f.read(), unsafe_allow_html=True)
