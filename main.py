import streamlit as st

from backend.get_url import get_todays_url

st.set_page_config(
    page_title="Welcome",
    page_icon="👋",
    layout="wide"
)

url = get_todays_url()

st.markdown("""
<style>
.big-font {
    font-size:300px !important;
}
</style>
""", unsafe_allow_html=True)

html_code = f'<a class="big-font" href="{url}">🌲</a>'
st.markdown(html_code, unsafe_allow_html=True)


st.write("for Spark, with love. 💚")
