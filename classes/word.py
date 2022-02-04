class Word:
    def __init__(self, value="None"):
        self.value = value
        self.letters = []
    def split(self):
        return [char for char in self.value]