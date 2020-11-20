import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox
from matplotlib import pyplot as plt

# Classe permettant de saisir les paramètres de taille de l'univers


class UniversWin():
    def confirm(self):
        """ Méthode exécutée pour enregistrer les données et fermer la fenêtre. """
        # Sauvegarde données
        self.parameter.proportion = self.champ_p.get()
        self.parameter.ajuster_taille(
            int(self.champ_coord_X.get()), int(self.champ_coord_Y.get()))

        # Fermeture fenêtre
        self.root.destroy()

    def __init__(self, param):
        # Initialisation
        self.root = tk.Tk()
        self.root.geometry("400x200")
        self.root.wm_title("Univers")
        self.parameter = param

        # Ajustement agencement
        self.root.columnconfigure(0, minsize=250)
        self.root.rowconfigure(0, minsize=50)
        self.root.rowconfigure(1, minsize=50)
        self.root.rowconfigure(2, minsize=50)
        self.root.rowconfigure(3, minsize=50)

        # Proportion astrocyte
        label_p = tk.Label(
            self.root, text="Proportion astrocyte : ", anchor="w")
        label_p.grid(row=0, column=0)
        self.champ_p = tk.Scale(self.root, orient='horizontal',
                                from_=0, to=1, resolution=0.01, tickinterval=2)
        self.champ_p.grid(row=0, column=1)

        # Taille X
        label_coordX = tk.Label(self.root, text="Taille X : ", anchor="w")
        label_coordX.grid(row=1, column=0)
        self.champ_coord_X = tk.Spinbox(
            self.root, format='%10.0f', increment=1, from_=0, to=100, width=15)
        self.champ_coord_X.grid(row=1, column=1)

        # Taille Y
        label_coordY = tk.Label(self.root, text="Taille Y : ", anchor="w")
        label_coordY.grid(row=2, column=0)
        self.champ_coord_Y = tk.Spinbox(
            self.root, format='%10.0f', increment=1, from_=0, to=100, width=15)
        self.champ_coord_Y.grid(row=2, column=1)

        # Bouton confirmer
        button = tk.Button(self.root, text="Confirmer", command=self.confirm)
        button.grid(row=3, column=0, columnspan=2)

        # Lancement
        self.root.mainloop()
