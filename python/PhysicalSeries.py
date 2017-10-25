import numpy as np

class PhysicalSeries:
    def __init__ (self, slope_type):
        self.series_collection = []
        filepath = "{}"
        if slope_type == "optimal":
            filepath = "./input/opt{}"
        elif slope_type == "sinus":
            filepath = "./input/sin{}"
        elif slope_type == "linje":
            filepath = "./input/lin{}"
        try:
            n = 1
            while True:
                with open(filepath.format(n), 'r') as f:
                    data = []

                    all_lines = f.readlines()

                    ## read first data line alone once to set offset for rest of data
                    l = all_lines[2].replace(',', '.')
                    l = l.split('\t')
                    offset = (float(l[0]), float(l[1]))

                    for lines in all_lines[2:]:
                        l = lines.replace(',', '.')
                        l = l.split('\t')
                        time = float(l[0]) - offset[0]
                        x = float(l[1]) - offset[1]
                        data.append( [ time, x ] )

                    data = np.array(data)
                series = (data[:,0], data[:,1])
                self.series_collection.append(series)
                n += 1
        except FileNotFoundError as e:
            print ("No file " + filepath.format(n))
