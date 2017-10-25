#!/usr/bin/python3
x = []
y = []
with open("./input/optdata", "r") as f:
    for line in f.readlines()[2:]:
        l = line.replace(',', '.')
        l = l.split("\t")
        x.append(float(l[2]))
        y.append(float(l[1]))
x.reverse()
y.reverse()
with open("./input/optdatafixed", "w") as f:
    f.write("BLAH BLAH HEADER INFO!\n")
    f.write("BLAH BLAH HEADER INFO HERE TOO!\n")
    for i in range(0, len(x)):
        f.write("{}\t{}\t{}\n".format("NaN", x[i], y[i]))
