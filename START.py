from tkinter import *
from RUN import *
from STOP_AND_CLEAR import *

class START:
    def __init__(self, master):
        
        self.master = master
        master.title("")
        
        self.label = Label(master, text="WEB BLOCK")
        self.label.pack()

        self.greet_button = Button(master, text="RUN", command=RUN.run)
        self.greet_button.pack()
        
        self.clear_button = Button(master, text="STOP", command=STOP_AND_CLEAR.stop_and_clear)
        self.clear_button.pack()
        
        self.close_button = Button(master, text="EXIT", command=master.quit)
        self.close_button.pack()
           
        
        
root = Tk()
root.geometry("250x120") 
my_gui = START(root)
root.mainloop()
