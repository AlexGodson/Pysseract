
class Array(object):
    def __init__(self, cols, rows):
        self.cols = cols        
        self.rows = rows

    def array(self):
        array = []
        row = []
        unit = []
        for j in range(self.rows):
            row.append(unit)
        for i in range(self.cols):
            array.append(row)
        self.array = array
        return self.array
        

    def shape(self):
        return (f"""The array is of dimensionality:
            [{self.cols}]x[{self.rows}]
        """)
    
    @staticmethod
    def identity(size=1):
        identity=[]
        for col in range(size):
            row=[]
            for row_unit in range(size):
                if col == row_unit:
                    row.append(1)
                else:
                    row.append(0)
            identity.append(row)
        return identity

    @staticmethod
    def ones(size=1):
        ones=[]
        for col in range(size):
            row=[]
            for row_unit in range(size):
                row.append(1)
            ones.append(row)
        return ones

    @staticmethod
    def zeros(rows=1, cols=None):
        if cols == None:    
            cols=rows
        zeros=[]
        row = []
        for i in range(cols):
            row.append(0)
        for j in range(rows):
            zeros.append(row)
        return zeros