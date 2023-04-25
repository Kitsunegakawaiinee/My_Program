import tkinter as tk
import threading as TH
import time
import os
import pynput

root = tk.Tk()
root.title("Countdown")
root.geometry("500x200+500+260")

class program:

    def __init__ (self, root_input): #constructer
        self.window = root_input
        self.enter_time()
        self.countlabel = tk.Label(font = ("Arial", 50), bg = "black", fg="white")
        self.running = False

        self.time_get = 0 #get from Entry

    def enter_time(self): #input your start
        self.mylabel = tk.Label(self.window, text="Input your time (sec)", font = ("Arial", 11))
        self.mylabel.pack()

        listner_input = tk.StringVar()
        listner_input.set("")

        self.my_listen = tk.Entry(self.window, textvariable= listner_input)
        self.my_listen.pack()

        self.mybutton = tk.Button(self.window, text="start", font = ("Arial", 11),command= lambda: self.start_button(listner_input.get()))
        self.mybutton.pack()

        self.warnning = tk.Label(self.window,text="int only", font = ("Arial", 11))
        self.warnning.pack()

    def check_condition(self):

        if self.time_get == 0:
            self.warnning.config(text = "Can't countdown with 0 number")

        elif self.time_get < 0:
            self.warnning.config(text= "Can't countdown with negative numbers")

        elif self.time_get > 0:
            self.mylabel.pack_forget()
            self.my_listen.pack_forget()
            self.mybutton.pack_forget()
            self.warnning.pack_forget()
            self.working()

    def start_button(self, listen_input): #when click start

        #warnning_word = {"number only", "Can't countdown with negative numbers", "Can't countdown with 0 number"}

        try:
            self.time_get = int(listen_input)
            self.check_condition()
        except:
            self.warnning.config(text = "number only")

    def config_countdown(self):
        
        Text_set= tk.StringVar()

        min, sec = divmod(self.time_get, 60)
        hour, min = divmod(min, 60)
        day, hour = divmod(hour, 24)

        if (not(day == 0)):
            Text = "{:02d}:{:02d}:{:02d}:{:02d}".format(day, hour, min, sec)
            Text_set.set(Text)

        elif(not(hour == 0)):
            Text = "{:02d}:{:02d}:{:02d}".format(hour, min, sec)
            Text_set.set(Text)

        elif (not(min == 0)):
            Text = "{:02d}:{:02d}".format(min, sec)
            Text_set.set(Text)
        elif(sec):
            Text = "00:{:02d}".format(sec)
            Text_set.set(Text)

        self.countlabel.config(textvariable=Text_set)

    def start_countdown(self):
        while(self.time_get):
            self.config_countdown()
            time.sleep(1)
            self.time_get -= 1

        self.countlabel.config(text = "SHUTDOWN")
        os.system("shutdown /s /t 1") #shutdown
        os._exit(os.X_OK)

    def set_running(self, key):
        if key == pynput.keyboard.Key.esc and self.running:
            os._exit(os.X_OK)#exit
            
    def working(self):
        self.countlabel.pack()

        self.press_label = tk.Label(text= "press esc to exit", font = ("Arial", 11))
        self.press_label.pack()

        self.running = True
        thread = TH.Thread(target=self.start_countdown)
        thread.start()

        listener = pynput.keyboard.Listener(on_press=self.set_running)
        listener.start() #keyboard listener

call_class = program(root)
root.mainloop()

os._exit(os.X_OK)#exit
