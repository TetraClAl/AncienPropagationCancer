import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from data_main import *
from vue_univers import *

"""app = tk.Tk()"""

"""fig = Figure(figsize=(6, 4), dpi=96)
ax = fig.add_subplot(111)
ax.plot(range(10), [5, 4, 2, 6, 9, 8, 7, 1, 2, 3])"""


class App():

    def create_menu(self):
        mainmenu = tk.Menu(self.root)
        self.root.config(menu=mainmenu)

        menufichier = tk.Menu(mainmenu, tearoff=0)
        menufichier.add_command(label="Quitter", command=self.quit)
        menufichier.add_command(label="Sauvegarder", command=self.quit)

        menusimulation = tk.Menu(mainmenu, tearoff=0)
        menusimulation.add_command(label="Générer", command=self.generate)

        mainmenu.add_cascade(label="Fichier", menu=menufichier)
        mainmenu.add_cascade(label="Simulation", menu=menusimulation)
        mainmenu.add_cascade(
            label="Aide", command=self.quit)

    def __init__(self):
        self.root = tk.Tk()
        button = tk.Button(self.root, text='root quit', command=self.quit)
        self.root.wm_title("Propagation cancer")
        button.grid(row=0, column=1)

        univers = create_univers(5, 5)

        env = [univers, []]

        x1 = 0
        y1 = 4
        x2 = 2
        y2 = 2
        x3 = 2
        y3 = 3

        set_cell(x1, y1, 1, env)
        set_cell(x2, y2, 1, env)
        set_cell(x3, y3, 1, env)

        set_cell(x2, y2, 0, env)

        index = get_groupe(x1, y1, env)
        adj = env[1][index][1]
        for e in adj:
            univers[e[0], e[1]] = 2

        index = get_groupe(x3, y3, env)
        adj = env[1][index][1]
        for e in adj:
            univers[e[0], e[1]] = 2

        fig = plt.figure(figsize=(6, 6))
        ax = plt.subplot(1, 1, 1)
        plt.axis([-1, 10, -1, 10])
        display_full(univers, ax, False)

        self.graph = FigureCanvasTkAgg(fig, master=self.root)
        self.canvas = self.graph.get_tk_widget()
        self.canvas.grid(row=0, column=0)

        self.create_menu()

        self.root.mainloop()

    def quit(self):
        self.root.destroy()
        exit()

    def generate(self):

        univers = create_univers(5, 5)
        env = [univers, []]

        x1 = 0
        y1 = 4
        x2 = 2
        y2 = 2
        x3 = 2
        y3 = 3

        set_cell(x1, y1, 1, env)
        set_cell(x2, y2, 1, env)
        set_cell(x3, y3, 1, env)

        index = get_groupe(x1, y1, env)
        adj = env[1][index][1]
        for e in adj:
            univers[e[0], e[1]] = 2

        index = get_groupe(x3, y3, env)
        adj = env[1][index][1]
        for e in adj:
            univers[e[0], e[1]] = 2

        fig = plt.figure(figsize=(6, 6))
        ax = plt.subplot(1, 1, 1)
        plt.axis([-1, 10, -1, 10])
        display_full(univers, ax, False)

        self.graph = FigureCanvasTkAgg(fig, master=self.root)
        self.canvas = self.graph.get_tk_widget()
        self.canvas.grid(row=0, column=0)


app = App()
