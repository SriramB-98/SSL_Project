import sys
import text_to_music
import subprocess
from subprocess import call
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.filedialog import askopenfilename

L = []
Full = []

def set():
	global L
	global Full
	L = text_to_music.Raag_result(Area.get("1.0" , "end-1c") , 80)
	Full = text_to_music.Raag_result(Area.get("1.0" , "end-1c") , 0)
	#print(L)
	return

def display():
	m = Toplevel()
	m.title("Possible List of Ragas")
	m.geometry('300x300+100+100')
	global L
	global Full
	print(Full)
	if len(L) == 0:
		mlabel = Label(m , text = "No particular Raga is strongly followed").pack()
	else:
		for i in range(int(len(L)/2)):
			mlabel = Label(m , text = L[2*i] + " : " + str(L[2*i+1])).pack()

	m.mainloop()

def fileop():
	filename = askopenfilename(title = "Select file")
	file2 = open(filename,"r")
	Area.insert("1.0",file2.read())
	file2.close()
	return

mGui = Tk()
ment = StringVar()
mGui.geometry('600x800+400+200')
mGui.title('Menu')

Area = Text(mGui, height=8, width=20)
Area.pack()
mlabel = Label(mGui, text = 'Enter Text Here').pack()
mlabel = Label(mGui, text = 'or').pack()
mbutton2 = Button(mGui, text = 'Browse', command = fileop)
mbutton2.pack()

mbutton = Button(mGui, text = 'Set this as my text!', command = set)
mbutton.pack()

mbutton1 = Button(mGui , text = 'Run' , command = display)
mbutton1.pack()

mGui.mainloop()