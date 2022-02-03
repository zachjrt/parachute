class Board:

    def __init__(self):
        self.board = ["none"]

    def __init__(self, length):
        self.board = ["_" for i in range(length)]

    def display(self):
       print(" ".join(self.board))