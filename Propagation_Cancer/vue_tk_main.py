import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from data_main import *
from vue_univers import *
from vue_animation import animation
from tkinter import messagebox
from vue_tk_savewin import *
from vue_tk_param import *
import tkinter.ttk as ttk


class App():

    def create_menu(self):
        mainmenu = tk.Menu(self.root)
        self.root.config(menu=mainmenu)

        menufichier = tk.Menu(mainmenu, tearoff=0)
        menufichier.add_command(label="Quitter", command=self.quit)
        menufichier.add_command(label="Sauvegarder",
                                command=self.save_simulation)

        menusimulation = tk.Menu(mainmenu, tearoff=0)
        menusimulation.add_command(label="Générer", command=self.generate)
        menusimulation.add_command(
            label="Démo animation", command=self.tk_animation)

        mainmenu.add_cascade(label="Fichier", menu=menufichier)
        mainmenu.add_cascade(label="Simulation", menu=menusimulation)
        mainmenu.add_cascade(
            label="Aide", command=self.quit)

    def __init__(self):
        self.root = tk.Tk()
        #button = tk.Button(self.root, text='root quit', command=self.quit)
        self.root.wm_title("Propagation cancer")
        #button.grid(row=0, column=1)

        fig = plt.figure(figsize=(6, 6))
        self.graph_display(fig)

        self.s = ttk.Style()
        self.s.theme_use('clam')

        self.parametres = ParamWidget()
        self.parametres.root.grid(row=0, column=1, sticky="nw")

        self.hold_animation = None

        self.create_menu()
        self.root.protocol("WM_DELETE_WINDOW", quit)

        self.root.mainloop()

    def quit(self):
        if messagebox.askokcancel("Quitter", "Voulez-vous quitter ?"):
            self.root.destroy()
            exit()

    def graph_display(self, fig):
        self.graph = FigureCanvasTkAgg(fig, self.root)
        self.canvas = self.graph.get_tk_widget()
        self.canvas.grid(row=0, column=0)

    def tk_animation(self):
        self.canvas.grid_forget()

        univers = create_univers(20, 20)
        env = [univers, []]
        set_cell(0, 4, 1, env)
        set_cell(2, 2, 1, env)
        set_cell(2, 3, 1, env)

        fig = plt.figure()
        self.graph_display(fig)
        self.hold_animation = animation(
            env, 100, show=False, fig=fig, interv=300)

    def save_simulation(self):
        # S'il n'y a aucune animation
        if self.hold_animation == None:
            messagebox.showerror(title="Erreur sauvegarde",
                                 message="Pas d'animation à sauvegarder !")
            return

        # Sinon sauvegarde
        savewindows = SaveWin(self.hold_animation)

    def generate(self):
        self.canvas.grid_forget()
        self.hold_animation = None

        univers = create_univers(5, 5)
        env = [univers, []]
        set_cell(0, 4, 1, env)
        set_cell(2, 2, 1, env)
        set_cell(2, 3, 1, env)

        index = get_groupe(0, 4, env)
        adj = env[1][index][1]
        for e in adj:
            univers[e[0], e[1]] = 2
        index = get_groupe(2, 3, env)
        adj = env[1][index][1]
        for e in adj:
            univers[e[0], e[1]] = 2

        fig = plt.figure(figsize=(6, 6))
        ax = plt.subplot(1, 1, 1)
        plt.axis([-1, 10, -1, 10])
        display_full(univers, ax, False)

        self.graph_display(fig)


if __name__ == "__main__":
    app = App()
