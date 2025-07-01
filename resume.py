import streamlit as st

# Load CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load HTML layout
with open("layout.html", 'r') as f:
    html_content = f.read()
    st.markdown(html_content, unsafe_allow_html=True)
