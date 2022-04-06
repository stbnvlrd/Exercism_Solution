class Matrix:
    def __init__(self, matrix_string):
        x = matrix_string.rsplit("\n")
        print(x)

        y = []
        count = 0

        for i in x:
            z = i.rsplit(" ")
            z_new = [int(j) for j in z]
            y.append(z_new)
            count = count + 1
            
        print(y)
        self.matrix = y

    def row(self, index):
        row_sel = self.matrix[index-1]
        print("row[x] =", row_sel)
        return row_sel

    def column(self, index):
        column = [];
        for row in self.matrix:
            column.append(row[index-1])
        return column


