import streamlit as st

st.set_page_config(
    page_title="Footistcs",
    page_icon="⚽",
)

st.title("Home Page")
st.markdown("<h1 style='text-align: center;'>Hello Streamlit with HTML!</h1>", unsafe_allow_html=True)
st.sidebar.success("Select a page above.")

