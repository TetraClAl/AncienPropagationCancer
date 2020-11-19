import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox
from matplotlib import pyplot as plt


class SaveWin:
    def __init__(self, animation_data):
        # Initialisation
        self.data = animation_data
        self.root = tk.Tk()

        # Dimensions & Titre
        self.root.geometry("500x200")
        self.root.wm_title("Sauvegarde")
        self.root.columnconfigure(0, minsize=500)
        self.root.rowconfigure(0, minsize=80)
        self.root.rowconfigure(1, minsize=80)
        self.root.rowconfigure(2, minsize=20)

        # Champ de saisie
        self.filename = tk.Entry(self.root, width=10)

        # Label
        label = tk.Label(self.root, text="Nom du fichier & chemin :")

        # Bouton
        bouton = tk.Button(self.root, text='Enregistrer',
                           command=self.save_action)

        # Placement des widgets
        label.grid(row=0, column=0)
        self.filename.grid(row=1, column=0)
        bouton.grid(row=2, column=0)

        # Lancement
        self.root.mainloop()

    def save_action(self):
        # Sauvegarde
        self.data.save(self.filename.get())
        self.root.destroy()
