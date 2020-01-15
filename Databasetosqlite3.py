from tkinter import *
import sqlite3 as db

conn = db.connect('saveit.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS DATA
      (
         Fname TEXT,
         Lname TEXT
       )''')
cur.close()
conn.commit()
conn.close()

def put():
    conn= db.connect('saveit.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO DATA VALUES('%s', '%s')"%(fname.get(), lname.get()))
    cur.close()
    conn.commit()
    conn.close()

master = Tk()


fname = StringVar()
lname = StringVar()
status = StringVar()


Label(master, text='First Name: ').grid(row=0, column=0)
Label(master, text='Last Name: ').grid(row=1, column=0)
Label(master, text='',textvariable=status).grid(row=3, columnspan=2)

Entry(master, textvariable=fname).grid(row=0, column=1)
Entry(master, textvariable=lname).grid(row=1, column=1)


Button(master, text='Sumbit', command=put).grid(row=2, columnspan=2)

mainloop()

