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

# At first we need to load the data
training_lyrics = []  # Here will be stored the lyrics data
training_emotions = []  # Here will be stored the emotions data
testing_lyrics = []
testing_emotions = []

# Here will be stored every type of emotiom
labels = ["Anger", "Joy", "Sad", "Disgusting", "Fear", "Suprise"]

training_data_path = os.path.join('data', 'training_lyrics.csv')
testing_data_path = os.path.join('data', 'testing_lyrics.csv')


def loading_data(lyrics_list, emotions_list, path):
    with open(path, 'r', encoding='utf-8') as file:
        dataset = csv.reader(file)
        next(dataset)  # We skip the header

        for track in dataset:
            lyrics_list.append(track[0].capitalize())
            emotions_list.append(track[3].capitalize())


# We need to numerize the emotions
def numerize_emotions(emotions_dataset):
    for i in range(len(emotions_dataset)):
        for j in range(len(labels)):
            if emotions_dataset[i] == labels[j]:
                emotions_dataset[i] = j


loading_data(training_lyrics, training_emotions, training_data_path)
loading_data(testing_lyrics, testing_emotions, testing_data_path)
numerize_emotions(training_emotions)
numerize_emotions(testing_emotions)


# Tokenization process
tokenizer = Tokenizer(num_words=pm["num_words"], oov_token=pm["oov_tok"])
tokenizer.fit_on_texts(training_lyrics)  # Words are fitted on the tokenizer
word_index = tokenizer.word_index  # Words are represented by index

vocab_size = len(word_index) + 1  # The size of the vocabulary

training_lyrics = tokenizer.texts_to_sequences(training_lyrics)
training_lyrics = pad_sequences(
    training_lyrics,
    maxlen=pm["max_length"],
    padding=pm["padding_type"],
    truncating=pm["trunc_type"]
)

testing_lyrics = tokenizer.texts_to_sequences(testing_lyrics)
testing_lyrics = pad_sequences(
    testing_lyrics,
    maxlen=pm["max_length"],
    padding=pm["padding_type"],
    truncating=pm["trunc_type"]
)

training_emotions = to_categorical(training_emotions, len(labels))
testing_emotions = to_categorical(testing_emotions, len(labels))


# Transforming the tokenized data in numpy arrays
training_lyrics = np.array(training_lyrics)
training_emotions = np.array(training_emotions)
testing_lyrics = np.array(testing_lyrics)
testing_emotions = np.array(testing_emotions)


# ---- Here you can predict the emotion of any song lyrics ----
model = load_model('model.h5')
phrase = ["I am talking to the moon still trying to get to you"]
sequence = tokenizer.texts_to_sequences(phrase)
padded = pad_sequences(sequence,
                       maxlen=pm["max_length"],
                       padding=pm["padding_type"],
                       truncating=pm["trunc_type"])
print(model.predict(padded))
print(model.predict(padded).argmax())
