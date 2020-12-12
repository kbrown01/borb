from decimal import Decimal
from typing import List


class Matrix:
    """
    In mathematics, a matrix (plural matrices) is a rectangular array or table of numbers, symbols, or expressions, arranged in rows and columns.
    Provided that they have the same size (each matrix has the same number of rows and the same number of columns as the other),
    two matrices can be added or subtracted element by element (see conformable matrix).

    The rule for matrix multiplication, however, is that two matrices can be multiplied only when the number of columns
    in the first equals the number of rows in the second (i.e., the inner dimensions are the same, n for an (m×n)-matrix times an (n×p)-matrix,
    resulting in an (m×p)-matrix). There is no product the other way round—a first hint that matrix multiplication is not commutative.
    Any matrix can be multiplied element-wise by a scalar from its associated field.
    """

    def __init__(self):
        self.mtx = [[], [], []]

    @staticmethod
    def identity_matrix() -> "Matrix":
        """
        The identity matrix In of size n is the n-by-n matrix in which all the elements on the main diagonal are equal to 1 and all other elements are equal to 0.
        """
        m = Matrix()
        m.mtx = [
            [Decimal(1), Decimal(0), Decimal(0)],
            [Decimal(0), Decimal(1), Decimal(0)],
            [Decimal(0), Decimal(0), Decimal(1)],
        ]
        return m

    @staticmethod
    def matrix_from_six_values(
        a: Decimal, b: Decimal, c: Decimal, d: Decimal, e: Decimal, f: Decimal
    ):
        """
        This method returns the matrix [[a, b, 0], [c, d, 0], [e, f, 1]]
        """
        m = Matrix()
        m.mtx = [[a, b, Decimal(0)], [c, d, Decimal(0)], [e, f, Decimal(1)]]
        return m

    def mul(self, y: "Matrix") -> "Matrix":
        m_vals = [
            [Decimal(0), Decimal(0), Decimal(0)],
            [Decimal(0), Decimal(0), Decimal(0)],
            [Decimal(0), Decimal(0), Decimal(0)],
        ]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    m_vals[i][j] += self.mtx[i][k] * y.mtx[k][j]
        m = Matrix()
        m.mtx = m_vals
        return m

    def cross(self, x: float, y: float, z: float):
        x2 = x * self[0][0] + y * self[1][0] + z * self[2][0]
        y2 = x * self[0][1] + y * self[1][1] + z * self[2][1]
        z2 = x * self[0][2] + y * self[1][2] + z * self[2][2]
        return x2, y2, z2

    def __getitem__(self, item) -> List[Decimal]:
        return self.mtx[item]

    def __str__(self):
        return "[[%f %f %f]\n [%f %f %f]\n [%f %f %f]]" % (
            self.mtx[0][0],
            self.mtx[0][1],
            self.mtx[0][2],
            self.mtx[1][0],
            self.mtx[1][1],
            self.mtx[1][2],
            self.mtx[2][0],
            self.mtx[2][1],
            self.mtx[2][2],
        )

    def __deepcopy__(self, memodict={}):
        m = Matrix()
        m.mtx = [
            [self.mtx[0][0], self.mtx[0][1], self.mtx[0][2]],
            [self.mtx[1][0], self.mtx[1][1], self.mtx[1][2]],
            [self.mtx[2][0], self.mtx[2][1], self.mtx[2][2]],
        ]
        return m