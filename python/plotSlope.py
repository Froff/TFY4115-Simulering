#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np
import sys
from math import sin, pi
from Slope import Slope
from SlopeDict import slopeDict

slope_type = "linje"
if __name__ == "__main__":
    try:
        slope_type = sys.argv[1]
    except IndexError:
        print("Usage: main.py <linje|optimal|sinus>")
        exit(2)
data_slope = slopeDict[slope_type]["data"]
theory_slope = slopeDict[slope_type]["teori"]

x_axis_data = np.linspace(data_slope.begin, data_slope.end, num = 200)
data_axis = []
for x in x_axis_data:
    data_axis.append(data_slope.f(x))

x_axis_theory = np.linspace(theory_slope.begin, theory_slope.end, num = 200)
theory_axis = []
for x in x_axis_theory:
    theory_axis.append(theory_slope.f(x))

fig = plt.figure()
ax = fig.add_subplot(1,1,1, aspect="equal")
ax.set_xlabel("Horisontal (cm)")
ax.set_ylabel("Vertikal (cm)")
data_plot = ax.plot(x_axis_data, data_axis)
theory_plot = ax.plot(x_axis_theory, theory_axis)
ax.legend((data_plot[0], theory_plot[0]), ("Fysisk bane", "Teoretisk ligning"))
plt.show()
