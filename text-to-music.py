from midiutil import MIDIFile
import re
chosennotes=[]

def taals(x):
    if x=="Teen":
        return "Dha Dhin Dhin Dha Dha Dhin Dhin Dha Dha Tin Tin Ta Ta Dhin Dhin Dha"
    elif x=="Dadra":
        return "Dha Dhin Na Dha Tin Na"
    elif x=="Rupak":
        return "Tin Tin Na Dhin Na Dhin Na"
    elif x=="Dhamar":
        return "Ka Dhin Tta Dhin Tta Dha x Ga Ti Tta Ti Tta Ta x"
    elif x=="Jhap":
        return "Dhi Na Dhi Dhi Na Ti Na Dhi Dhi Na"
    elif x=="Ek":
        return "Dhin Dhin ( Dha Ge ) ( Ti Di Ke Tta ) Tun Na Ka Ta ( Dha Ge ) ( Ti Di Ke Tta ) Dhin Na"    
    else:
        return x


def notepitch(x):
    if x=='S':
        return 0
    elif x=='R_':
        return 1
    elif x=='R':
        return 2
    elif x=='G_':
        return 3
    elif x=='G':
        return 4
    elif x=='M':
        return 5
    elif x=="M'":
        return 6
    elif x=='P':
        return 7
    elif x=='D_':
        return 8
    elif x=='D':
        return 9
    elif x=='N_':
        return 10
    elif x=='N':
        return 11
    else:
        return -1

def AddNote(x, file, track, duration, volume, channel, pitch, time):
    global chosennotes
    n=19
    if notepitch(x)!=-1:
        file.addNote(track, channel, pitch + notepitch(x), time, duration, volume)
    elif re.search("\^",x):
        x=re.split("\^",x)

        i=0
        while x[0][i]=='.' :
            i=i+1
        j=0
        while x[0][j+ len(x[0]) -1]=='.':
            j=j-1
        start=pitch+(-i -j)*12+notepitch(x[0].strip('.'))
        i=0
        while x[1][i]=='.' :
            i=i+1
        j=0
        while x[1][j+ len(x[1]) -1]=='.':
            j=j-1
        pitch += (-i -j)*12
        end=pitch+notepitch(x[1].strip('.'))
        for a,b in chosennotes:
                if a==start:
                    startfreq=b
                if a==end:
                    endfreq=b

        ratio=endfreq/startfreq
        step=ratio**(1/n)
        meend=[]
        for k in range(1,n+1):
            meend.append((k,startfreq*step**k))
        file.changeNoteTuning(track,meend)
        for k in range(1,n+1):
            file.addNote(track, channel, k, time, duration/n, volume)
            time += duration/n
        file.changeNoteTuning(track,chosennotes)       
        time -=duration
    elif re.search("v",x):
        x=re.split("v",x)
        i=0
        while x[0][i]=='.' :
            i=i+1
        j=0
        while x[0][j+ len(x[0]) -1]=='.':
            j=j-1
        mean=pitch+(-i -j)*12+notepitch(x[0].strip('.'))
        for a,b in chosennotes:
                if a==mean:
                    meanf=b
        highf = meanf*1.04
        lowf = meanf/1.04
        file.changeNoteTuning(track,[(1,meanf),(2,highf),(3,meanf),(4,lowf)])
        endtime=time+duration
        k=0
        while time < endtime :
            file.addNote(track, channel,k%4 +1 , time, duration/(4*int(x[1])), volume)
            time += duration/(4*int(x[1]))
            k+=1
        file.changeNoteTuning(track,chosennotes)       
        time -=duration
    elif re.search("\.",x):
        i=0
        while x[i]=='.' :
            i=i+1
        j=0
        while x[j+ len(x) -1]=='.':
            j=j-1
        x=x.strip('.')
        pitch += (-i -j)*12
        file.addNote(track, channel, pitch + notepitch(x), time, duration, volume)        
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


    global chosennotes
    chosennotes=[]
    if len(tuningnotes)!=12 :
        tuningnotes=['S','r1', 'R1', 'g2', 'G1', 'M1', 'm1', 'P', 'd2','D1','n2','N1']
        print("12 notes needed. Default values being used")

    
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



def hash_swara(swar):
    if swar=='S' :
        return 0
    elif swar=='R_' :
        return 1
    elif swar=='R' :
        return 2   
    elif swar=='G_' :
        return 3
    elif swar=='G' :
        return 4
    elif swar=='M' :
        return 5
    elif swar=="M'" :
        return 6
    elif swar=='P' :
        return 7
    elif swar=='D_' :
        return 8
    elif swar=='D' :
        return 9
    elif swar=='N_' :
        return 10
    elif swar=='N' :
        return 11
    elif swar=="S." :
        return 12
    else :
        pass


def Raag_check(notestring, aarohastr, avrohastr):

    arohnotes=aarohastr.split(" ")
    avrohnotes=avrohastr.split(" ")

    avrohnotes.append('E')
    arohnotes.append('E')

    aaroha=['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
    avroha=['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']

    j=0
    while arohnotes[j+1]!='E':
        if aaroha[hash_swara(arohnotes[j])]=='a':
            aaroha[hash_swara(arohnotes[j])]=arohnotes[j+1]
        else :
            aaroha[hash_swara(arohnotes[j])]=aaroha[hash_swara(arohnotes[j])]+" "+arohnotes[j+1]
        j=j+1


    j=0
    while avrohnotes[j+1]!='E':
        if avroha[hash_swara(avrohnotes[j])]=='a':
            avroha[hash_swara(avrohnotes[j])]=avrohnotes[j+1]
        else :
            avroha[hash_swara(avrohnotes[j])]=avroha[hash_swara(avrohnotes[j])]+" "+avrohnotes[j+1]
        j=j+1

    notes=notestring.split(" ")
    notes.append('E') 


    i=0
    a=0
    b=0

    while notes[i+1]!='E':
        while notes[i+1]=='(' or notes[i+1]==')' or notes[i+1]=='_' or notes[i+1]=='.':
            i=i+1
        if notes[i+1]=='E':
            break

        c=0
        check=0
        temp_aaroha=aaroha[hash_swara(notes[i])].split(" ")
        temp_avroha=avroha[hash_swara(notes[i])].split(" ")

        temp_aaroha.append('E')
        temp_avroha.append('E')

        while temp_aaroha[c]!='E' :
            if notes[i+1]==temp_aaroha[c] :
                check=1
                break
            c=c+1

        c=0
        while temp_avroha[c]!='E' :
            if notes[i+1]==temp_avroha[c] :
                check=1
                break
            c=c+1

        if check==1 :
            a=a+1
        else :
            b=b+1
        i=i+1

    return (100*a)/(a+b)


def AddTabla(bols, loops, file, Sapitch, tempo, channel,volume, starttrack):
    pitch=Sapitch
    time=0
    duration=1
    defaultduration=1
    bols=taals(bols)
    for i in range(starttrack,starttrack+10):
        file.addTempo(i, time, tempo)

    bols=bols.split(" ")
    bols.append('EOF')
    for index in range(1,loops+1):
        i=0
        while bols[i]!='EOF':
            x=bols[i]
            if x=='(' :
                j=i
                while bols[j]!=')' :
                    j=j+1
                duration = duration /(j-i-1)
            elif x==')' :
                duration = defaultduration
            elif x=='Ti':
                file.addProgramChange(starttrack, channel, time, 116)
                file.addNote(starttrack, channel, pitch, time, duration, volume)
            if x=='Ta':
                file.addProgramChange(starttrack+1, channel, time, 115)
                file.addNote(starttrack+1, channel, pitch, time + duration/5, duration, volume-10)
            elif x=='Dha':
                file.addProgramChange(starttrack+2, channel, time, 117)
                file.addNote(starttrack+2, channel, pitch, time, duration, volume)
            elif x=='Tun':
                file.addProgramChange(starttrack+3, channel, time, 118)
                file.addNote(starttrack+3, channel, pitch, time, duration, volume)
            elif x=='Tta':
                file.addProgramChange(starttrack+4, channel, time, 119)
                file.addNote(starttrack+4, channel, pitch, time, duration, volume)
            elif x=='Dhin' or x=='Dhi':
                file.addProgramChange(starttrack+5, channel, time, 120)
                file.addNote(starttrack+5, channel, pitch, time, duration, volume)
            elif x=='Na':
                file.addProgramChange(starttrack+6, channel, time, 121)
                file.addNote(starttrack+6, channel, pitch, time, duration, volume)
            elif x=="Ga" or x=='Ge':
                file.addProgramChange(starttrack+7, channel, time, 122)
                file.addNote(starttrack+7, channel, pitch, time, duration, volume)
            elif x=='Di':
                file.addProgramChange(starttrack+8, channel, time, 123)
                file.addNote(starttrack+8, channel, pitch, time, duration, volume)
            elif x=='Ka' or x=='Ke':
                file.addProgramChange(starttrack+9, channel, time, 124)
                file.addNote(starttrack+9, channel, pitch, time, duration, volume)
            elif x=='Tin':
                file.addProgramChange(starttrack+10, channel, time, 125)
                file.addNote(starttrack+10, channel, pitch, time, duration, volume)

            elif x=='x' :
                pass
            else :
                time -= duration
            time += duration
            i+=1
    return  



test = MIDIFile(numTracks=13,adjust_origin=True)

AddTabla("Teen",1, test,60,150,0,255,1)

#MusicWrite("Sv3 _ _ _ _ _ S _", [], 40, 0, 0, 180, 100, 260, test)
#MusicWrite("( R M ) ( P D ) M G / R G S R / M _ G S / R G .N S" , [], 40, 0, 1, 150, 100, 520, test)

print( Raag_check("S R_ G_ G_ G M M' G P D_ D D_ P D M' M G G_ R" ,"S R_ R G_ G M M' G P D_ D N_ N S.","S. N N_ D D_ P D M' M G G_ R R_ S") )

with open("testmusic.mid", "wb") as output_file:
    test.writeFile(output_file)


