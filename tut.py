import sys
import text_to_music
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename


#Default Values
safreq = 130;
instru_n = 0;
volume = 100;
pitch = 60;
text = "";
tune_text = "";
channel = 0;
track = 0;
tempo = 60;

test = text_to_music.MIDIFile(adjust_origin=True)


def mset():
	global safreq
	global instru_n
	global volume
	global pitch
	global text
	global tune_text
	global tempo



	safreq = int(T_1.get("1.0",END))
	#print(safreq)
	instru_n = int(T_2.get("1.0",END))
	#print(instru_n)
	volume = int(Slider_1.get())
	#print(volume)
	pitch = int(Slider_2.get())
	#print(pitch)
	text = Area.get("1.0",END)
	#print(text)
	tune_text = Tuning.get("1.0",END).split(',')
	tune_text.pop()

	print(tune_text)
	tempo = int(Slider_3.get())
	return

def mexec():
	
	# if mfinal > 0:
	print(text)
	print(safreq)
	print(instru_n)
	print(volume)
	print(pitch)
	print(tune_text)
	print(tempo)
	text_to_music.MusicWrite(text, tune_text, instru_n, channel, track, tempo, volume, safreq, test)
	with open("testmusic.mid", "wb") as output_file:
		test.writeFile(output_file)
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

Area = Text(mGui, height=10, width=25)
Area.pack()
mlabel = Label(mGui, text = 'Enter Text Here').pack()
mlabel = Label(mGui, text = 'or').pack()

mbutton = Button(mGui, text = 'Browse', command = fileop)
mbutton.pack()


Slider_1 = Scale(mGui, orient=HORIZONTAL, length = 127 , from_=0,to=127)
Slider_1.pack()
mlabel = Label(mGui, text = 'Volume').pack()
mlabel = Label(mGui , text = ' ').pack()
Slider_2 = Scale(mGui, orient=HORIZONTAL, length = 127 , from_=0,to=127)
Slider_2.pack()
mlabel = Label(mGui, text = 'Pitch').pack()
mlabel = Label(mGui , text = ' ').pack()
Slider_3 = Scale(mGui, orient=HORIZONTAL, length = 255 , from_=0,to=255)
Slider_3.pack()
mlabel = Label(mGui, text = 'Tempo').pack()
mlabel = Label(mGui , text = ' ').pack()
T_1 = Text(mGui, height=1, width=4)
T_1.pack()

mlabel = Label(mGui , text = 'Sa frequency').pack()
mlabel = Label(mGui , text = ' ').pack()
# spinbox1 = Spinbox(mGui,from_=-6,to=5).pack()
# mlabel = Label(mGui , text = 'Transpose').pack()
# mlabel = Label(mGui , text = ' ').pack()
T_2 = Text(mGui, height=1, width=4)
T_2.pack()
mlabel = Label(mGui , text = 'Instrument Number').pack()
mlabel = Label(mGui , text = ' ').pack()

Tuning = Text(mGui, height = 4 , width = 24)
Tuning.insert(END,"S,r1,R1,g2,G1,M1,m1,P,d2,D1,n2,N1,")
Tuning.pack()

mtuning = Label(mGui , text= 'Tuning Notes').pack()
mtuning = Label(mGui , text= '').pack()

mbutton = Button(mGui, text = 'OK', command = mset )
mbutton.pack()

mGui.mainloop()



#text_to_music.MusicWrite("S R x G M P x D N S. R. G. M. P. D. N. S.." , [], 0, 0, 0, 180, 100, 130, test)

with open("testmusic.mid", "wb") as output_file:
	test.writeFile(output_file)

