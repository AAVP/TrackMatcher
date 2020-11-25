import json
import csv
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import load_model

# Loading parameters
with open('parameters.json', 'r') as json_file:
    pm = json.load(json_file)

lyrics = []  # Here will be stored the lyrics data
emotions = []  # Here will be stored the emotions data

# Here will be stored every type of emotiom
labels = ["Anger", "Joy", "Sad", "Disgusting", "Fear", "Suprise"]

data_path = os.path.join('data', 'lyrics_dataset.csv')


def loading_data(lyrics_list, emotions_list, path):
    with open(path, 'r', encoding='utf-8') as file:
        dataset = csv.reader(file)
        next(dataset)  # We skip the header of the file

        for track in dataset:
            lyrics_list.append(track[0].capitalize())
            emotions_list.append(track[3].capitalize())


# We need to numerize the emotions
def numerize_emotions(emotions_dataset):
    for i in range(len(emotions_dataset)):
        for j in range(len(labels)):
            if emotions_dataset[i] == labels[j]:
                emotions_dataset[i] = j


loading_data(lyrics, emotions, data_path)
numerize_emotions(emotions)


# Tokenization process
tokenizer = Tokenizer(num_words=pm["num_words"], oov_token=pm["oov_tok"])
tokenizer.fit_on_texts(lyrics)  # Words are fitted on the tokenizer
word_index = tokenizer.word_index  # Words are represented by index

vocab_size = len(word_index) + 1  # The size of the vocabulary

lyrics = tokenizer.texts_to_sequences(lyrics)
lyrics = pad_sequences(
    lyrics,
    maxlen=pm["max_length"],
    padding=pm["padding_type"],
    truncating=pm["trunc_type"]
)

emotions = to_categorical(emotions, len(labels))

# Transforming the tokenized data in numpy arrays
lyrics = np.array(lyrics)
emotions = np.array(emotions)


# ---- Here you can predict the emotion of any song lyrics ----
model = load_model('model.h5')


def predict_emotion(lyrics):
    """
    It predicts the percentage of the prevalent emotions of a given lyric

    Args:
        lyrics (str): string written in English

    Returns:
        dict: dictionary obj. with the percentages
    """
    sequence = tokenizer.texts_to_sequences([lyrics])
    padded = pad_sequences(sequence,
                           maxlen=pm["max_length"],
                           padding=pm["padding_type"],
                           truncating=pm["trunc_type"])

    # prediction has the percentage of each emotion
    prediction = model.predict(padded)
    results = {}  # The keys will be the emotion name and the values will be the percentage
    for i in range(len(prediction[0])):
        results[labels[i]] = prediction[0][i]

    return results


if __name__ == '__main__':
    for emotion, percentage in predict_emotion("Then I saw her face, now I'm a believer").items():
        print(f'{emotion}: {percentage}')
