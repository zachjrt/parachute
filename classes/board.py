class Board:
    """Example text. 
    
    Example text.

    Attributes:
        
    """
    def __init__(self):
        """Example text.
        
        Args:
            
        """
        self.board = ["none"]

    def __init__(self, word):
        """Example text.
        
        Args:
            
        """
        self.word = word
        self.board = ["_" for i in range(len(word))]
    
    def reveal_letter(self, guess, letters):
        """Example text.
        
        Args:
            
        """
        for i in range(len(self.word)):
           if (guess == letters[i]):
               self.board[i] = guess
        # update the board to reveal all instances of the letter in the word
        pass

    def display(self):
        """Example text.
        
        Args:
            
        """
        print(" ".join(self.board))