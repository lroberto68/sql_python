from tkinter import Tk, Button, Label, Entry, Frame
from tkinter import ttk


class MainWindow(Tk):
    def __init__(self):
        super().__init__()

        self.title("CRUD Database")
        self.geometry("800x600")
        self.resizable(False,False)

        self.__Create_Widget()

    def __Create_Widget(self):
        
        self.frmEntry = ttk.Frame(self)
        self.frmEntry.grid(column=0)

        self.frmBtn = ttk.Frame(self)
        self.frmBtn.grid(column=1)

        self.lblNome = ttk.Label(self.frmEntry, text="Nome")
        self.lblNome.grid(column=0, row=0, padx=20, pady=50)

        self.lblCognome = ttk.Label(self.frmEntry, text="Cognome")
        self.lblCognome.grid(column=0, row=1, padx=20)

        self.etryNome = ttk.Entry(self.frmEntry, background="white")
        self.etryNome.grid(column=1, row=0, padx=20)

        self.etryCognome = ttk.Entry(self.frmEntry, background="white")
        self.etryCognome.grid(column=1, row=1, padx=20)