class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = []
        for string in matrix_string.strip().split("\n"):
            self.matrix.append(string.split())
        self.matrix = [
            [int(string) for string in self.matrix[i]] for i in range(len(self.matrix))
        ]

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        column_length = len(self.matrix[0])
        return [[row[i] for row in self.matrix] for i in range(column_length)][
            index - 1
        ]
