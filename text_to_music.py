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

# MusicWrite("S R x G M P x D N S. R. G. M. P. D. N. S.." , [], 0, 0, 0, 180, 100, 130, test)
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
        chosennotes.append((pitch+i+24,tuningratios[x]*Safrequency*4))
        chosennotes.append((pitch+i-24,tuningratios[x]*Safrequency*0.25))
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


def Raag_check(notestring, aaroha=[], avroha=[]):
    notes=notestring.split(" ")
    notes.append('E')
    i=0
    print(notes)
    while notes[i+1]!='E':
        if notes[i]=='S' :
            while notes[i+1]=='(' or notes[i+1]==')' or notes[i+1]=='_' or notes[i+1]=='.':
                i=i+1
            if notes[i+1]!=aaroha[0] and notes[i+1]!=avroha[0]:
                print(i)
                break
        elif notes[i]=='R_' :
            while notes[i+1]=='(' or notes[i+1]==')' or notes[i+1]=='_' or notes[i+1]=='.':
                i=i+1
            if notes[i+1]!=aaroha[1] and notes[i+1]!=avroha[1]:
                print(i)
                break
        elif notes[i]=='R' :
            while notes[i+1]=='(' or notes[i+1]==')' or notes[i+1]=='_' or notes[i+1]=='.':
                i=i+1
            if notes[i+1]!=aaroha[2] and notes[i+1]!=avroha[2]:
                print(i)
                break
        elif notes[i]=='G_' :
            while notes[i+1]=='(' or notes[i+1]==')' or notes[i+1]=='_' or notes[i+1]=='.':
                i=i+1
            if notes[i+1]!=aaroha[3] and notes[i+1]!=avroha[3]:
                print(i)
                break
        elif notes[i]=='G' :
            while notes[i+1]=='(' or notes[i+1]==')' or notes[i+1]=='_' or notes[i+1]=='.':
                i=i+1
            if notes[i+1]!=aaroha[4] and notes[i+1]!=avroha[4]:
                print(i)
                break
        elif notes[i]=='M' :
            while notes[i+1]=='(' or notes[i+1]==')' or notes[i+1]=='_' or notes[i+1]=='.':
                i=i+1
            if notes[i+1]!=aaroha[5] and notes[i+1]!=avroha[5]:
                print(i)
                print(aaroha[5])
                print(notes[i+1])
                break
        elif notes[i]=="M'" :
            while notes[i+1]=='(' or notes[i+1]==')' or notes[i+1]=='_' or notes[i+1]=='.':
                i=i+1
            if notes[i+1]!=aaroha[6] and notes[i+1]!=avroha[6]:
                print(i)
                print("M'")
                break
        elif notes[i]=='P' :
            while notes[i+1]=='(' or notes[i+1]==')' or notes[i+1]=='_' or notes[i+1]=='.':
                i=i+1
            if notes[i+1]!=aaroha[7] and notes[i+1]!=avroha[7]:
                print(i)
                break
        elif notes[i]=='D_' :
            while notes[i+1]=='(' or notes[i+1]==')' or notes[i+1]=='_' or notes[i+1]=='.':
                i=i+1
            if notes[i+1]!=aaroha[8] and notes[i+1]!=avroha[8]:
                print(i)
                break
        elif notes[i]=='D' :
            while notes[i+1]=='(' or notes[i+1]==')' or notes[i+1]=='_' or notes[i+1]=='.':
                i=i+1
            if notes[i+1]!=aaroha[9] and notes[i+1]!=avroha[9]:
                print(i)
                break
        elif notes[i]=='N_' :
            while notes[i+1]=='(' or notes[i+1]==')' or notes[i+1]=='_' or notes[i+1]=='.':
                i=i+1
            if notes[i+1]!=aaroha[10] and notes[i+1]!=avroha[10]:
                print(i)
                break
        elif notes[i]=='N' :
            while notes[i+1]=='(' or notes[i+1]==')' or notes[i+1]=='_' or notes[i+1]=='.':
                i=i+1
            if notes[i+1]!=aaroha[11] and notes[i+1]!=avroha[11]:
                print(i)
                print(notes[i+1])
                print(aaroha[11])
                print('E')
                break
        else:
            pass

        i=i+1


    if notes[i+1]=='E':
        return True
    else:
        return False

def AddTabla(bols, file, Safrequency, tempo, channel,volume):
    pitch=60
    time=0
    duration=1
    defaultduration=1
    for i in range(1,11):
        file.addTempo(i, time, tempo)

    bols=bols.split(" ")
    print(bols)


    for x in bols:
        if x=='Ta':
            file.addProgramChange(1, channel, time, 116)
            file.addNote(1, channel, pitch, time, duration, volume)
        elif x=='Dha':
            file.addProgramChange(2, channel, time, 117)
            file.addNote(2, channel, pitch, time, duration, volume)
        elif x=='Tun':
            file.addProgramChange(3, channel, time, 118)
            file.addNote(3, channel, pitch, time, duration, volume)
        elif x=='Tta':
            file.addProgramChange(4, channel, time, 119)
            file.addNote(4, channel, pitch, time, duration, volume)
        elif x=='Dhin':
            file.addProgramChange(5, channel, time, 120)
            file.addNote(5, channel, pitch, time, duration, volume)
        elif x=='Na':
            file.addProgramChange(6, channel, time, 121)
            file.addNote(6, channel, pitch, time, duration, volume)
        elif x=="Ga" or x=='Ge':
            file.addProgramChange(7, channel, time, 122)
            file.addNote(7, channel, pitch, time, duration, volume)
        elif x=='Di':
            file.addProgramChange(8, channel, time, 123)
            file.addNote(8, channel, pitch, time, duration, volume)
        elif x=='Ka' or x=='Ke':
            file.addProgramChange(9, channel, time, 124)
            file.addNote(9, channel, pitch, time, duration, volume)
        elif x=='Tin':
            file.addProgramChange(10, channel, time, 125)
            file.addNote(10, channel, pitch, time, duration, volume)
        elif x=='x' :
            pass
        else :
            time -= duration
        time += duration
    return  






# test = MIDIFile(adjust_origin=True)

# MusicWrite("S R x G M P x D N S. R. G. M. P. D. N. S.." , [], 0, 0, 0, 180, 100, 520, test)

# # print( Raag_check("S R_ R G_ G M M' P D_ D N_ N" , ['R_' , 'R','G_', 'G' , 'M', "M'",'P','D_', 'D' , 'N_', 'N', 'a'],['a', 'S', 'R_', 'R', 'G_', 'G', 'M', "M'", 'P','D_','D','N_']))

#AddTabla("Dha Dhin Dhin Dha Dha Dhin Dhin Dha Dha Tin Tin Na Na Dhin Dhin Dha",test,262,200,0,100)
# with open("testmusic.mid", "wb") as output_file:
#     test.writeFile(output_file)


