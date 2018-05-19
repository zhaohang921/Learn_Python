from array import Array2D

class Matrix:
    def __init__(self, numRows, numCols):
        self._theGrid = Array2D(numRows, numCols)
        self._theGrid.clear(0)

    def numCols(self):
        return self._theGrid.numRows()

    def numRows(self):
        return self._theGrid.numCols()

    def __getitem__(self, ndxTuple):
        return self._theGrid[ndxTuple[0], ndxTuple[1]]

    def __setitem__(self, ndxTuple, scalar):
        self._theGrid[ndxTuple[0], ndxTuple[1]] = scalar

    def scaleBy(self, scalar):
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                self[r, c] *= scalar

    def tranpose(self):
        pass

    def __add__(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numRows() and \
               rhsMatrix.numCols() == self.numCols(), \
               "Matrix sizes not compatible for the add operation."

        newMatrix = Matrix(self.numRows(), self.numCols())
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                newMatrix[r, c] = self.[r, c] + rhsMatrix[r, c]

        return newMatrix

    def __sub__(self, rhsMatrix):
        pass

    def __mul__(self, rhsMatrix):
        pass


