import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox
from matplotlib import pyplot as plt

from vue_animation import *
from vue_tk_univers import *
import tkinter.ttk as ttk

# Widget de gestion des paramètres


class ParamWidget():

    def set_univers(self):
        self.uni = UniversWin(self)

    def __init__(self, data):
        # Initialisation
        self.root = tk.Frame()

        # Style
        self.s = ttk.Style()
        self.s.theme_use('clam')

        # Taille
        self.taille_x = data.taille_y
        self.taille_y = data.taille_x
        self.proportion = data.proportion

        # Champ n
        label_n = tk.Label(self.root, text="Itérations : ", anchor="w")
        label_n.grid(row=0, column=0)
        self.champ_iter = tk.Spinbox(
            self.root, format='%10.0f', increment=1, from_=0, to=200, width=32)
        self.champ_iter.grid(row=0, column=1, columnspan=2)
        self.champ_iter.delete(0, "end")
        self.champ_iter.insert(0, 20)

        # Homotype/hétérotype/jonction
        label_f = tk.Label(self.root, text="Modèle : ", anchor="w")
        label_f.grid(row=1, column=0)
        self.champ_modele = tk.Spinbox(self.root, values=(
            'Homotype', 'Hétérotype', 'Jonction'), width=32)
        self.champ_modele.grid(row=1, column=1, columnspan=2)

        # P
        label_p = tk.Label(self.root, text="P : ", anchor="w")
        label_p.grid(row=2, column=0)
        self.champ_p = tk.Scale(self.root, orient='horizontal',
                                from_=0, to=1, resolution=0.01, tickinterval=2, length=210)
        self.champ_p.grid(row=2, column=1, columnspan=2)

        # Q
        label_q = tk.Label(self.root, text="Q : ", anchor="w")
        label_q.grid(row=3, column=0)
        self.champ_q = tk.Scale(self.root, orient='horizontal',
                                from_=0, to=1, resolution=0.01, tickinterval=2, length=210)
        self.champ_q.grid(row=3, column=1, columnspan=2)

        # Interv
        label_interv = tk.Label(self.root, text="Interv : ", anchor="w")
        label_interv.grid(row=4, column=0)
        self.champ_interv = tk.Spinbox(
            self.root, format='%10.0f', increment=50, from_=100, to=2000, width=32)
        self.champ_interv.grid(row=4, column=1, columnspan=2)

        # Coordonées centre
        label_coord = tk.Label(self.root, text="Centre (coord) : ", anchor="w")
        label_coord.grid(row=5, column=0)
        self.champ_coord_X = tk.Spinbox(
            self.root, format='%10.0f', increment=1, from_=0, to=self.taille_x, width=15)
        self.champ_coord_X.grid(row=5, column=1)
        self.champ_coord_Y = tk.Spinbox(
            self.root, format='%10.0f', increment=1, from_=0, to=self.taille_y, width=15)
        self.champ_coord_Y.grid(row=5, column=2)

        # Taille centre
        label_size = tk.Label(self.root, text="Taille centre : ", anchor="w")
        label_size.grid(row=6, column=0)
        self.champ_size_X = tk.Spinbox(
            self.root, format='%10.0f', increment=1, from_=0, to=10, width=15)
        self.champ_size_X.grid(row=6, column=1)
        self.champ_size_X.delete(0, "end")
        self.champ_size_X.insert(0, "1")

        self.champ_size_Y = tk.Spinbox(
            self.root, format='%10.0f', increment=1, from_=0, to=10, width=15)
        self.champ_size_Y.grid(row=6, column=2)
        self.champ_size_Y.delete(0, "end")
        self.champ_size_Y.insert(0, "1")

        # Univers
        self.button_univers = tk.Button(
            self.root, text="Univers", command=self.set_univers, width=38)
        self.button_univers.grid(row=7, column=0, columnspan=3)

        # Sample
        label_sample = tk.Label(self.root, text="Taille stat : ", anchor="w")
        label_sample.grid(row=8, column=0)
        self.champ_sample = tk.Spinbox(
            self.root, format='%10.0f', increment=1, from_=1, to=1000, width=32)
        self.champ_sample.grid(row=8, column=1, columnspan=2)
        self.champ_sample.delete(0, "end")
        self.champ_sample.insert(0, "50")

    def ajuster_taille(self, x, y):
        """ Méthode permettant d'actualiser les valeurs de taille de l'univers. """
        self.taille_x = x
        self.taille_y = y

        self.champ_coord_X.config(to=self.taille_x)
        self.champ_coord_Y.config(to=self.taille_y)
