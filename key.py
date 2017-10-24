# from Tkinter import *
from pynput import keyboard 
import time
import sys

letter = []
end = 'o'

def s():
	global letter
	def callb(key):
		global end;
		ti1 = time.time() - t
		ti1 = str(ti1) #converting float value to string
		ti2 = ti1[0:5] #cutting the seconds ( time ) , without it , it will print like 0.233446546
		#print("The key",key,"Pressed For",ti2,'seconds')
		end = str(key)[2]
		if end != 'x':
			letter.append(str(key)[2])
			letter.append(str(ti2))
			print(str(key)[2])
			print(str(ti2))
			# letter.append(str(key)[2])
			# duration.append(ti2)
		#	print(str(key)[2])
		# 	# print(ti2)
			#print(letter)
			#sys.exit()
		return False #stop detecting more key-releases

	def callb1(key): #what to do on key-press
	    return False #stop detecting more key-presses


	while True:
		with keyboard.Listener(on_press = callb1) as listener1: #setting code for listening key-press
	    		listener1.join()

		t = time.time()

		with keyboard.Listener(on_release = callb) as listener: #setting code for listening key-release
	    		listener.join()
	    	if end == 'x':
				break

	return letter

s()
# mGui = Tk()
# ment = StringVar()
# mGui.geometry('600x300+400+200')
# mGui.title('Menu')
# mGui.mainloop()
# print(letter)
# sys.exit()
