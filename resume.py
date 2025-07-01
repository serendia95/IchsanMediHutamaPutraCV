import streamlit as st

# Load CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load HTML layout
with open("layout.html", 'r') as f:
    html_content = f.read()
    st.markdown(html_content, unsafe_allow_html=True)

# Sidebar Contact Info
with st.sidebar:
    st.title("📬 Contact")
    st.markdown("""
    📞 +62 821-1411-4195  
    📧 ichsanmedi95@gmail.com  
    📧 ichsanmedi_v@ymail.com  
    📍 Lippo Karawaci, Tangerang, Banten  
    [LinkedIn](https://www.linkedin.com/in/ichsan-medi-hutama-putra/)  
    [GitHub](https://github.com/serendia95)  
    """)
