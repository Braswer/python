from os import read
from tkinter import *
from tkinter import ttk
from typing import Annotated, Counter
import sqlite3

#dati finti di prova
'''data =[ 
    ["Lenovo", "Thinkpad", "PC533424", "", "MN523", "Gabriele De Anna", "Romania", "SupportoIT", "Frocio"],
    ["Lenovo", "Thinkpad", "PC533424", "", "MN523", "Gabriele De Anna", "Romania", "SupportoIT", "Frocio"],
    ["Lenovo", "Thinkpad", "PC533424", "", "MN523", "Gabriele De Anna", "Romania", "SupportoIT", "Frocio"],
    ["Lenovo", "Thinkpad", "PC533424", "", "MN523", "Gabriele De Anna", "Romania", "SupportoIT", "Frocio"],
    ["Lenovo", "Thinkpad", "PC533424", "", "MN523", "Gabriele De Anna", "Romania", "SupportoIT", "Frocio"],
]'''


#creo database

conn = sqlite3.connect("asset_luiss.db")

#cursore (questo lo copio ancora, non ho ben capito cosa sia)
c = conn.cursor()
#creo la table del database
c.execute("""CREATE TABLE if not exists asset (
    marca text,
    modello text,
    seriale text,
    seriale_k text,
    seriale_m text,
    proprietario text,
    sede text,
    ufficio text,
    ruolo text)
    """)
#aggiungo i dati che ho scritto sotto al db
'''for dato in data:
    c.execute("INSERT INTO asset VALUES (:marca, :modello, :seriale, :seriale_k, :seriale_m, :proprietario, :sede, :ufficio, :ruolo)",
        {
        "marca": dato[0],
        "modello": dato[1],
        "seriale": dato[2],
        "seriale_k": dato[3],
        "seriale_m": dato[4],
        "proprietario": dato[5],
        "sede": dato[6],
        "ufficio": dato[7],
        "ruolo": dato[8]
        }
        )'''

#commissiono modifiche
conn.commit()

#chiudo il db
conn.close()


def ricerca():
    conn = sqlite3.connect("asset_luiss.db")
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM asset")
    dati = c.fetchall()

    #aggiungo i dati alla schermata
    global count
    count = 0

    for record in dati:
        if count % 2 == 0:
            frame1.insert(parent="", index="end", iid=count, text="", values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[0]), tags=("evenrow"))
        else:
            frame1.insert(parent="", index="end", iid=count, text="", values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[0]), tags=("oddrow"))
        count += 1

    conn.commit()
    conn.close()


#creo tabella
test = Tk()
test.title("Asset PC Luiss")
test.geometry("1500x500")
#aggiungere uno stile
style = ttk.Style()
#prendo un tema
style.theme_use("default")
#configuro i colori di Treview
style.configure("Treeview",
    background = "#D3D3D3",
    foreground = "black",
    rowheight=25,
    fieldbackground="#D3D3D3")
#cambio il colore dei records selezionati
style.map("Treeview",
    background = [("selected", "#347083")])

#creo il frame di Treeview
tree_frame = Frame(test)
tree_frame.pack(pady=10)

#creo la scroolbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

#creo il Treeview vero e proprio
frame1 = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set,selectmode="extended")
frame1.pack()



#configuro la scrollbar
tree_scroll.config(command=frame1.yview)

#definisco le colonne
frame1["columns"] = (
                     "Marca",
                     "Modello",
                     "Seriale",
                     "Seriale Kens",
                     "Seriale Monitor",
                     "Proprietario",
                     "Sede",
                     "Ufficio",
                     "Ruolo"
                    )

#formatto le colonne
frame1.column("#0", width=0, stretch=NO)
frame1.column("Marca", anchor=W, width=100)
frame1.column("Modello", anchor=W, width=100)
frame1.column("Seriale", anchor=W, width=100)
frame1.column("Seriale Kens", anchor=W, width=100)
frame1.column("Seriale Monitor", anchor=W, width=100)
frame1.column("Proprietario", anchor=W, width=100)
frame1.column("Sede", anchor=W, width=100)
frame1.column("Ufficio", anchor=W, width=100)
frame1.column("Ruolo", anchor=W, width=100)

#creo intestazioni
frame1.heading("#0", text="", anchor=CENTER)
frame1.heading("Marca", text="Marca", anchor=CENTER)
frame1.heading("Modello", text="Modello", anchor=CENTER)
frame1.heading("Seriale", text="Seriale", anchor=CENTER)
frame1.heading("Seriale Kens", text="Seriale Kens", anchor=CENTER)
frame1.heading("Seriale Monitor", text="Seriale Monitor", anchor=CENTER)
frame1.heading("Proprietario", text="Proprietario", anchor=CENTER)
frame1.heading("Sede", text="Sede", anchor=CENTER)
frame1.heading("Ufficio", text="Ufficio", anchor=CENTER)
frame1.heading("Ruolo", text="Ruolo", anchor=CENTER)

#creo i tag delle righe
frame1.tag_configure("oddrow", background="white")
frame1.tag_configure("evenrow", background="lightblue")


#aggiungo il campo di inserimento dati
data_frame = LabelFrame(test, text="Dati")
data_frame.pack(fill="x", expand="yes", padx=20)

marca_label = Label(data_frame, text="Marca")
marca_label.grid(row=0, column=0, padx=10, pady=10)
marca_entry = Entry(data_frame)
marca_entry.grid(row=0, column=1, padx=10, pady=10)

modello_label = Label(data_frame, text="Modello")
modello_label.grid(row=0, column=2, padx=10, pady=10)
modello_entry = Entry(data_frame)
modello_entry.grid(row=0, column=3, padx=10, pady=10)

seriale_label = Label(data_frame, text="Seriale")
seriale_label.grid(row=0, column=4, padx=10, pady=10)
seriale_entry = Entry(data_frame)
seriale_entry.grid(row=0, column=5, padx=10, pady=10)

serialek_label = Label(data_frame, text="Seriale Kens")
serialek_label.grid(row=0, column=6, padx=10, pady=10)
serialek_entry = Entry(data_frame)
serialek_entry.grid(row=0, column=7, padx=10, pady=10)

serialem_label = Label(data_frame, text="Seriale Monitor")
serialem_label.grid(row=0, column=8, padx=10, pady=10)
serialem_entry = Entry(data_frame)
serialem_entry.grid(row=0, column=9, padx=10, pady=10)

proprietario_label = Label(data_frame, text="Proprietario")
proprietario_label.grid(row=1, column=0, padx=10, pady=10)
proprietario_entry = Entry(data_frame)
proprietario_entry.grid(row=1, column=1, padx=10, pady=10)

sede_label = Label(data_frame, text="Sede")
sede_label.grid(row=1, column=2, padx=10, pady=10)
sede_entry = Entry(data_frame)
sede_entry.grid(row=1, column=3, padx=10, pady=10)

ufficio_label = Label(data_frame, text="Ufficio")
ufficio_label.grid(row=1, column=4, padx=10, pady=10)
ufficio_entry = Entry(data_frame)
ufficio_entry.grid(row=1, column=5, padx=10, pady=10)

ruolo_label = Label(data_frame, text="Ruolo")
ruolo_label.grid(row=1, column=6, padx=10, pady=10)
ruolo_entry = Entry(data_frame)
ruolo_entry.grid(row=1, column=7, padx=10, pady=10)

id_label = Label(data_frame, text="ID")
id_label.grid_forget#(row=1, column=8, padx=10, pady=10)
id_entry = Entry(data_frame)
id_entry.grid_forget#(row=1, column=9, padx=10, pady=10)

#funzione Seleziona
def seleziona_anag(e):
    #pulisco il campo
    marca_entry.delete(0, END)
    modello_entry.delete(0, END)
    seriale_entry.delete(0, END)
    serialek_entry.delete(0, END)
    serialem_entry.delete(0, END)
    proprietario_entry.delete(0, END)
    sede_entry.delete(0, END)
    ufficio_entry.delete(0, END)
    ruolo_entry.delete(0, END)
    id_entry.delete(0, END)
#prendo il numero di dato
    selezionati = frame1.focus()
#prendo il valore del dato
    valori = frame1.item(selezionati, "values")

#output per il campo da compilare
    marca_entry.insert(0, valori[0])
    modello_entry.insert(0, valori[1])
    seriale_entry.insert(0, valori[2])
    serialek_entry.insert(0, valori[3])
    serialem_entry.insert(0, valori[4])
    proprietario_entry.insert(0, valori[5])
    sede_entry.insert(0, valori[6])
    ufficio_entry.insert(0, valori[7])
    ruolo_entry.insert(0, valori[8])
    id_entry.insert(0, valori[9])

#funzione svuota
def svuota():
    marca_entry.delete(0, END)
    modello_entry.delete(0, END)
    seriale_entry.delete(0, END)
    serialek_entry.delete(0, END)
    serialem_entry.delete(0, END)
    proprietario_entry.delete(0, END)
    sede_entry.delete(0, END)
    ufficio_entry.delete(0, END)
    ruolo_entry.delete(0, END)
    id_entry.delete(0, END)

#funzione sali
def sali():
    rows = frame1.selection()
    for row in rows:
        frame1.move(row, frame1.parent(row), frame1.index(row)-1)


#funzione scendi
def scendi():
    rows = frame1.selection()
    for row in rows:
        frame1.move(row, frame1.parent(row), frame1.index(row)+1)

#funzione rimuovi un elemento
def rimuovi_1():
    x = frame1.selection()[0]

    conn = sqlite3.connect("asset_luiss.db")
    c = conn.cursor()
    c.execute("DELETE FROM asset WHERE oid = :oid",
            {
                "oid": id_entry.get(),
            })

    conn.commit()
    conn.close()

    frame1.delete(x)
    
    marca_entry.delete(0, END)
    modello_entry.delete(0, END)
    seriale_entry.delete(0, END)
    serialek_entry.delete(0, END)
    serialem_entry.delete(0, END)
    proprietario_entry.delete(0, END)
    sede_entry.delete(0, END)
    ufficio_entry.delete(0, END)
    ruolo_entry.delete(0, END)
    id_entry.delete(0, END)

   

#funzione rimuovi più elementi
def rimuovi_molti():
    y = frame1.selection()

    for dato in y:
        frame1.delete(dato)

#funzione rimuovi tutti
def rimuovi_tutti():
    for dato in frame1.get_children():
        frame1.delete(dato)

#funzione aggiorna anagrafica
def aggiorna():
    selezionato = frame1.focus()
    frame1.item(selezionato, text="", values=(marca_entry.get(), modello_entry.get(), seriale_entry.get(), serialek_entry.get(), serialem_entry.get(), proprietario_entry.get(), sede_entry.get(), ufficio_entry.get(), ruolo_entry.get()))


    conn = sqlite3.connect("asset_luiss.db")
    c = conn.cursor()
    c.execute("""UPDATE asset SET
        marca = :marca,
        modello = :modello,
        seriale = :seriale,
        seriale_k = :seriale_k,
        seriale_m = :seriale_m,
        proprietario = :proprietario,
        sede = :sede,
        ufficio = :ufficio,
        ruolo = :ruolo

        WHERE oid = :oid""",


        {
            "marca": marca_entry.get(),
            "modello": modello_entry.get(),
            "seriale": seriale_entry.get(),
            "seriale_k": serialek_entry.get(),
            "seriale_m": serialem_entry.get(),
            "proprietario": proprietario_entry.get(),
            "sede": sede_entry.get(),
            "ufficio": ufficio_entry.get(),
            "ruolo": ruolo_entry.get(),
            "oid": id_entry.get(),
        })


    conn.commit()
    conn.close()


    marca_entry.delete(0, END)
    modello_entry.delete(0, END)
    seriale_entry.delete(0, END)
    serialek_entry.delete(0, END)
    serialem_entry.delete(0, END)
    proprietario_entry.delete(0, END)
    sede_entry.delete(0, END)
    ufficio_entry.delete(0, END)
    ruolo_entry.delete(0, END)
    id_entry.delete(0, END)

#funzione aggiungi  
def aggiungi():

    conn = sqlite3.connect("asset_luiss.db")
    c = conn.cursor()
    c.execute("INSERT INTO asset VALUES (:marca, :modello, :seriale, :seriale_k, :seriale_m, :proprietario, :sede, :ufficio, :ruolo)",
        {
        "marca": marca_entry.get(),
        "modello": modello_entry.get(),
        "seriale": seriale_entry.get(),
        "seriale_k": serialek_entry.get(),
        "seriale_m": serialem_entry.get(),
        "proprietario": proprietario_entry.get(),
        "sede": sede_entry.get(),
        "ufficio": ufficio_entry.get(),
        "ruolo": ruolo_entry.get()
        }
        )

    
    conn.commit()
    conn.close()


    marca_entry.delete(0, END)
    modello_entry.delete(0, END)
    seriale_entry.delete(0, END)
    serialek_entry.delete(0, END)
    serialem_entry.delete(0, END)
    proprietario_entry.delete(0, END)
    sede_entry.delete(0, END)
    ufficio_entry.delete(0, END)
    ruolo_entry.delete(0, END)
    id_entry.delete(0, END)


#creo il frame dei pulsanti
opzioni_frame = LabelFrame(test, text="Opzioni")
opzioni_frame.pack(fill="x", expand="yes", padx=20)

#creo i tasti
aggiungi_tasto = Button(opzioni_frame, text="Aggiungi",command=aggiungi)
aggiungi_tasto.grid(row=0, column=0, padx=10, pady=10)

aggiorna_tasto = Button(opzioni_frame, text="Aggiorna",command=aggiorna)
aggiorna_tasto.grid(row=0, column=1, padx=10, pady=10)

svuota_tasto = Button(opzioni_frame, text="Svuota campi", command=svuota)
svuota_tasto.grid(row=0, column=2, padx=10, pady=10)

rimuovi_selezione_tasto = Button(opzioni_frame, text="Rimuovi", command=rimuovi_1)
rimuovi_selezione_tasto.grid(row=0, column=3, padx=10, pady=10)

#rimuovi_molti_tasto = Button(opzioni_frame, text="Rimuovi selezionati", command=rimuovi_molti)
#rimuovi_molti_tasto.grid(row=0, column=4, padx=10, pady=10)

#su_tasto = Button(opzioni_frame, text="Muovi su", command=ricerca)
#su_tasto.grid(row=0, column=5, padx=10, pady=10)

#giu_tasto = Button(opzioni_frame, text="Muovi giù", command=scendi)
#giu_tasto.grid(row=0, column=6, padx=10, pady=10)

#seleziona_tasto = Button(opzioni_frame, text="Seleziona", command=seleziona_anag)
#seleziona_tasto.grid(row=0, column=7, padx=10, pady=10)

#lego Treeview nella selezione dei dati
frame1.bind("<ButtonRelease -1>", seleziona_anag)

ricerca()

test.mainloop()