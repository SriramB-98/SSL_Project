from pynput import keyboard 
import time

letter = []
duration = []

def callb(key):
    ti1 = time.time() - t
    ti1 = str(ti1) #converting float value to string
    ti2 = ti1[0:5] #cutting the seconds ( time ) , without it , it will print like 0.233446546
    #print("The key",key,"Pressed For",ti2,'seconds')
    letter.append(key)
    duration.append(ti2)
    print(key)
    print(ti2)
    return False #stop detecting more key-releases

def callb1(key): #what to do on key-press
    return False #stop detecting more key-presses


while True:
	with keyboard.Listener(on_press = callb1) as listener1: #setting code for listening key-press
    		listener1.join()

	t = time.time()

	with keyboard.Listener(on_release = callb) as listener: #setting code for listening key-release
    		listener.join()