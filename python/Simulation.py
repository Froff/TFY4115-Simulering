from math import sqrt
import Slope

class Simulation:
    SIM_STEP_SIZE = 0.0001
    const_g = -981

    def __init__ (self, slope, **kwargs):
        self.slope = slope
        self.t = [0]
        self.x = [Simulation.SIM_STEP_SIZE]
        self.mom_inertia_coefficient = 0
        for name, value in kwargs.items():
            if name == "startingposition":
                self.x = [value]
            if name == "momentofintertiacoefficient":
                self.mom_inertia_coefficient = value

    def runSimulation(self):
        while not self.isFinished():
            self.step()

    def step (self):
        x = self.x[-1]
        dydx = self.slope.dydx(x)
        y = self.slope.f(x) - self.slope.f(0)
        I = self.mom_inertia_coefficient
        g = Simulation.const_g
        step_size = Simulation.SIM_STEP_SIZE
        try:
            self.x.append(x + step_size * sqrt( (2*g*y) / ( (1 + I) * (1 + dydx**2) ) ))
            self.t.append(self.t[-1] + Simulation.SIM_STEP_SIZE)
        except ValueError:
            print("Math domain error. x={}, y={}".format(x, y))
            exit(2)

    def isFinished (self):
        return self.x[-1] >= self.slope.end
