class Parachute:
    def __init__(self):
        self.parachute = [" ___", "/___\\", "\\   /", " \\ /", "  O", " /|\\", " / \\", "", "^^^^^^^"]
    def display(self, misses):
        if misses >= 4:
            self.parachute[4] = "  X"
        
        for i in range(misses, len(self.parachute)):
            print(self.parachute[i])
        print()