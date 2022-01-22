from jina import DocumentArray, Flow

from jina.types.document.generators import from_files

import os
import csv
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def save_song_from_track(sp, track_id):
    try:
        track = sp.track(track_id)
    except Exception:
        return

    if track["preview_url"] is None:
        return

    try:
        res = requests.get(track["preview_url"])
    except Exception:
        return

    if not res.ok or not res.content:
        return

    with open(f"data/{track_id}.mp3", "wb") as f:
        f.write(res.content)


def generate_data():
    if not os.path.exists("data"):
        os.makedirs("data")

    if len(os.listdir("data")) != 0:
        print("Data alredy present")
        return

    print("Populating data")

    auth_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(auth_manager=auth_manager)

    with open("genres_v2.csv") as f:
        TOTAL_LIMIT = 15
        curr_limit = 0
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            save_song_from_track(sp, row["id"])
            curr_limit += 1
            if curr_limit > TOTAL_LIMIT:
                break

    print("Data populated!")


def check_query(resp):
    for d in resp.docs:
        print(f"{d.uri}, {len(d.chunks)}")
        for m in d.matches:
            print(f'+- {m.uri}: {m.scores["cosine"].value:.6f}, {m.tags}')


def main():
    generate_data()
    docs = DocumentArray(from_files("data/*.mp3"))

    f = Flow.load_config("flow.yml")
    with f:
        f.post(on="/index", inputs=docs)
        f.post(on="/search", inputs=docs, on_done=check_query)
        f.protocol = "http"
        f.cors = True
        f.block()


if __name__ == "__main__":
    main()
