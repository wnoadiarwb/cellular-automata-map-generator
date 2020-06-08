import numpy as N
from numpy import int32, uint8, uint

class Scaler():
    def __init__(self, array, scale):
        self.inArray = array
        self.scale = scale
        self.inW = len(array)
        self.inH = len(array[0])
        self.outArray = N.zeros((self.inW*scale, self.inH*scale, 3), int32)

    def transform(self):
        if self.inW != 0 and self.inH != 0:
            for i in range(self.inW):
                for j in range(self.inH):
                    for k in range(self.scale):
                        for l in range(self.scale):
                            self.outArray[i*self.scale+k][j*self.scale+l] = self.inArray[i][j]
            return self.outArray
        else:
            return None
