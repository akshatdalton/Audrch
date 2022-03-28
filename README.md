# Audrch
Audrch (Audio + Search) - Using this project one can enter an audio and search which song it is! The project is made using Jina AI which is a neural search framework.
Check the original issue [here](https://github.com/jina-ai/jina/issues/3650).

## Idea:
Create a search hinge for songs using Jina

## What it does?
Upload an audio and check which song is it!

## Tech stack used?
- Backend: Jina
- Frontend: Streamlit
- Dataset: [Kaggle dataset of songs in Spotify](https://www.kaggle.com/mrmorj/dataset-of-songs-in-spotify)

Made with ❤️

## How to use?

Note: You must have `python >= 3.7`.

Create a virtual environment

```
python -m venv audrch-venv
```

Activate the virtual environment

```
source audrch-venv/bin/activate
```


Download and unzip `genres_v2.csv.zip` from [Kaggle dataset of songs in Spotify](https://www.kaggle.com/mrmorj/dataset-of-songs-in-spotify) and put the file in the same directory as that of `backend/app.py`.


Follow instructions from [here](https://developer.spotify.com/documentation/general/guides/authorization/app-settings) to obtain `SPOTIPY_CLIENT_ID` and `SPOTIPY_CLIENT_SECRET`.<br>

Set the environment variables (can follow [this guide](https://spotipy.readthedocs.io/en/2.19.0/#client-credentials-flow) also):
```
export SPOTIPY_CLIENT_ID='your-spotify-client-id'
export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
```


- Run the backend:

```
python app.py
```

You can tweak `TOTAL_LIMIT` in `app.py:generate_data` to control the number of training samples.

- In another terminal, run streamlit:

```
streamlit run client/app.py
```

Now, head over to `http://localhost:8501` and you can query songs/audio of your choice!
