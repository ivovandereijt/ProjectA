# te doen:
# schrijf de info en recensie naar de database
# Maak de vragen die nodig zijn die opgeslagen moeten worden in de database
#problemen:
#naam gaat weg bij het loginscherm als die nog een keer ingevuld moet worden
#alle tekst van de vorrige persoon staat er nog als die nog een keer inguld moet worden

from tkinter import *  # Tkinder import
from tkinter.messagebox import showinfo  # Import popups
from time import time, ctime
import psycopg2
from random import randrange

def data_connectie():
    try:
        con = psycopg2.connect(
            host='localhost',  # De host waarop je database runt
            database='TEST_twitterzuil',  # Database naam
            user='postgres',  # Als wat voor gebruiker je connect, standaard postgres als je niets veranderd
            password='wittekop'  # Wachtwoord die je opgaf bij installatie
            # port=5432 runt standaard op deze port en is alleen nodig als je de port handmatig veranderd
        )
        cur = con.cursor()
    except:
        print("fout in connectie")
    t = time()
    realtime = ctime(t)
    DB_student = vraag2.get()
    DB_idnummer = randrange(1000)
    DB_naam = loginfield.get()
    DB_woonplaats = vraag3.get()
    DB_recentie = rec.get()
    DB_datum = ctime(t)
    if DB_naam == "":
        DB_naam = "Anoniem"
    try:
        sql = "insert into reiziger (idnummer, naam, student, woonplaats, recentie, datum) values (%s, %s, %s, %s, %s, %s)"
        val = DB_idnummer, DB_naam, DB_student, DB_woonplaats, DB_recentie, DB_datum
        cur.execute(sql, val)
        cur.execute("delete from reiziger where recentie='';")
        con.commit()
    except:
        print("fout in versturen van data")
    try:
        cur.execute("select * FROM reiziger")

        myresult = cur.fetchall()

        for x in myresult:
            print(x)
    except:
        print("Kan overzicht niet laten zien")

def toonLoginFrame():  # Beeld1
    #info van loginfield.get(), vraag2.get(), vraag3.get()
    t = time()
    realtime = ctime(t)
    with open('data.txt','w') as f:
        f.write("\n" +"Naam:" + loginfield.get() + '\n')
        f.write("datum: " + ctime(t) + "\n")
        f.write("student: " + vraag2.get() + "\n")
        f.write("Woonplaats: " + vraag3.get() +"\n")
        f.write("recentie: " + rec.get() +"\n")
    print(loginfield.get())
    print(ctime(t))
    print(vraag2.get())
    print(vraag3.get())
    print(rec.get())
    data_connectie()
    loginfield.delete(0, END)   #textveld leeg maken
    vraag2.delete(0, END)
    vraag3.delete(0, END)
    rec.delete(0, END)
    hoofdframe.pack_forget()
    vragenframe.pack_forget()
    voorwaardenframe.pack_forget()

    loginframe.pack(padx=300, pady=300)



def doorgaanKnop():
        bericht = 'In het volgende scherm kunt u uw recensie invoeren.'
        showinfo(title='popup', message=bericht)
        vragenRecensie()

def terugknop():
    voorwaardenframe.pack_forget()
    loginframe.pack(padx=300, pady=300)



def toonVoorwaarden():  # Beeld2
    loginframe.pack_forget()
    voorwaardenframe.pack()

def toonHoofdFrame():  # Beeld3
    if len(rec.get()) > 140:
        popup = 'Maak het bericht korter.'
        showinfo(title='popup', message=popup)
        vragenRecensie()
    elif len(rec.get()) == 0:
        popup2 = 'Voer een recensie in.'
        showinfo(title='popup', message=popup2)
        vragenRecensie()
    else:
        loginname.pack_forget()  # Beeld 1 weghalen
        vragenframe.pack_forget()
        hoofdframe.pack(padx=300, pady=300)  # Beeld 3 laten zien


def login():
    if loginfield.get() == "":
        bericht = 'U gaat anoniem verder.'          # Bericht dat weergegeven moet worden als geen naam in gevuld moet worden
        showinfo(title='popup', message=bericht)    # Maak popup van bericht
        toonVoorwaarden()                           # Ga naar functie met vragen
        return 'Anoniem'

    else:
        toonVoorwaarden()
        return loginfield.get()


def vragenRecensie():
    voorwaardenframe.pack_forget()
    vragenframe.pack(padx=300, pady=300)
    return vraag2, vraag3, rec

root = Tk()  # Creëer het hoofdschermroot.
root.overrideredirect(True)
root.overrideredirect(False)
root.attributes('-fullscreen', True)
filename = PhotoImage(file="C:\\Users\\Ivo\\OneDrive\\Pictures\\NS foto\\ns1.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)



loginframe = Frame(master=root)                                         # plaatsen op hoofdscherm (root)
loginframe.pack(padx=300, pady=300)                                                       # Plaats en groote van het scherm bepalen
loginname = Label(master=loginframe, text='Naam:')                      # de tekst die getoond moet worden
loginname.pack(padx=50, pady=10 )
loginfield = Entry(master=loginframe)                                   # Tekst vak maken en plaats op scherm loginFrame (master=loginframe)
loginfield.pack(padx=50, pady=10)
loginbutton = Button(master=loginframe, text='Start', command=login)
loginbutton.pack(padx=50, pady=30)

voorwaardenframe = Frame(master=root)
voorwaardenframe.pack()
voorwaardenTXT = Label(master=voorwaardenframe,
                       text='Bij het accpteren van deze voorwaarden accepteerd u dat de info die u bij deze enquete geeft opgeslagen worden'
                            'in de database van de NS \n en mogelijk weergegeven wordt op het groote scherm in de hal.')
voorwaardenTXT.pack(padx=0, pady=240 )

acceptbutton = Button(master=voorwaardenframe, text='Accepteer', command=doorgaanKnop)
acceptbutton.place(x=300, y=300)
terugknop = Button(master=voorwaardenframe, text='Terug', command=terugknop)
terugknop.place(x=400, y=300)

vragenframe = Frame(master=root)
vragenframe.pack()

vraag2TXT = Label(master=vragenframe, text='Bent u student?:')
vraag2TXT.pack(pady=4)
vraag2 = Entry(master=vragenframe)
vraag2.pack(pady=4)

vraag3TXT = vraag2TXT = Label(master=vragenframe, text='Waar woont u?:')
vraag2TXT.pack(pady=4)
vraag3 = Entry(master=vragenframe)
vraag3.pack(pady=4)

recTXT = vraag2TXT = Label(master=vragenframe, text='Vul hier uw recentie in over uw ervraring over het reizen met NS:')
recTXT.pack(pady=4)
rec = Entry(master=vragenframe)
rec.pack(pady=4, ipady=40, padx=40, ipadx=40)

next = Button(master=vragenframe, text='Volgende', command=toonHoofdFrame)
next.pack(padx=20, pady=30)

hoofdframe = Frame(master=root)
hoofdframe.pack(fill="both", expand=True)
backbutton = Button(master=hoofdframe, text='submit', command=toonLoginFrame)
backbutton.pack(padx=20, pady=30)

toonLoginFrame()
root.mainloop()  # Toon het hoofdscherm