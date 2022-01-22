import os
from pathlib import Path
import streamlit as st
from helper import get_matches

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

st.set_page_config(page_title="Jina Audio Search")

st.title("Audrch")

current_abs_path = os.path.abspath(os.path.dirname(__file__))


def get_track_id(path):
    return Path(path).stem


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()

    matches = get_matches(bytes_data)

    if not matches:
        st.write("No matches found :(")

    auth_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(auth_manager=auth_manager)

    for match in matches:
        path = os.path.join(current_abs_path, "..", match["uri"])
        track_id = get_track_id(match["uri"])

        try:
            track = sp.track(track_id)
        except Exception:
            continue

        if "spotify" not in track["external_urls"]:
            continue

        name = track["name"]
        url = track["external_urls"]["spotify"]
        img = track["album"]["images"][-1]["url"]

        container = st.container()
        container.write(name)
        container.image(img)
        container.audio(path)
        container.markdown(
            f'[Click Here to open in Spotify]({url})', unsafe_allow_html=True
        )
