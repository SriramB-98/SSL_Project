import sys
import text_to_music
import subprocess
from subprocess import call
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from pydub import AudioSegment
from pydub.playback import play 

#Default Values
safreq = 130
instru_n = 0
volume = 100
text = ""
tabla_text = ""
tuneS = 'S'
tuner = 'r1'
tuneR = 'R1'
tuneg = 'g2'
tuneG = 'G1'
tuneM = 'M1'
tunem = 'm1'
tuneP = 'P'
tuned = 'd2'
tuneD = 'D1'
tunen = 'n2'
tuneN = 'N1'
loops = 1
tune_text = " "
channel = 0
track = 0
tempo = 60

# mix1 = "Tabla.wav"
# mix2 = "Violin.wav"
mix = []

# test = text_to_music.MIDIFile(adjust_origin=True)
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

# def mixtracks():
# 	audio1 = AudioSegment.from_file(mix[0]) #your first audio file
# 	# audio2 = AudioSegment.from_file(mix2) #your second audio file
# 	for i in range(1,len(mix)):
# 		mixed = audio1.overlay(AudioSegment.from_file(mix[i]))        #combine , superimpose audio files

# 	mixed.export("mixed.wav", format='wav') #export mixed  audio file
# 	play(mixed)


def mset():
	global safreq
	global instru_n
	global volume
	global pitch
	global text
	global tabla_text
	global tempo
	global loops

	name = instr.get()

	safreq = int(T_1.get("1.0","end-1c"))
	loops = int(T_l.get("1.0","end-1c"))
	#print(safreq)
	if(name == "Acoustic_Grand_Piano"):
		instru_n = 0
	if(name == "Acoustic_Brite_Piano"):
		instru_n = 1
	if(name == "Electric_Grand_Piano"):
		instru_n = 2
	if(name == "Electric_Piano_1"):
		instru_n = 4
	if(name == "Electric_Piano_2"):
		instru_n = 5
	if(name == "Harpsichord"):
		instru_n = 6
	if(name == "Clavinet"):
		instru_n = 7
	if(name == "Celesta"):
		instru_n = 8
	if(name == "Glockenspiel"):
		instru_n = 9
	if(name == "Xylophone"):
		instru_n = 13
	if(name == "Tubular_Bells"):
		instru_n = 14
	if(name == "Dulcimer"):
		instru_n = 15
	if(name == "Hammond_Organ"):
		instru_n = 16
	if(name == "Church_Organ"):
		instru_n = 19
	if(name == "Accordion"):
		instru_n = 21
	if(name == "Tango_Accordion"):
		instru_n = 23
	if(name == "Nylon_Guitar"):
		instru_n = 24
	if(name == "Steel_Guitar"):
		instru_n = 25
	if(name == "Jazz_Guitar"):
		instru_n = 26
	if(name == "Clean_Electric_Guitar"):
		instru_n = 27
	if(name == "Muted_Electric_Guitar"):
		instru_n = 28
	if(name == "Overdriven_Guitar"):
		instru_n = 29
	if(name == "Distortion_Guitar"):
		instru_n = 30
	if(name == "Acoustic_Bass"):
		instru_n = 32
	if(name == "Finger_Bass"):
		instru_n = 33
	if(name == "Pick_Bass"):
		instru_n = 34
	if(name == "Fretless_Bass"):
		instru_n = 35
	if(name == "Slap_Bass_1"):
		instru_n = 36
	if(name == "Slap_Bass_2"):
		instru_n = 37
	if(name == "Synth_Bass_1"):
		instru_n = 38
	if(name == "Violin"):
		instru_n = 40
	if(name == "Cello"):
		instru_n = 42
	if(name == "Tremolo_Strings"):
		instru_n = 44
	if(name == "Pizzicato_Strings"):
		instru_n = 45
	if(name == "Harp"):
		instru_n = 46
	if(name == "Timpani"):
		instru_n = 47
	if(name == "String_Ensemble"):
		instru_n = 48
	if(name == "Voice_Oohs"):
		instru_n = 53
	if(name == "Trumpet"):
		instru_n = 56
	if(name == "Trombone"):
		instru_n = 57
	if(name == "Tuba"):
		instru_n = 58
	if(name == "Muted_Trumpet"):
		instru_n = 59
	if(name == "French_Horn"):
		instru_n = 60
	if(name == "Brass_Section"):
		instru_n = 61
	if(name == "Soprano_Sax"):
		instru_n = 64
	if(name == "Alto_Sax"):
		instru_n = 65
	if(name == "Tenor_Sax"):
		instru_n = 66
	if(name == "Baritone_Sax"):
		instru_n = 67
	if(name == "Oboe"):
		instru_n = 68
	if(name == "English_Horn"):
		instru_n = 69
	if(name == "Bassoon"):
		instru_n = 70
	if(name == "Clarinet"):
		instru_n = 71
	if(name == "Piccolo"):
		instru_n = 72
	if(name == "Flute"):
		instru_n = 73
	if(name == "Recorder"):
		instru_n = 74
	if(name == "Pan_Flute"):
		instru_n = 75
	if(name == "Bottle_Blow"):
		instru_n = 76
	if(name == "Ocarina"):
		instru_n = 79
	if(name == "Square_Wave"):
		instru_n = 80
	if(name == "Charang"):
		instru_n = 84
	if(name == "New_Age"):
		instru_n = 88
	if(name == "Halo_Pad"):
		instru_n = 94
	if(name == "Sweep_Pad"):
		instru_n = 95
	if(name == "Crystal"):
		instru_n = 98
	if(name == "Goblins--Unicorn"):
		instru_n = 101
	if(name == "Echo_Voice"):
		instru_n = 102
	if(name == "Sitar"):
		instru_n = 104
	if(name == "Steel_Drums"):
		instru_n = 114

	#print(instru_n)
	volume = int(Slider_1.get())
	#print(volume)
	text = Area.get("1.0","end-1c")
	#print(text)
	tabla_text = AreaT.get("1.0" , "end-1c")
	tempo = int(Slider_3.get())
	return

def mexec():
	print(text)
	print(loops)
	print(tabla_text)
	print(safreq)
	print(instru_n)
	print(volume)
	print(tuneS)
	print(tuner)
	print(tuneR)
	print(tuneg)
	print(tuneG)
	print(tuneM)
	print(tunem)
	print(tuneP)
	print(tuned)
	print(tuneD)
	print(tunen)
	print(tuneN)
	tune_text = [tuneS, tuner , tuneR, tuneg , tuneG , tuneM , tunem , tuneP , tuned , tuneD , tunen , tuneN]
	print(tune_text)
	print(tempo)

	text_to_music.MusicWrite(text, tune_text, instru_n, channel, track, tempo, volume, safreq, "timidity1.mid")
	#text_to_music.AddTabla(tabla_text , 1 , "timidity2.mid" , safreq , tempo , channel , volume , 1)
	text_to_music.AddTabla(tabla_text,loops,"timidity2.mid",60,tempo,0,255,1)
	subprocess.call("./script.sh")
	audio1 = AudioSegment.from_file("timidity1.wav") #your first audio file
	audio2 = AudioSegment.from_file("timidity2.wav") #your second audio file


	mixed = audio1.overlay(audio2)          #combine , superimpose audio files

	mixed.export("mixed.wav", format='wav') #export mixed  audio file
	play(mixed)  
	mGui.destroy()
	# with open("testmusic.mid", "wb") as output_file:
	# 	test.writeFile(output_file)

	return

def changesa(v):
	safreq = v
	#print(safreq)
	return

def mQuit():
	mExit = messagebox.askyesno(title="Quit", message = "Are You Sure?")
	if mExit > 0:
		mGui.destroy()
	return

def fileop():
	filename = askopenfilename(initialdir = "/",title = "Select file")
	file2 = open(filename,"r")
	Area.insert("1.0",file2.read())
	file2.close()
	return

def setfile():
	def openfile1():
		global mix
		mix.append((askopenfilename( title = "Select wav file") , 1000*int(T_i.get("1.0" , "end-1c"))))


	m = Toplevel()
	m.title("Mixing wav files")
	m.geometry('300x300+100+100')
	T_i = Text(m, height=1, width=4)
	T_i.pack()
	mlabel = Label(m , text = 'Starting Time').pack()
	butt = Button(m , text = 'first file' , command = openfile1)
	butt.pack()
	butt3 = Button( m , text = 'Mix Files!' , command = lambda : combine(mix , 'wav'))
	butt3.pack()
	m.mainloop()


def create_window():

	def gett():
		global tuneS
		global tuner
		global tuneR
		global tuneg
		global tuneG
		global tuneM
		global tunem
		global tuneP
		global tuned
		global tuneD
		global tunen
		global tuneN

		tuner = btnr.get()
		tuneR = btnR.get()
		tuneg = btng.get()
		tuneG = btnG.get()
		tuneM = btnM.get()
		tunem = btnm.get()
		tuned = btnd.get()
		tuneD = btnD.get()
		tunen = btnn.get()
		tuneN = btnN.get()
		t.destroy();

	t = Toplevel()
	t.title("Tuning Notes")
	t.geometry('500x500+200+200')
	btnr = StringVar()
	btnR = StringVar()
	btng = StringVar()
	btnG = StringVar()
	btnM = StringVar()
	btnm = StringVar()
	btnd = StringVar()
	btnD = StringVar()
	btnn = StringVar()
	btnN = StringVar()

	radr1 = Radiobutton(t , text = "r1" , variable = btnr , value = 'r1')
	radr1.pack()
	radr2 = Radiobutton(t , text = "r2" , variable = btnr , value = 'r2')
	radr2.pack()
	radR1 = Radiobutton(t , text = "R1" , variable = btnR , value = 'R1')
	radR1.pack()
	radR2 = Radiobutton(t , text = "R2" , variable = btnR , value = 'R2')
	radR2.pack()

	radg1 = Radiobutton(t , text = "g1" , variable = btng , value = 'g1')
	radg1.pack()
	radg2 = Radiobutton(t , text = "g2" , variable = btng , value = 'g2')
	radg2.pack()
	radG1 = Radiobutton(t , text = "G1" , variable = btnG , value = 'G1')
	radG1.pack()
	radG2 = Radiobutton(t , text = "G2" , variable = btnG , value = 'G2')
	radG2.pack()

	radM1 = Radiobutton(t , text = "M1" , variable = btnM , value = 'M1')
	radM1.pack()
	radM2 = Radiobutton(t , text = "M2" , variable = btnM , value = 'M2')
	radM2.pack()
	radm1 = Radiobutton(t , text = "m1" , variable = btnm , value = 'm1')
	radm1.pack()
	radm2 = Radiobutton(t , text = "m2" , variable = btnm , value = 'm2')
	radm2.pack()

	radd1 = Radiobutton(t , text = "d1" , variable = btnd , value = 'd1')
	radd1.pack()
	radd2 = Radiobutton(t , text = "d2" , variable = btnd , value = 'd2')
	radd2.pack()
	radD1 = Radiobutton(t , text = "D1" , variable = btnD , value = 'D1')
	radD1.pack()
	radD2 = Radiobutton(t , text = "D2" , variable = btnD , value = 'D2')
	radD2.pack()

	radn1 = Radiobutton(t , text = "n1" , variable = btnn , value = 'n1')
	radn1.pack()
	radn2 = Radiobutton(t , text = "n2" , variable = btnn , value = 'n2')
	radn2.pack()
	radN1 = Radiobutton(t , text = "N1" , variable = btnN , value = 'N1')
	radN1.pack()
	radN2 = Radiobutton(t , text = "N2" , variable = btnN , value = 'N2')
	radN2.pack()

	mbuttont = Button(t , text = 'OK' , command = gett)
	mbuttont.pack()

	t.mainloop()


mGui = Tk()
ment = StringVar()
mGui.geometry('600x800+400+200')
mGui.title('Menu')

mlabel = Label(mGui, text = 'Music' , fg='red', bg='blue').pack()

menubar = Menu(mGui)

filemenu = Menu(menubar)
#filemenu.add_command(label="Open", command = fileop)
filemenu.add_command(label="Exit",command = mQuit)

runmenu = Menu(menubar)
runmenu.add_command(label="Run!" , command = mexec)

menubar.add_cascade(label="File",menu=filemenu)
menubar.add_cascade(label="Run",menu=runmenu)

mGui.config(menu=menubar)

Area = Text(mGui, height=8, width=20)
Area.pack()
mlabel = Label(mGui, text = 'Enter Text Here').pack()
mlabel = Label(mGui, text = 'or').pack()
mbutton = Button(mGui, text = 'Browse', command = fileop)
mbutton.pack()

mlabelblank = Label(mGui , text = ' ').pack()

AreaT = Text(mGui, height=8, width=20)
AreaT.pack()
mlabelT = Label(mGui , text = 'Enter Text Here').pack()


T_l = Text(mGui, height=1, width=4)
T_l.pack()

mlabel = Label(mGui , text = 'Number of loops in Tabla').pack()


instr = StringVar(mGui)
instr.set("Acoustic_Brite_Piano") # initial value

# option = OptionMenu(mGui, instr, "Acoustic_Grand_Piano" , "Acoustic_Brite_Piano" , "Electric_Grand_Piano" , "Electric_Piano_1" , "Electric_Piano_2" , "Harpsichord" , "Clavinet" , "Celesta" , "Glockenspiel" , "Xylophone" , "Tubular_Bells" , "Dulcimer" , "Hammond_Organ" , "Church_Organ" , "Accordion" , "Tango_Accordion" , "Nylon_Guitar" , "Steel_Guitar" , "Jazz_Guitar" , "Clean_Electric_Guitar" , "Muted_Electric_Guitar" , "Overdriven_Guitar" , "Distortion_Guitar" , "Acoustic_Bass" , "Finger_Bass" , "Pick_Bass" , "Fretless_Bass" , "Slap_Bass_1" , "Slap_Bass_2" , "Synth_Bass_1" , "Violin" , "Cello" , "Tremolo_Strings" , "Pizzicato_Strings" , "Harp" , "Timpani" , "String_Ensemble" , "Voice_Oohs" , "Trumpet", "Trombone" , "Tuba" , "Muted_Trumpet" , "French_Horn" , "Brass_Section" , "Soprano_Sax" , "Alto_Sax" , "Tenor_Sax" , "Baritone_Sax" , "Oboe" , "English_Horn" , "Bassoon" , "Clarinet" , "Piccolo" , "Flute" , "Recorder" , "Pan_Flute" , "Bottle_Blow" , "Ocarina" , "Square_Wave" , "Charang" , "New_Age" , "Halo_Pad" , "Sweep_Pad" , "Crystal" , "Goblins--Unicorn" , "Echo_Voice" , "Sitar" , "Steel_Drums")
# option.pack()
w = ttk.Combobox(mGui, textvariable=instr, values=["Acoustic_Grand_Piano" , "Acoustic_Brite_Piano" , "Electric_Grand_Piano" , "Electric_Piano_1" , "Electric_Piano_2" , "Harpsichord" , "Clavinet" , "Celesta" , "Glockenspiel" , "Xylophone" , "Tubular_Bells" , "Dulcimer" , "Hammond_Organ" , "Church_Organ" , "Accordion" , "Tango_Accordion" , "Nylon_Guitar" , "Steel_Guitar" , "Jazz_Guitar" , "Clean_Electric_Guitar" , "Muted_Electric_Guitar" , "Overdriven_Guitar" , "Distortion_Guitar" , "Acoustic_Bass" , "Finger_Bass" , "Pick_Bass" , "Fretless_Bass" , "Slap_Bass_1" , "Slap_Bass_2" , "Synth_Bass_1" , "Violin" , "Cello" , "Tremolo_Strings" , "Pizzicato_Strings" , "Harp" , "Timpani" , "String_Ensemble" , "Voice_Oohs" , "Trumpet", "Trombone" , "Tuba" , "Muted_Trumpet" , "French_Horn" , "Brass_Section" , "Soprano_Sax" , "Alto_Sax" , "Tenor_Sax" , "Baritone_Sax" , "Oboe" , "English_Horn" , "Bassoon" , "Clarinet" , "Piccolo" , "Flute" , "Recorder" , "Pan_Flute" , "Bottle_Blow" , "Ocarina" , "Square_Wave" , "Charang" , "New_Age" , "Halo_Pad" , "Sweep_Pad" , "Crystal" , "Goblins--Unicorn" , "Echo_Voice" , "Sitar" , "Steel_Drums"])#"Carrier 19EX 4667kW/6.16COP/Vanes", "Carrier 19EX 4997kW/6.40COP/Vanes", "Carrier 19EX 5148kW/6.34COP/Vanes", "Carrier 19EX 5208kW/6.88COP/Vanes", "Carrier 19FA 5651kW/5.50COP/Vanes", "Carrier 19XL 1674kW/7.89COP/Vanes", "Carrier 19XL 1779kW/6.18COP/Vanes", "Carrier 19XL 1797kW/5.69COP/Vanes", "Carrier 19XL 1871kW/6.49COP/Vanes", "Carrier 19XL 2057kW/6.05COP/Vanes", "Carrier 19XR 1076kW/5.52COP/Vanes", "Carrier 19XR 1143kW/6.57COP/VSD", "Carrier 19XR 1157kW/5.62COP/VSD", "Carrier 19XR 1196kW/6.50COP/Vanes", "Carrier 19XR 1213kW/7.78COP/Vanes", "Carrier 19XR 1234kW/5.39COP/VSD", "Carrier 19XR 1259kW/6.26COP/Vanes", "Carrier 19XR 1284kW/6.20COP/Vanes", "Carrier 19XR 1294kW/7.61COP/Vanes", "Carrier 19XR 1350kW/7.90COP/VSD", "Carrier 19XR 1403kW/7.09COP/VSD", "Carrier 19XR 1407kW/6.04COP/VSD", "Carrier 19XR 1410kW/8.54COP/VSD", "Carrier 19XR 1558kW/5.81COP/VSD", "Carrier 19XR 1586kW/5.53COP/VSD", "Carrier 19XR 1635kW/6.36COP/Vanes", "Carrier 19XR 1656kW/8.24COP/VSD", "Carrier 19XR 1723kW/8.32COP/VSD", "Carrier 19XR 1727kW/9.04COP/Vanes", "Carrier 19XR 1758kW/5.86COP/VSD", "Carrier 19XR 1776kW/8.00COP/Vanes", "Carrier 19XR 1801kW/6.34COP/VSD", "Carrier 19XR 2391kW/6.44COP/VSD", "Carrier 19XR 2391kW/6.77COP/Vanes", "Carrier 19XR 742kW/5.42COP/VSD", "Carrier 19XR 823kW/6.28COP/Vanes", "Carrier 19XR 869kW/5.57COP/VSD", "Carrier 19XR 897kW/6.23COP/VSD", "Carrier 19XR 897kW/6.50COP/Vanes", "Carrier 19XR 897kW/7.23COP/VSD", "Carrier 23XL 1062kW/5.50COP/Valve", "Carrier 23XL 1108kW/6.92COP/Valve", "Carrier 23XL 1196kW/6.39COP/Valve", "Carrier 23XL 686kW/5.91COP/Valve", "Carrier 23XL 724kW/6.04COP/Vanes", "Carrier 23XL 830kW/6.97COP/Valve", "Carrier 23XL 862kW/6.11COP/Valve", "Carrier 23XL 862kW/6.84COP/Valve", "Carrier 23XL 865kW/6.05COP/Valve", "Carrier 30RB100 336.5kW/2.8COP", "Carrier 30RB110 371kW/2.8COP", "Carrier 30RB120 416.4kW/2.8COP", "Carrier 30RB130 447.7kW/2.8COP", "Carrier 30RB150 507.8kW/2.8COP", "Carrier 30RB160 538kW/2.9COP", "Carrier 30RB170 585.5kW/2.8COP", "Carrier 30RB190 662.9kW/2.8COP", "Carrier 30RB210 710kW/2.9COP", "Carrier 30RB225 753.3kW/2.8COP", "Carrier 30RB250 836.2kW/2.8COP", "Carrier 30RB275 915kW/2.8COP", "Carrier 30RB300 993.8kW/2.8COP", "Carrier 30RB315 1076.1kW/2.9COP", "Carrier 30RB330 1123.6kW/2.8COP", "Carrier 30RB345 1170.7kW/2.8COP", "Carrier 30RB360 1248.4kW/2.8COP", "Carrier 30RB390 1325.8kW/2.8COP", "Carrier 30RB90 303.8kW/2.9COP", "Carrier 30XA100 330.1kW/3.1COP", "Carrier 30XA110 359.9kW/3COP", "Carrier 30XA120 389kW/3COP", "Carrier 30XA140 466.7kW/3.1COP", "Carrier 30XA160 535.1kW/3.1COP", "Carrier 30XA180 601.9kW/3.1COP", "Carrier 30XA200 681.7kW/3.1COP", "Carrier 30XA220 743.7kW/3.1COP", "Carrier 30XA240 801.6kW/3COP", "Carrier 30XA260 881.7kW/3.1COP", "Carrier 30XA280 943.4kW/3.1COP", "Carrier 30XA300 1010.2kW/3.1COP", "Carrier 30XA325 1077.4kW/3.1COP", "Carrier 30XA350 1138.7kW/3COP", "Carrier 30XA400 1348kW/3COP", "Carrier 30XA450 1499.5kW/2.9COP", "Carrier 30XA500 1609.4kW/2.9COP", "Carrier 30XA80 265.5kW/2.9COP", "Carrier 30XA90 297.8kW/3.1COP", "DOE-2 Centrifugal/5.50COP", "DOE-2 Reciprocating/3.67COP", "McQuay AGZ010BS 34.5kW/2.67COP", "McQuay AGZ013BS 47.1kW/2.67COP", "McQuay AGZ017BS 54.5kW/2.67COP", "McQuay AGZ020BS 71kW/2.67COP", "McQuay AGZ025BS 78.1kW/2.67COP", "McQuay AGZ025D 96kW/2.81COP", "McQuay AGZ029BS 95.7kW/2.67COP", "McQuay AGZ030D 111.1kW/2.81COP", "McQuay AGZ034BS 117.1kW/2.61COP", "McQuay AGZ035D 122.7kW/2.93COP", "McQuay AGZ040D 133.3kW/2.96COP", "McQuay AGZ045D 149.8kW/3.02COP", "McQuay AGZ050D 169.2kW/2.96COP", "McQuay AGZ055D 181.5kW/2.93COP", "McQuay AGZ060D 197.3kW/2.87COP", "McQuay AGZ065D 204.3kW/3.02COP", "McQuay AGZ070D 225.4kW/2.84COP", "McQuay AGZ075D 257.1kW/2.93COP", "McQuay AGZ080D 285.2kW/2.87COP", "McQuay AGZ090D 313.7kW/2.87COP", "McQuay AGZ100D 351kW/2.81COP", "McQuay AGZ110D 373.1kW/2.87COP", "McQuay AGZ125D 411.8kW/2.87COP", "McQuay AGZ130D 455.8kW/2.81COP", "McQuay AGZ140D 479kW/2.99COP", "McQuay AGZ160D 539.1kW/2.93COP", "McQuay AGZ180D 605.6kW/2.81COP", "McQuay AGZ190D 633.4kW/2.96COP", "McQuay PEH 1030kW/8.58COP/Vanes", "McQuay PEH 1104kW/8.00COP/Vanes", "McQuay PEH 1231kW/6.18COP/Vanes", "McQuay PEH 1635kW/7.47COP/Vanes", "McQuay PEH 1895kW/6.42COP/Vanes", "McQuay PEH 1934kW/6.01COP/Vanes", "McQuay PEH 703kW/7.03COP/Vanes", "McQuay PEH 819kW/8.11COP/Vanes", "McQuay PFH 1407kW/6.60COP/Vanes", "McQuay PFH 2043kW/8.44COP/Vanes", "McQuay PFH 2124kW/6.03COP/Vanes", "McQuay PFH 2462kW/6.67COP/Vanes", "McQuay PFH 3165kW/6.48COP/Vanes", "McQuay PFH 4020kW/7.35COP/Vanes", "McQuay PFH 932kW/5.09COP/Vanes", "McQuay WDC 1973kW/6.28COP/Vanes", "McQuay WSC 1519kW/7.10COP/Vanes", "McQuay WSC 1751kW/6.73COP/Vanes", "McQuay WSC 471kW/5.89COP/Vanes", "McQuay WSC 816kW/6.74COP/Vanes", "Multistack MS 172kW/3.67COP/None", "Trane CGAM100 337.6kW/3.11COP", "Trane CGAM110 367.2kW/3.02COP"])
w.pack()

Slider_1 = Scale(mGui, orient=HORIZONTAL, length = 127 , from_=0,to=127)
Slider_1.pack()
mlabel = Label(mGui, text = 'Volume').pack()	
Slider_3 = Scale(mGui, orient=HORIZONTAL, length = 255 , from_=0,to=255)
Slider_3.pack()
mlabel = Label(mGui, text = 'Tempo').pack()
mlabel = Label(mGui , text = ' ').pack()
T_1 = Text(mGui, height=1, width=4)
T_1.pack()

mlabel = Label(mGui , text = 'Sa frequency').pack()
# spinbox1 = Spinbox(mGui,from_=-6,to=5).pack()
# mlabel = Label(mGui , text = 'Transpose').pack()
# mlabel = Label(mGui , text = ' ').pack()
# Tuning = Text(mGui, height = 4 , width = 24)
# Tuning.insert(END,"S,r1,R1,g2,G1,M1,m1,P,d2,D1,n2,N1,")
# Tuning.pack()

# mtuning = Label(mGui , text= 'Tuning Notes').pack()
# mtuning = Label(mGui , text= '').pack()

mbutton = Button(mGui, text = 'OK', command = mset )
mbutton.pack()


mbutton2 = Button(mGui , text = 'Tuning Notes' , command = create_window)
mbutton2.pack()

mbuttonmix = Button(mGui , text = 'Mix Tracks' , command = setfile)
mbuttonmix.pack()


#List1 = Listbox(mGui)
#List1.pack()
# mild = Radiobutton(mGui, text='Mild')
# mild.config(indicatoron=0, bd=4, width=12, value='Mild')
# mild.grid(row=0, column=0)

# medium = Radiobutton(mGui , text='Medium')
# medium.config(indicatoron=0, bd=4, width=12, value='Medium')
# medium.grid(row=0, column=1)

# hot = Radiobutton(mGui, text='Hot')
# hot.config(indicatoron=0, bd=4, width=12, value='Hot')
# hot.grid(row=0, column=2)


mGui.mainloop()



#text_to_music.MusicWrite("S R x G M P x D N S. R. G. M. P. D. N. S.." , [], 0, 0, 0, 180, 100, 130, test)

# with open("testmusic.mid", "wb") as output_file:
# 	test.writeFile(output_file)


