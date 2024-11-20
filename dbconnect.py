from tkinter import *
import cx_Oracle
from dbfunctions import display

#Connect to the TMU database
def connection(self):
        username = self.username_input.get()
        password = self.password_input.get()
        try:
            self.connection = cx_Oracle.connect(
                user=username,
                password=password,
                dsn="(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(Host=oracle.scs.ryerson.ca)(Port=1521))(CONNECT_DATA=(SID=orcl)))"
            )
            if self.connection.version:
                print(self.connection.version)
                self.cursor = self.connection.cursor()
                display(self, self.functions)
        #Avoid crashing if credentials are wrong
        except cx_Oracle.DatabaseError:
            self.login_message["text"] = "Incorrect username or password."
            self.username_input.delete(0, END)
            self.password_input.delete(0, END)
            
            
            