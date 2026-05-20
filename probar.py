import tkinter as tk
from tkinter import ttk
import threading
import time



class myapp:
    def __init__(self,root:tk.Tk,title:str,mysubs,backgrounds:str,foregrounds:str,labels:str):
        self.root=root
        self.root.title(title)
        self.root.configure(background=backgrounds)
        self.progress= ttk.Progressbar(value=0)
        self.progress.pack(padx=10,pady=10)
        self.texts= tk.Text(background=backgrounds,foreground=foregrounds)
        self.texts.pack(padx=10,pady=10)
        self.texts.insert("1.0","waiting.........................................................................")
        self.label=tk.Label(text=labels,background=backgrounds,foreground=foregrounds)
        self.label.pack(padx=10,pady=10)
        self.mysubsts=mysubs
        
        self.timer=threading.Thread(target=self.mysubst)
        self.timer.start()
    def mysubst(self):
        self.mysubsts(self)
    def inserts(self,value:str,steps:int):
        self.texts.delete("1.0","end-1c")
        self.texts.insert("1.00",value)
        self.progress.step(steps)
        

def inits(mysubs,titles:str,backgrounds:str,foregrounds:str,labels:str):
    root=tk.Tk()
    apps=myapp(root,titles,mysubs,backgrounds,foregrounds,labels)
    root.mainloop()