import tkinter as tk
import classes as cl
import dbtools as db

class Application:
    def __init__(self, master):
        self.master = master
        self.db = db.dbtools()  
        self.create_widgets()
        self.display_plants()
        self.display_suppliers()    

    def create_widgets(self):
        pass

    def create_plant(self):
        pass

    def create_supplier(self):
        pass

    def display_plants(self):
        pass

    def display_suppliers(self):    
        pass


