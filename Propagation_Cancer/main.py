from data_main import *
from vue_univers import *
from vue_animation import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk


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

"""
fig = plt.figure()

animation(env, 100, show=True, fig=fig, interv=300)"""

fig = plt.Figure()
root = tk.Tk()

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(column=0, row=0)

animation(env, 100, show=False, fig=fig, interv=300)

tk.mainloop()
