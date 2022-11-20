from Array import Array


def print_mat(matrix):
    print("[")
    for row in range(len(matrix)):
        print("[", end="")
        for unit in range(len(matrix[row])):
            print(matrix[row][unit], end=", ") if unit!=len(matrix[row])-1 else print(matrix[row][unit], end="]\n")
    print(" ]\n")

def row_by_col(col:list, row:list):
    if len(row) != len(col):
        raise IndexError(f"""Row_by_Col: The Dimensions of the given matrices don't match up""")
    else:
        return sum(a*b for a,b in zip(row, col))

def cross_multiply(mat_A: object, mat_B: object):
    # Cross multiply A with B == [A] x [B]
    if mat_A.cols_size != mat_B.rows_size:
        raise IndexError(
        f"""Cross_Multiply_Function: The Dimensions of the given matrices don't match up 
        [{mat_A.rows_size}*{mat_A.cols_size}] X [{mat_B.rows_size}*{mat_B.cols_size}]"""
        )
    else:
        mat_B_transpose = mat_B.transpose()
        product = []
        for i in range(mat_A.rows_size):
            row = []
            for j in range(mat_B.cols_size):
                row.append(row_by_col(col=mat_A.matrix[i], row=mat_B_transpose[j]))
            product.append(row)
        return product
    
def dot_product(mat_A:object, mat_B:object):
    if mat_A.cols_size != mat_B.col_size:
        raise IndexError(
        f"""Dot Product_function: The Dimensions of the given matrices don't match up 
        [{mat_A.rows_size}*{mat_A.cols_size}] X [{mat_B.rows_size}*{mat_B.cols_size}]"""
        )
    else:
        pass


class Matrix(object):
    def __init__(self, mat):
        self.matrix = mat
        self.rows = [i for i in self.matrix]
        self.cols = []
        self.rows_size = len(mat)
        self.cols_size = len(mat[0])

    def print_matrix(self):
        print_mat(self.matrix)

    @staticmethod
    def identity(size=1, show=False):
        identity = Array.identity(size)
        if show:
            print_mat(identity)
        return identity

    @staticmethod
    def ones(size=1, show=False):
        ones = Array.ones(size)
        if show:
            print_mat(ones)
        return ones

    @staticmethod
    def zeros(rows=1, cols=None, show=False):
        if cols == None:
            cols = rows
        zeros = Array.zeros(rows=rows, cols=cols)
        if show:
            print_mat(zeros)
        return zeros
    
    def transpose(self, show=False):
        transpose_mat = []
        for j in range(self.cols_size):
            row = []
            for i in range(self.rows_size):
                row.append(self.matrix[i][j])
            transpose_mat.append(row)
            transpose_mat = list(transpose_mat)
        if show:
            print_mat(transpose_mat)
        return transpose_mat

    def matrix_scalar(self, scalar, show=False):
        for row in range(self.rows_size):
            for col in range(self.cols_size):
                self.matrix[row][col] *= scalar
        if show:
            self.print_matrix()
        return self.matrix

    def matrix_cross(self, matrix_B: object):
        if self.cols_size != matrix_B.rows_size:
            raise IndexError(
            f"""The Dimensions of the given matrices don't match up 
            [{self.rows_size}*{self.cols_size}] X [{matrix_B.rows_size}*{matrix_B.cols_size}]"""
            )
        else:
            product = cross_multiply(mat_A=self, mat_B=matrix_B)
            return product

    def matrix_dot(self, matrix_B: object):
        print(matrix_B.matrix)