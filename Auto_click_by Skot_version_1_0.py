import tkinter as tk
import pynput
import time
import threading as TH
import pyautogui
import os

running = False
click_function_on = False
T = 0.02 #Click Delay
clicking = False
open = True
mouse = pynput.mouse.Controller()

root1 = tk.Tk()
root1.title("Auto Click by Zero")

def working():
    global T,running
    while True:
        while running:

            if clicking:
                mouse.click(pynput.mouse.Button.left, 1)
            time.sleep(T)

def text_set():
    global running,open,clicking

    while True:
        if running:
            Label1.config(text="Now Working")
            btn_start.config(text="Stop")
            #btn_start.config(bg='white', fg = 'green',font = "RSU", text="Stop")
            Label2.config(text = "Press 1 to click", bg = "white")
            Label2_1.config(text = "Press 2 to Set Delay Time", bg = 'white')
            if click_function_on:
                Label3.config(text = "Press C to Left-Click", bg = "white")
                Label4.config(text = "Press V to Right-Click", bg = "white")
                Label5.config(text = "Press ESC to Stop WOrking", bg = "white")
            else:
                Label3.config(text="", bg= "white")
                Label4.config(text="", bg= "white")
                Label5.config(text="", bg= "white")

            if clicking:
                Label6.config(text="NOW CLICKING")
            else:
                Label6.config(text="")


        else:
            Label1.config(text="Now SLeeping")
            btn_start.config(text="Start")
            #btn_start.config(bg='white', fg = 'green', text="Start")
            Label2.config(text="", bg= "white")
            Label2_1.config(text="", bg= "white")
            Label3.config(text="", bg= "white")
            Label4.config(text="", bg= "white")
            Label5.config(text="", bg= "white")
            Label6.config(text="", bg= "white")
        
        if not(open):
            print("Already break")
            break

    return False

def running_set_buton():
    global running,clicking
    clicking = False
    running = not running

def set_running_keyboard(key):
    global clicking, running, click_function_on
    if key == pynput.keyboard.KeyCode(char='1') and running: #Start_clicking
        clicking = not clicking
        # if clicking == True:
        #     print("Clicking!  ", end=("\r"))
        # elif clicking == False:
        #     print("Break Time!", end=("\r"))
 
    elif key == pynput.keyboard.Key.esc and running:
        running = False
        print("Stop Working")
 
    elif key == pynput.keyboard.KeyCode(char='2') and running:
        click_function_on = not click_function_on
    
    if click_function_on:
        if key == pynput.keyboard.KeyCode(char='c') and running: #right click
            pyautogui.click()
        elif key == pynput.keyboard.KeyCode(char='v') and running: #left_click
            pyautogui.rightClick()


Label1 = tk.Label(root1, text = "Click", bg = "white", font = 30)
Label1.pack(padx = 5, pady = 10)
 
btn_start = tk.Button(root1, text = "Click Me To Start" ,command = running_set_buton)
btn_start.pack(padx = 5, pady = 10)
 
Label2 = tk.Label(root1)
Label2.pack(padx = 5, pady = 10)
Label2_1 = tk.Label(root1)
Label2_1.pack(padx = 5, pady = 10)
Label3 = tk.Label(root1)
Label3.pack(padx = 5, pady = 10)
Label4 = tk.Label(root1)
Label4.pack(padx = 5, pady = 10)
Label5 = tk.Label(root1)
Label5.pack(padx = 5, pady = 10)
Label6 = tk.Label(root1)
Label6.pack(padx= 5, pady= 10)

listener = pynput.keyboard.Listener(on_press=set_running_keyboard)
listener.start() #keyboard listener

threading_text_set = TH.Thread(target=text_set)
threading_text_set.start() #text config

threading_working = TH.Thread(target=working)
threading_working.start() #clicking_check

root1.geometry("700x500+100+100")
root1.mainloop()

os._exit(os.X_OK)