from math import sin, pi
from Slope import Slope
slopeDict = {
    "optimal": {
        "data": Slope(inputfile="./input/opt1"),
        "teori": Slope(inputfile="./input/optdatafixed")
    },
    "sinus": {
        "data": Slope(inputfile="./input/sin1"),
        "teori": Slope(length=120, height=60, function=(lambda x: -6*sin(2*pi/120 * x)))
    },
    "linje": {
        "data": Slope(inputfile="./input/lin1"),
        "teori": Slope(length=120, height=60)
    }
}
