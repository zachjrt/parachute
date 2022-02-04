class Parachute:
    """Example text. 
    
    Example text.

    Attributes:
        
    """
    def __init__(self):
        """Example text.
        
        Args:
            
        """
        self.parachute = [" ___", "/___\\", "\\   /", " \\ /", "  O", " /|\\", " / \\", "", "^^^^^^^"]
    def display(self, misses):
        """Example text.
        
        Args:
            
        """
        if misses >= 4:
            self.parachute[4] = "  X"
        
        for i in range(misses, len(self.parachute)):
            print(self.parachute[i])
        print()