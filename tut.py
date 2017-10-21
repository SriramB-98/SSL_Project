import sys
import text_to_music
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename


#Default Values
safreq = 130
instru_n = 0
volume = 100
text = ""

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

tune_text = " "
channel = 0
track = 0
tempo = 60

test = text_to_music.MIDIFile(adjust_origin=True)


def mset():
	global safreq
	global instru_n
	global volume
	global pitch
	global text
	global tempo


	safreq = int(T_1.get("1.0",END))
	#print(safreq)
	instru_n = int(T_2.get("1.0",END))
	#print(instru_n)
	volume = int(Slider_1.get())
	#print(volume)
	text = Area.get("1.0",END)
	#print(text)
	tempo = int(Slider_3.get())
	return

def mexec():
	
	# if mfinal > 0:
	print(text)
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

# Tuning = Text(mGui, height = 4 , width = 24)
# Tuning.insert(END,"S,r1,R1,g2,G1,M1,m1,P,d2,D1,n2,N1,")
# Tuning.pack()

# mtuning = Label(mGui , text= 'Tuning Notes').pack()
# mtuning = Label(mGui , text= '').pack()

mbutton = Button(mGui, text = 'OK', command = mset )
mbutton.pack()


mbutton2 = Button(mGui , text = 'Tuning Notes' , command = create_window)
mbutton2.pack()
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

with open("testmusic.mid", "wb") as output_file:
	test.writeFile(output_file)

