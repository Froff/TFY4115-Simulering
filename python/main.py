#!/usr/bin/python3
import matplotlib.pyplot as plt
import matplotlib.text as txt
import numpy as np
import math
import sys
from Slope import Slope
from SlopeDict import slopeDict
from Simulation import Simulation
from PhysicalSeries import PhysicalSeries
import os.path

slope_type = "linje"
if __name__ == "__main__":
    try:
        slope_type = sys.argv[1]
    except IndexError:
        print("Usage: main.py <linje|optimal|sinus>")
        exit(2)

data_slope = slopeDict[slope_type]["data"]
theory_slope = slopeDict[slope_type]["teori"]
physical_series = PhysicalSeries(slope_type)

t_axis = [0]

data_sim = Simulation(data_slope, momentofintertiacoefficient = 2/3)
theory_sim = Simulation(theory_slope, momentofintertiacoefficient = 2/3)

data_sim.runSimulation()
theory_sim.runSimulation()

print("Slope type is {}".format(slope_type))
print("End time for data based slope: {}".format(data_sim.t[-1]))
print("End time for theoretical slope: {}".format(theory_sim.t[-1]))

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
data_plot = ax.plot(data_sim.t, data_sim.x, color='blue')
theory_plot = ax.plot(theory_sim.t, theory_sim.x, color='orange')
for series in physical_series.series_collection:
    #### Plots x(t) for a single physical test ####
    physical_plot = ax.plot(series[0], series[1], color='red', linewidth=0.2)
ax.set_xlabel("t (s)")
ax.set_ylabel("x (cm)")
ax.set_title("Bane av typen {}".format(slope_type))
ax.legend((data_plot[0], theory_plot[0], physical_plot[0]), ("Simulering, fysisk bane", "Simulering, teoretisk bane", "Forsøk"))

#plt.show()
