
from pydub import AudioSegment
from pydub.playback import play

audio1 = AudioSegment.from_file("Tabla.wav") #your first audio file
audio2 = AudioSegment.from_file("Violin.wav") #your second audio file


mixed = audio1.overlay(audio2)          #combine , superimpose audio files

mixed.export("mixed.wav", format='wav') #export mixed  audio file
play(mixed)  
