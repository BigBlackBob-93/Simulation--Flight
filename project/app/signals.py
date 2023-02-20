from PyQt6.QtWidgets import QTableWidgetItem
import pyqtgraph as pg
from math import (cos, sin, radians, sqrt)
from objects import (param, launch_btn, clear_btn, table)

count = 0
G = 9.81
C = 0.15
RHO = 1.29
Y: list[float] = []
X: list[float] = []


def start():
    global count, Y, X
    count += 1
    X.clear()
    Y.clear()

    data: list[float] = []
    for sb in param.values():
        data.append(sb.value())

    angle = radians(data[1])
    cosa = cos(angle)
    sina = sin(angle)

    beta: float = 0.5 * C * data[2] * RHO
    k: float = beta / data[3]
    x = 0
    y = data[0]
    dt = data[5]
    X.append(x)
    Y.append(y)
    vx: float = data[4] * cosa
    vy: float = data[4] * sina

    root: float = sqrt(vx * vx + vy * vy)
    vx = vx - k * vx * root * dt
    vy = vy - (G + k * vy * root) * dt
    x = x + vx * dt
    y = y + vy * dt
    X.append(x)
    Y.append(y)

    while y > 0:
        root: float = sqrt(vx * vx + vy * vy)
        vx = vx - k * vx * root * dt
        vy = vy - (G + k * vy * root) * dt
        x = x + vx * dt
        y = y + vy * dt
        X.append(x)
        Y.append(y)

    speed = sqrt(vx * vx + vy * vy)
    results(dt, x, max(Y), speed)
    draw()


def draw():
    theTitle = "Simulation: Flight - GRAPH"
    plt = pg.plot(X, Y, title=theTitle, pen='r')
    plt.showGrid(x=True, y=True)


def results(dt: float, x: float, max: float, speed: float):
    table.insertRow(count - 1)
    table.setItem(count - 1, 0, QTableWidgetItem(str(dt)))
    table.setItem(count - 1, 1, QTableWidgetItem(str(round(x, 2))))
    table.setItem(count - 1, 2, QTableWidgetItem(str(round(max, 2))))
    table.setItem(count - 1, 3, QTableWidgetItem(str(round(speed, 2))))


def clear():
    global count
    if count > 0:
        table.setRowCount(0)
        count = 0


launch_btn.clicked.connect(start)
clear_btn.clicked.connect(clear)
