from pydub import AudioSegment
from pydub.playback import play


def combine(x, formattype): # x is a list of tuples ( wavname, starttime) sorted according to starttime, should start with 0 
    first,second = x[0]
    mixed = AudioSegment.from_file(first)
    x.remove((first,second))
    for a,b in x :
            silence=AudioSegment.silent(duration=b-len(mixed)+1000+len(AudioSegment.from_file(a)))
            mixed = mixed+silence
            mixed = mixed.overlay(AudioSegment.from_file(a), position=b)
            
        
    mixed.export("final.wav", format=formattype) #export mixed  audio file
    play(mixed)
    return


combine([("./Tabla.wav",0),("./Violin.wav",10000)] ,'wav')
