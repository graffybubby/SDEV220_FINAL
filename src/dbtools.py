import sqlite3 as sql
import os
import dataclasses


class dbtools:
    # initialization of the dbtools object, upon init run the create_db() function
    def __init__(self):
        self.create_connect_db()
        
    # function creates the main sqlite3 file for the program, if the file exists already it just connects.
    def create_connect_db(self):
        # connect or create main database
        self.con = sql.connect('main.db')
        # assign cursor
        self.cur = self.con.cursor()
        # If the tables don't already exist, create a table for plants and suppliers.
        self.cur.execute("CREATE TABLE IF NOT EXISTS plants(id INTEGER PRIMARY KEY, quantity INTEGER, name TEXT, description TEXT, greenhouse INTEGER, supplier_id INTEGER)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS supplier(id INTEGER PRIMARY KEY, name TEXT, address TEXT, phone TEXT)")

# this is the formatting for how data should be sent in tuple form from the respective classes.    
# data = ("plants (id, quantity ,name ,description ,greenhouse ,supplier_id)",1, 5, "rose bush", "this is a rosebush", 0, 30)  
    def add_data(self, data):  
        queary_string = ("INSERT INTO " + (data[0]) + " VALUES " + (str((data[1:]))))
        self.cur.execute(queary_string)
        self.con.commit()

    def update(self, data):
        queary_string = ("UPDATE " + (data[0]) + " SET " + (data[1]) + " = WHERE id = " + (data[2]))
        self.cur.execute(queary_string)
        self.con.commit()

    def remove_data(self, data):
        pass
    

    """ 
        concerns for find function 
        if the user inserts a sql command into one of the search values will it return more data than they need?
    """
    """
        Generel setup will be in this order: 
        find table based on class name,
        Find row based on provided ID or name,
        Find any NON ID column as requested by user,
        then finally validate and update the db based on provided info
    """
    def find(self, data):
        # data needs to pass a tuple in this order: what to select(*), class name(table), desired search(...)
        "SELECT * FROM table WHERE name = ..." # this collects all
        "SELECT id FROM table WHERE name = ..." # this collects specifically id
        queary_string = ("SELECT " + (data[0]) + " FROM " + (data[1]) + " WHERE " + (data[2]) + " = " + (data[3]))
        queary_response = self.cur.execute(queary_string)
        return queary_response





