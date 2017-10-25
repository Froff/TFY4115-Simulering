import math, copy
import numpy as np

class Slope:
    DIFF_STEP_SIZE = 0.001

    def __init__ (self, **kwargs):
        if "inputfile" in kwargs:
            self.setupFromFile(kwargs["inputfile"])
            return
        if not ("length" in kwargs and "height" in kwargs):
            raise TypeError("must specify either inputfile or height and length")
        length = kwargs["length"]
        height = kwargs["height"]
        self.f = (lambda x: height - height/length * x)
        for name, value in kwargs.items():
            if name == "function":
                g = copy.copy(self.f)
                h = copy.copy(value)
                self.f = (lambda x: g(x) + h(x))
            elif name == "functionoverride":
                self.f = copy.copy(value)
        self.dydx = self.default_dydx
        self.begin = 0
        self.end = length

    def default_dydx (self, x, **kwargs):
        f = self.f
        step_size = Slope.DIFF_STEP_SIZE
        for name, value in kwargs.items():
            if name == "step size":
                step_size = value
        y_last = f(x - step_size)
        y_next = f(x + step_size)
        return (y_next - y_last) / (2 * step_size)

    def setupFromFile(self, filename):
        with open(filename) as inputfile:
            data = []
            for line in inputfile.readlines()[2:]:
                l = line.replace(",", ".")
                l = l.split("\t")
                data.append([ float(l[1]), float(l[2]) ])
            data = np.array(data)
        offset = data[0,0], data[-1,1]
        coefficients = np.polyfit(data[:,0], data[:,1], 30)
        self.f = (lambda x: np.polyval(coefficients, (x + offset[0])) - offset[1])
        ddx_coefficients = np.polyder(coefficients)
        self.dydx = (lambda x: np.polyval(ddx_coefficients, (x + offset[0])))
        self.begin = 0
        self.end = data[-1,0] - offset[0]
