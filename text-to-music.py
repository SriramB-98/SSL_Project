from midiutil import MIDIFile

def AddNote(x, file, track, duration, volume, channel, pitch, time):
    
    i=0
    while x[i]=='.' :
        i=i+1
    j=0
    while x[j+ len(x) -1]=='.':
        j=j-1

    
    x=x.strip('.')
    pitch += (-i -j)*12
    if x=='S':
        file.addNote(track, channel, pitch, time, duration, volume)
    elif x=='R_':
        file.addNote(track, channel, pitch + 1, time, duration, volume)
    elif x=='R':
        file.addNote(track, channel, pitch + 2, time, duration, volume)
    elif x=='G_':
        file.addNote(track, channel, pitch + 3, time, duration, volume)
    elif x=='G':
        file.addNote(track, channel, pitch + 4, time, duration, volume)
    elif x=='M':
        file.addNote(track, channel, pitch + 5, time, duration, volume)
    elif x=="M'":
        file.addNote(track, channel, pitch + 6, time, duration, volume)
    elif x=='P':
        file.addNote(track, channel, pitch + 7, time, duration, volume)
    elif x=='D_':
        file.addNote(track, channel, pitch + 8, time, duration, volume)
    elif x=='D':
        file.addNote(track, channel, pitch + 9, time, duration, volume)
    elif x=='N_':
        file.addNote(track, channel, pitch + 10, time, duration, volume)
    elif x=='N':
        file.addNote(track, channel, pitch + 11, time, duration, volume)
    elif x=='x' :
        pass
    else :
        time -= duration

    time += duration
    return time

def MusicWrite(notestring, tuningnotes, instrumentno, channel, track, tempo, volume, Safrequency, MyMIDI ):
    pitch=60
    time=0
    duration=1
    defaultduration=1
    tuningratios = {
    'S':1,
    'r1' :1.0535,
    'r2':1.0666,
    'R1':1.1111,
    'R2':1.1250,
    'g1':1.1851,
    'g2':1.2000,
    'G1':1.2500,
    'G2':1.2626,
    'M1':1.3333,
    'M2':1.3500,
    'm1':1.4062,
    'm2':1.4238,
    'P':1.5000,
    'd1':1.5802,
    'd2':1.6000,
    'D1':1.6666,
    'D2':1.6875,
    'n1':1.7777,
    'n2':1.8000,
    'N1':1.8750,
    'N2':1.8984  }

    if len(tuningnotes)!=12 :
        tuningnotes=['S','r1', 'R1', 'g2', 'G1', 'M1', 'm1', 'P', 'd2','D1','n2','N1']
        print("12 notes needed. Default values being used")

    chosennotes=[]
    i=0
    for x in tuningnotes:
        chosennotes.append((pitch+i,tuningratios[x]*Safrequency))
        chosennotes.append((pitch+i+12,tuningratios[x]*Safrequency*2))
        chosennotes.append((pitch+i-12,tuningratios[x]*Safrequency*0.5))
        i = i+1

    MyMIDI.changeNoteTuning(track, chosennotes)

    notes = notestring.split(" ")

    notes.append('EOF')

    MyMIDI.addTempo(track, time, tempo)
    MyMIDI.addProgramChange(track, channel, time, instrumentno)

    nandd=[]
    i=0
    while notes[i]!='EOF':
        if notes[i]=='(' :
            j=i
            while notes[j]!=')' :
                j=j+1
            duration = duration /(j-i-1)

        if notes[i]==')' :
            duration = defaultduration
            
        if notes[i+1]=='_' :
            j= i+1
            while notes[j]=='_' :
                j=j+1
            nandd.append((notes[i],duration*(j-i)))
            i=j
            
        else:
            nandd.append((notes[i],duration))
            i=i+1

    for x,d in nandd :
        time=AddNote(x, MyMIDI, track, d, volume, channel, pitch, time)

    return


test = MIDIFile(adjust_origin=True)

MusicWrite("( S R_ ) R _ _ G_ G M M' P D_ D N_ N S." , [], 40, 0, 0, 180, 100, 260, test)

with open("testmusic.mid", "wb") as output_file:
    test.writeFile(output_file)




    
