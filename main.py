import librosa
import os

# Music samples from: https://www.kaggle.com/andradaolteanu/gtzan-dataset-music-genre-classification
SONGFILES = []


# list the .wav(s)
for folder in os.listdir('./data'):
    songs = len(os.listdir(f'./data/{folder}'))
    print(f'Genre: {folder} Quantity: {songs}')
    for file in os.listdir(f'./data/{folder}'):
        SONGFILES.append(f'./data/{folder}/{file}')

print(f'\nTotal: {len(SONGFILES)}')


# loop frame by frame like the stegosaurus' did back in the day...
for path in SONGFILES:
    stream = librosa.stream(path, 1, 1, 1)# https://librosa.org/doc/latest/generated/librosa.stream.html#librosa.stream
    print(f'SongStream-OBJ for {path}: {stream}')
    break


# put the stego inside the saurus
math = None