import math

class Body:
    def __init__ (self, mass, radius, **kwargs):
        self.mass = mass
        self.radius = radius
        self.shape = "point mass"
        for name, value in kwargs.items():
            if name == "shape":
                self.shape = value
        self.setMomentOfInertia()

    def setMomentOfInertia(self):
        m = self.mass
        r = self.radius
        shape = self.shape
        if shape == "sphere":
            self.mom_inertia = m * r**2 * 2/5
        elif shape == "sphere shell":
            self.mom_inertia = m * r**2 * 2/3
        elif shape == "cyllinder shell":
            self.mom_inertia = m * r**2 * 2
        elif shape == "point mass":
            self.mom_inertia = 0
        else:
            raise ValueError ("Argument 'shape' did not match any recognized values.")
