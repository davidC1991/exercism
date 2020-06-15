import numpy as np


class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string=matrix_string

    def row(self, index):
        matriz=self.matrix_string.replace("\n",";")
        x1=np.matrix(matriz)
        x2=np.array(x1)
        return x2[index-1].tolist()

    def column(self, index):
        matriz=self.matrix_string.replace("\n",";")
        x1=np.matrix(matriz)
        x2=np.array(x1)
        return x2[:,index-1].tolist()


