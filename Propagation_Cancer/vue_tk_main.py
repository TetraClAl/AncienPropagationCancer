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
from controleur_couplage import jonction_duo
from vue_stats import *

matplotlib.use('tkagg')

# Classe principale de l'application

matplotlib.use('tkagg')


class App():

    def create_menu(self):
        """ Fonction gérant la création du menu. """
        mainmenu = tk.Menu(self.root)
        self.root.config(menu=mainmenu)

        # Menu Fichier
        menufichier = tk.Menu(mainmenu, tearoff=0)
        menufichier.add_command(label="Quitter", command=self.quit)
        menufichier.add_command(label="Sauvegarder",
                                command=self.save_simulation)

        # Menu Simulation
        menusimulation = tk.Menu(mainmenu, tearoff=0)
        menusimulation.add_command(label="Générer", command=self.update_env)
        menusimulation.add_command(
            label="Simuler", command=self.tk_animation)

        # Sous-menu Stats
        menustats = tk.Menu(menusimulation, tearoff=0)
        menustats.add_command(label="Distance", command=self.stat_distance)
        menustats.add_command(label="Occupation", command=self.stat_occupation)
        menusimulation.add_cascade(label="Stats", menu=menustats)

        # Construction finale du menu
        mainmenu.add_cascade(label="Fichier", menu=menufichier)
        mainmenu.add_cascade(label="Simulation", menu=menusimulation)
        mainmenu.add_cascade(label="Aide", command=self.aide)

    def __init__(self):
        self.root = tk.Tk()
        #button = tk.Button(self.root, text='root quit', command=self.quit)
        self.root.wm_title("Propagation cancer")
        #button.grid(row=0, column=1)

        # Permet de créer un espace pour l'affichage
        fig = plt.figure(figsize=(6, 6))
        self.graph_display(fig)

        # Gestion style
        self.s = ttk.Style()
        self.s.theme_use('clam')

        # Initialisation des attributs
        self.env = None
        self.hold_animation = None

        self.taille_x = 20
        self.taille_y = 20
        self.sample = 50
        self.proportion = 0.5

        # Création et ajout du widget de gestion des paramètres
        self.parametres = ParamWidget(self)
        self.parametres.root.grid(row=0, column=1, sticky="nw")

        # Création du menu
        self.create_menu()
        self.root.protocol("WM_DELETE_WINDOW", quit)

        # Lancement de la boucle principale
        self.root.mainloop()

    def quit(self):
        """ Fonction s'exécutant à la fermeture de l'application. """
        if messagebox.askokcancel("Quitter", "Voulez-vous quitter ?"):
            self.root.destroy()
            exit()

    def graph_display(self, fig):
        """ Méthode d'affichage d'un graphe matplotlib. """
        self.graph = FigureCanvasTkAgg(fig, self.root)
        self.canvas = self.graph.get_tk_widget()
        self.canvas.grid(row=0, column=0)

    def update_param(self):
        """ Fonction de mise à jour des paramètres de la simulation. """

        self.centre = (int(self.parametres.champ_coord_X.get()), int(self.parametres.champ_coord_Y.get(
        )), int(self.parametres.champ_size_X.get()), int(self.parametres.champ_size_Y.get()))

        self.proportion = self.parametres.proportion

        self.sample = int(self.parametres.champ_sample.get())

        self.p = float(self.parametres.champ_p.get())
        self.q = float(self.parametres.champ_q.get())
        rule_str = self.parametres.champ_modele.get()
        if rule_str == 'Homotype':
            self.q = None
        if rule_str == 'Hétérotype':
            self.p = None

        self.n = int(self.parametres.champ_iter.get())

        self.interal = int(self.parametres.champ_interv.get())

        self.taille_x = int(self.parametres.taille_x)
        self.taille_y = int(self.parametres.taille_y)

    def update_env(self):
        """ Fonction permettant de créer l'environnement/univers. """

        self.update_param()

        self.env = init_univers(self.taille_x, self.taille_y, self.centre,
                                Pocc=self.proportion, init_tumor=None, cx=None, cy=None)

        self.canvas.grid_forget()
        fig = plt.figure()
        self.graph_display(fig)

        self.hold_animation = animation(
            self.env, self.centre, 1, jonction_duo, None, None, show=False, fig=fig, interv=1)

    def tk_animation(self):
        """ Fonction d'affichage d'une animation. """

        self.update_param()

        if self.env == None:
            self.update_env()
        else:
            del self.hold_animation

        self.canvas.grid_forget()
        fig = plt.figure()
        self.graph_display(fig)

        self.hold_animation = animation(
            self.env, self.centre, self.n, jonction_duo, self.p, self.q, show=False, fig=fig, interv=self.interal)

    def save_simulation(self):
        """ Méthode de sauvegarde de simulation. """
        # S'il n'y a aucune animation
        if self.hold_animation == None:
            messagebox.showerror(title="Erreur sauvegarde",
                                 message="Pas d'animation à sauvegarder !")
            return

        # Sinon sauvegarde
        savewindows = SaveWin(self.hold_animation)

    def generate(self):
        """ Fonction test/exemple, non fonctionnelle. """
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

    def stat_distance(self):
        """ Méthode callback pour les stats de distance. """

        self.update_param()

        fig = plt.figure(2)
        plt.clf()

        display_moyenne_distance(self.env, self.sample, self.n,
                                 self.centre, jonction_duo, self.p, self.q)

        window = tk.Toplevel()
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.get_tk_widget(). pack()

    def stat_occupation(self):
        """ Méthode callback pour les stats d'occupation. """

        self.update_param()

        fig = plt.figure(2)
        plt.clf()

        display_moyenne_occ(self.env, self.sample, self.n, self.centre,
                            jonction_duo, self.p, self.q)

        window = tk.Toplevel()
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.get_tk_widget(). pack()

    def aide(self):
        tk.messagebox.showinfo(
            title="Aide", message="Lire READ.me pour un apperçu du projet\nLire USE.md pour les consignes d'utilisation\nSe référer à ./Livrables pour des renseignements supplémentaires")


if __name__ == "__main__":
    app = App()
