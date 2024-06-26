from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import pickle

#laoding_models

df = pickle.load(open('df.pkl', 'rb'))
similarity = pickle.load(open('sim.pkl', 'rb'))


def recommendation(song_df):
    idx = df[df['song'] == song_df].index[0]
    distances = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])

    songs = []
    for m_id in distances[1:21]:
        songs.append(df.iloc[m_id[0]].song)

    return songs
#flask_app

app = Flask(__name__)

# paths
@app.route('/')
def index():
    names = df['song'].to_list()
    return render_template('index.html', name=names)
@app.route('/recom', methods=['POST'])
def mysong():
    user_song = request.form['names']
    songs = recommendation(user_song)
    return render_template('index.html', songs=songs)
#python

if __name__ == "__main__":
    app.run(debug=True)
