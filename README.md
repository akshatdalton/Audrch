# Audrch
Audrch (Audio + Search) - Using this project one can enter an audio and search which song it it! The project is make using Jina AI which is a neural search engine.
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
- Download the AudioCLIP model by running:

```
bash scripts/download_models.sh
```

- Run the backend:

```
python app.py
```

- In another terminal, run streamlit:

```
streamlit run client/app.py
```

Now, head over to `http://localhost:8501` and you can query songs/audio of your choice!
