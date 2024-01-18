import streamlit as st

from backend.get_url import get_todays_url

st.set_page_config(
    page_title="Welcome",
    page_icon="👋",
)

url = get_todays_url()
st.write("# [🌳](%s)" % url)


st.write("for Spark, with love. 💚")
