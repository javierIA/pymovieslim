import os
from scipy.io import wavfile
from scipy.io.wavfile import write
from pathlib import Path
import noisereduce as nr
import numpy as np
from pydub import AudioSegment, effects 


def removeNoise(pathaudio):
    src = pathaudio
    dst = pathaudio.replace(".mp3", ".wav")
    noise="music/noise.wav"
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")
    rate, data = wavfile.read(dst)
    # select section of data that is noise
    reduced_noise = nr.reduce_noise(y = data.T,y_noise = noise, sr=rate, thresh_n_mult_nonstationary=0.2,stationary=False)
    write(dst, rate, reduced_noise.T.astype(np.int16))
    soundmp3 = AudioSegment.from_wav(dst)
    soundmp3.export(src, format="mp3")

def normalizeAudio(audio_path,numbermusic=1,volumenvoice=0.5,volumenmusic=20):
    rawsound = AudioSegment.from_file(audio_path, "mp3")  
    normalizedsound = effects.normalize(rawsound)  
    normalizedsound.export(audio_path, format="mp3")   
    mindb = volumenmusic
    sound1 = AudioSegment.from_file(str(audio_path), format="mp3")
    sound2 = AudioSegment.from_file("music/"+str(numbermusic)+".mp3", format="mp3")
    sound1 = sound1+volumenvoice
    overlay = sound1.overlay(sound2 - int(mindb)  , position=0)
    overlay.export(audio_path, format="mp3")
    audio_path = Path(audio_path)