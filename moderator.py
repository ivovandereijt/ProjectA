from tkinter import *                       #Tkinder import
from tkinter.messagebox import showinfo     #Import popups
import psycopg2
from tkinter import ttk

#text box maken met welke je wilt verwijderen 
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

def overzichtview():
    cur.execute("Select idnummer, recentie from reiziger")
    f= open('data.txt', 'w')
    myresult = cur.fetchall()
    for x in myresult:
        print(x)
        line = ' '.join(str(a) for a in x)
        f.write(line  + '\n')

    return f
overzichtview()
f= ""
def dataoverview(f):
    f = open('data.txt', 'r')
    f= f.read()
    return f
f = dataoverview(f)

def toonLoginFrame():                       #Beeld1
    hoofdframe.pack_forget()
    loginname.pack()

def dataverwijderen():
    #f= ""
    data = int(verwijderen.get())
    if str(data) == '':
        print("Geen data ingevoerd om te verwijderen")
    else:
        cur.execute("delete from reiziger where idnummer= '%s'" % (data))
        con.commit()
    overzichtview()
    print(data)
    #allesview.pack_forget()
    #f = open('data.txt', 'r')
    #f = f.read()
    #f = dataoverview(f)
    #allesview.pack(padx=50, pady=10,)
    #newallesview = Label(master=overviewframe, text=f)
    #newallesview.pack(padx=50, pady=10, )
    #newallesview.pack()

def terugbut():

    newoverviewframe.pack_forget()
    overviewframe.pack(padx=300, pady=300)

def refresh():
    #overviewframe.pack_forget()
    #newoverviewframe.pack()
    f= ''
    f = dataoverview(f)
    showinfo(title='popup', message=f)
    #newallesview = Label(master=newoverviewframe, text=f)
    #newallesview.pack()


def login():
    gebruiker = loginfield.get()
    ww = wwfield.get()
    if gebruiker == 'Admin' and ww == "Wachtwoord":
        bericht = "Welkom"
        showinfo(title='popup', message=bericht)
        loginframe.pack_forget()
        overviewframe.pack

    else:
        bericht = "Wachtwoord / gebruikersnaam is niet juis"
        showinfo(title='popup', message=bericht)

def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=200,height=200)

root = Tk()   # Creëer het hoofdschermroot.
root.title('Moderator scherm')
root.overrideredirect(True)
root.overrideredirect(False)
root.attributes('-fullscreen',True)
filename = PhotoImage(file="C:\\Users\\Ivo\\OneDrive\\Pictures\\NS foto\\ns1.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


loginframe = Frame(master=root)                                             #plaatsen op hoofdscherm (root)
loginframe.pack(padx=300, pady=300)                                   #Plaats en groote van het scherm bepalen

loginname = Label(master=loginframe, text='Naam:')                          #de tekst die getoond moet worden
loginname.pack (padx=50, pady=10,)
loginfield = Entry(master=loginframe)                                       #Tekst vak maken en plaats op scherm loginFrame (master=loginframe)
loginfield.pack (padx=50, pady=10)

loginww = Label(master=loginframe, text='Wachtwoord:')
loginww.pack (padx=50, pady=10,)
wwfield = Entry(master=loginframe, show= "*")
wwfield.pack (padx=50, pady=10)

loginbutton = Button(master=loginframe, text='Start', command=login)
loginbutton.pack(padx=50, pady=30)

overviewframe = Frame(master=root)
overviewframe.pack(padx=300, pady=300)
allesview = Label(master=overviewframe, text=f)
allesview.pack (padx=50, pady=10,)
#newallesview = Label(master=overviewframe, text="")
#newallesview.pack(padx=50, pady=10, )

hoofdframe = Frame(master=root)
hoofdframe.pack(fill="both", expand=True)


verwijderenTXT = Label(master=overviewframe, text='Welke recentie wilt u verwijderen?:')
verwijderenTXT.pack(pady=4)
verwijderen = Entry(master=overviewframe)
verwijderen.pack(pady=4)
verwijderenKNP = Button(master=overviewframe, text='Verwijderen', command=dataverwijderen)
verwijderenKNP.pack(pady=4)

newoverviewKNP = Button(master=overviewframe, text='Overview', command=refresh)
newoverviewKNP.pack(pady=4)

newoverviewframe = Frame(master=root)
newoverviewframe.pack(padx=300, pady=300)
terugKNP = Button(master=newoverviewframe, text='Terug', command=terugbut)
terugKNP.pack(pady=4)


canvas=Canvas(newoverviewframe)
frame=Frame(canvas)
myscrollbar=Scrollbar(newoverviewframe,orient="vertical", command=canvas.yview)
myscrollbar.pack(side="right",fill="y")
canvas.configure(yscrollcommand=myscrollbar.set)
canvas.bind("<Configure>",lambda e: canvas.config(scrollregion= canvas.bbox(ALL)))
#scrollbar = ttk.Scrollbar(container = newoverviewframe, orient='vertical', command=newoverviewframe.yview)

#newoverviewframe['yscrollcommand']= scrollbar.set

toonLoginFrame()
root.mainloop()