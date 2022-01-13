import os
import streamlit as st
from helper import get_matches

st.set_page_config(page_title="Jina Audio Search")

st.title("Audrch")

current_abs_path = os.path.abspath(os.path.dirname(__file__))

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()

    matches = get_matches(bytes_data)

    if not matches:
        st.write("No matches found :(")

    for match in matches:
        path = os.path.join(current_abs_path, "..", match["uri"])
        st.audio(path)
