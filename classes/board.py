class Board:
    """The Board will display some clues about the word, like the lenght of the word,
        and each guessed letter by the player. 
    
    Attribute: 
        board (list): A list that holds all the _ or the guessed letters.
        
    """
    def __init__(self):
        """Constructs a new instance of Board.
        
        Args:
            self (Board): An instance of Board.
        """
        self.board = ["none"]

    def __init__(self, word):
        """display _ for each letter in the word.
        
        Args:
            self (Board): An instance of Board.
            word (string): The word to be guess by the player.
        """
        self.word = word
        self.board = ["_" for i in range(len(word))]
    
    def reveal_letter(self, guess, letters):
        """If the player enters a letter that is part of the word then the empty space will be replaced by the letter.
                
        Args:
            self (Board): An instance of Board.
            guess (string): the letter entered by the player.
            letters (list): the list of letter in the word.
        """
        for i in range(len(self.word)):
           if (guess == letters[i]):
               self.board[i] = guess
        # update the board to reveal all instances of the letter in the word
        pass

    def display(self):
        """Display _ for each letter not guessed and the guessed letters separated by a space.
        
        Args:
            self (Board): An instance of Board.
        """
        print(" ".join(self.board))