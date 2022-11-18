import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
#LIBRERIAS PARA WEBSCRAPING
import requests
from bs4 import BeautifulSoup
import pandas as pd
#CREAMOS LA VENTANA
ventana = tk.Tk()
ventana.geometry("200x150")
ventana.title('WEBSCRAPING DE POKEMONES')

def webscraping():
    try:
        url = "https://pokemondb.net/pokedex/all"
        r = requests.get(url)
        soup = BeautifulSoup(r.content,'html.parser')
        rows = soup.find('table',attrs={'id':'pokedex'}).find('tbody').find_all('tr')
        rows[0].find_all('td')[1].get_text()
        rows[0].find_all('td')[2].get_text()
        names = []
        types = []
        total = []
        hp = []
        attack = []
        defense = []
        sp_atk = []
        sp_def = []
        speed = []
        for rows in rows:
            names.append(rows.find_all('td')[1].get_text())
            types.append(rows.find_all('td')[2].get_text())
            total.append(rows.find_all('td')[3].get_text())
            hp.append(rows.find_all('td')[4].get_text())
            attack.append(rows.find_all('td')[5].get_text())
            defense.append(rows.find_all('td')[6].get_text())
            sp_atk.append(rows.find_all('td')[7].get_text())
            sp_def.append(rows.find_all('td')[8].get_text())
            speed.append(rows.find_all('td')[9].get_text())
        len(names)

        df = pd.DataFrame({"Nombres":names,"Tipos":types,"Total":total,"HP":hp,"Ataque":attack,"Defensa":defense,"Sp Atk":sp_atk,"Sp Def":sp_def,"Velocidad":speed})
        df.to_csv('Pokemones.csv')
        messagebox.showinfo(message='Webscraping hechon con exito!',title='Exito!')
    except:
        messagebox.showerror(message='No se ha podido hacer la conexión a la pagina web!')

Boton = tk.Button(ventana,text='Webscraping',command=webscraping).place(x=40,y=50)
ventana.mainloop()