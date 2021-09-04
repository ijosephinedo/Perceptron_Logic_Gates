from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

RED = "#fa8174"
YELLOW = "#feffb3"
GREEN = "#b3de69"

# Main frame and principals frames for data and graphs
root = Tk()
root.title("Práctica 1 - Compuertas AND y OR")
root.geometry('600x400')
root.resizable(False, False)
f_inputData = Frame(root)
f_graphs = Frame(root)
f_inputData.pack(side=RIGHT)
f_graphs.pack(side=LEFT, fill=BOTH, expand=1)
lf_log_gates = LabelFrame(f_inputData, text="Logic Gates", padx=5, pady=5)
lf_weights = LabelFrame(f_inputData, text="Weights", padx=5, pady=5)

# Iniitial variables
w1 = StringVar(lf_weights, "")
w2 = StringVar(lf_weights, "")
bias = StringVar(lf_weights, "")
done = False


def perceptron_and():
    start_over()
    ax_p.plot(1, 1, color=RED, marker='o')
    ax_p.plot(0, 1, color=GREEN, marker='o')
    ax_p.plot(1, 0, color=GREEN, marker='o')
    ax_p.plot(0, 0, color=GREEN, marker='o')
    fig_p.canvas.draw()
    w1.set("1")
    w2.set("1")
    bias.set("1.5")
    ax_p.set_title("LOGIC GATE AND")
    graph()


def perceptron_or():
    start_over()
    ax_p.plot(1, 1, color=RED, marker='o')
    ax_p.plot(0, 1, color=RED, marker='o')
    ax_p.plot(1, 0, color=RED, marker='o')
    ax_p.plot(0, 0, color=GREEN, marker='o')
    fig_p.canvas.draw()
    w1.set("1")
    w2.set("1")
    bias.set("0.5")
    ax_p.set_title("LOGIC GATE OR")
    graph()


def graph():
    global done
    if valid_weigths() and not done:
        x = np.arange(-2, 2, 0.01)
        y = (-float(w1.get()) * x + float(bias.get())) / float(w2.get())
        ax_p.plot(x, y, color=YELLOW)
        fig_p.canvas.draw()
        done = True


def start_over():
    global done
    ax_p.clear()
    start_graph()
    fig_p.canvas.draw()
    w1.set("")
    w2.set("")
    bias.set("")
    done = False


def start_graph():
    major_ticks = np.arange(-2, 3, 1)
    minor_ticks = np.arange(-2, 3, 0.2)
    ax_p.set_xticks(major_ticks)
    ax_p.set_xticks(minor_ticks, minor=True)
    ax_p.set_yticks(major_ticks)
    ax_p.set_yticks(minor_ticks, minor=True)
    ax_p.axhline(color='white', lw=1)
    ax_p.axvline(color='white', lw=1)
    ax_p.set_xlim(-2, 2)
    ax_p.set_ylim(-2, 2)
    ax_p.grid(which='minor', linestyle=':', color='gray', alpha=0.5)
    ax_p.grid(which='major', linestyle=':', color='gray')


def onclick(event):
    #['#8dd3c7', '#feffb3', '#bfbbd9', '#fa8174', '#81b1d2', '#fdb462',
    #'#b3de69', '#bc82bd', '#ccebc4', '#ffed6f'])
    global done
    goodPoint = True
    if event.xdata is None or event.ydata is None:
        goodPoint = False
    if event.button == 1 and goodPoint and not done:
        ax_p.plot(event.xdata, event.ydata, color=RED, marker='o')
        fig_p.canvas.draw()
    if event.button == 3 and goodPoint and not done:
        ax_p.plot(event.xdata, event.ydata, color=GREEN, marker='o')
        fig_p.canvas.draw()
    if done and valid_weigths():
        y = (-float(w1.get()) * event.xdata + float(bias.get())) / float(
            w2.get())
        if y > event.ydata:
            colorX = GREEN
        else:
            colorX = RED
        ax_p.plot(event.xdata, event.ydata, color=colorX, marker='o')
        fig_p.canvas.draw()


def valid_weigths():
    valid_weigths = True
    if w1.get() == "" or w2.get() == "" or bias.get() == "":
        print("Invalid weights")
        valid_weigths = False
    return valid_weigths


# GUI - Logic gates
b_and = Button(lf_log_gates, text="AND", command=perceptron_and)
b_or = Button(lf_log_gates, text="OR", command=perceptron_or)

# GUI - Weights
f_ws = Frame(lf_weights)
l_w1 = Label(master=f_ws, text="w1:")
l_w2 = Label(master=f_ws, text="w2:")
e_w1 = Entry(master=f_ws, textvariable=w1, width=10)
e_w2 = Entry(master=f_ws, textvariable=w2, width=10)
l_bias = Label(master=f_ws, text="bias:")
e_bias = Entry(master=f_ws, textvariable=bias, width=10)
b_graph = Button(master=lf_weights, text="Perceptron", command=graph)
b_restart = Button(master=f_inputData, text="Restart", command=start_over)

# GUI - Canvas
plt.style.use('dark_background')
fig_p, ax_p = plt.subplots(figsize=(8, 8))
start_graph()
cid = fig_p.canvas.mpl_connect('button_press_event', onclick)
canvas_p = FigureCanvasTkAgg(fig_p, master=f_graphs)
canvas_p.get_tk_widget().pack(padx=5, pady=5)

# Packing - Logic Gates
lf_log_gates.pack(fill=BOTH, padx=5, pady=5)
b_and.pack(fill=BOTH, padx=5, pady=5)
b_or.pack(fill=BOTH, padx=5, pady=5)

# Packing - Weights
lf_weights.pack(fill=BOTH, padx=5, pady=5)
l_w1.grid(row=0, column=0)
e_w1.grid(row=0, column=1)
l_w2.grid(row=1, column=0)
e_w2.grid(row=1, column=1)
l_bias.grid(row=2, column=0)
e_bias.grid(row=2, column=1)
f_ws.pack()
b_graph.pack(side=BOTTOM, fill=BOTH, padx=5, pady=5)
b_restart.pack(side=BOTTOM, fill=BOTH, padx=5, pady=5)

root.mainloop()
