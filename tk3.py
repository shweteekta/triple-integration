import tkinter
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_tkagg import (
                                    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

from scipy import integrate

#formula for calculating volume of cube using scipy tripquad
f = lambda z, y, x: 1


root = tkinter.Tk()
root.wm_title("Triple Integration")


side1=0

e1 = tkinter.Entry(root)
#e1.insert(,"enter side")
e1.pack()

#side1=int(e1.get())
'''
cube_definition = [
        (0,0,0), (0,side1,0), (side1,0,0), (0,0,side1)
        ]
cube_definition_array = [
    np.array(list(item))
    for item in cube_definition
]

points = []
points += cube_definition_array
vectors = [
    cube_definition_array[1] - cube_definition_array[0],
    cube_definition_array[2] - cube_definition_array[0],
    cube_definition_array[3] - cube_definition_array[0]
]

points += [cube_definition_array[0] + vectors[0] + vectors[1]]
points += [cube_definition_array[0] + vectors[0] + vectors[2]]
points += [cube_definition_array[0] + vectors[1] + vectors[2]]
points += [cube_definition_array[0] + vectors[0] + vectors[1] + vectors[2]]

points = np.array(points)

edges = [
    [points[0], points[3], points[5], points[1]],
    [points[1], points[5], points[7], points[4]],
    [points[4], points[2], points[6], points[7]],
    [points[2], points[6], points[3], points[0]],
    [points[0], points[2], points[4], points[1]],
    [points[3], points[6], points[7], points[5]]
]

'''

def hek():
    global side1

    side1=int(e1.get())
    cube_definition = [
        (0,0,0), (0,side1,0), (side1,0,0), (0,0,side1)
        ]
    cube_definition_array = [
        np.array(list(item))
        for item in cube_definition
    ]

    points = []
    points += cube_definition_array
    vectors = [
        cube_definition_array[1] - cube_definition_array[0],
        cube_definition_array[2] - cube_definition_array[0],
        cube_definition_array[3] - cube_definition_array[0]
    ]

    points += [cube_definition_array[0] + vectors[0] + vectors[1]]
    points += [cube_definition_array[0] + vectors[0] + vectors[2]]
    points += [cube_definition_array[0] + vectors[1] + vectors[2]]
    points += [cube_definition_array[0] + vectors[0] + vectors[1] + vectors[2]]

    points = np.array(points)

    edges = [
        [points[0], points[3], points[5], points[1]],
        [points[1], points[5], points[7], points[4]],
        [points[4], points[2], points[6], points[7]],
        [points[2], points[6], points[3], points[0]],
        [points[0], points[2], points[4], points[1]],
        [points[3], points[6], points[7], points[5]]
    ]


    '''
    fig = Figure(figsize=(5, 4), dpi=100)

    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    canvas.draw()ax = fig.add_subplot(111, projection="3d")
    
    ax = fig.add_subplot(111, projection="3d")
    '''





    faces = Poly3DCollection(edges, linewidths=1, edgecolors='k')
    faces.set_facecolor((0,0,1,0.1))
    ax.add_collection3d(faces)
    ax.scatter(points[:,0], points[:,1], points[:,2], s=0) 
    ax.set_aspect('equal')
    #t = np.arange(0, 3, .01)
    #ax.plot(t, 2 * np.sin(2 * np.pi * t))

    #toolbar = NavigationToolbar2Tk(canvas, root)
    #toolbar.update()

    answer=integrate.tplquad(f, 0, side1, lambda x: 0, lambda x: side1,
                  lambda x, y: 0, lambda x, y: side1)

    T = tkinter.Text(root, height=10, width=30)
    T.pack()
    final=f"Volume of cube with side{side1} is :{answer[0]}"
    T.insert(tkinter.END, final)
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


    tkinter.mainloop()




button = tkinter.Button(root, text='plot and calculate', width=25, command=hek)
button.pack()








fig = Figure(figsize=(5, 4), dpi=100)

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
ax = fig.add_subplot(111, projection="3d")
tkinter.mainloop()