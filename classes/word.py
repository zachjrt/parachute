class Word:
    """Word that person tries to guess
    
    The word acts as a variable to test the user's guess against. It exists in string fom as well as in array so that the guess can be checked against each letter.

    Attributes:
        value (value) : will have value in there to contain word
        letter (list) : list of words
    """

    _value = None

    def __init__(self):

        """Constructs a new Word.
        
        Args:
            self (Word): an instance of Word.
        """
        self._value = "value"
        self.letters = []
    def split(self):
        """Returns a list with the letters of the word.
        
        Args:
            self (Word): an instance of Word.
        """
        return [char for char in self._value]
    def get(self):
        """Returns the chosen random word.
        
        Args:
            self (Word): an instance of Word.
        """
        return self._value
    def set(self, word):
        """Set the chosen random word to the variable.
        
        Args:
            self (Word): an instance of Word.
        """
        self._value = word