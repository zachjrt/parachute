class Parachute:
    """
        The responsability of the parachute is the display it's state.
        
    Attributes:
        parachute (list): A list of states of the parachute. 
    """
    def __init__(self):
        """Constructs a new instance of Parachute.
        
        Args:
            self (Parachute): An instance of Parachute.
        """
        self.parachute = [" ___", "/___\\", "\\   /", " \\ /", "  O", " /|\\", " / \\", "", "^^^^^^^"]
    def display(self, misses):
        """Display the state of the parachute according to the (misses) value.

        Args:
            misses (int) the number of times a have entered an incorrect value.
            self (Parachute): An instance of Parachute.
        """
        if misses >= 4:
            self.parachute[4] = "  X"
        
        for i in range(misses, len(self.parachute)):
            print(self.parachute[i])
        print()