class Word:
    """Word that person tries to guess
    
    The word acts as a variable to test the user's guess against. It exists in string fom as well as in array so that the guess can be checked against each letter.

    Attributes:
        value (value) : will have value in there to contain word
        letter (list) : list of words
    """
    def __init__(self):

        """Constructs a new Word.
        
        Args:
            self (word): an instance of word.
        """
        self.value = "value"
        self.letters = []
    def split(self):
        """Example text.
        
        Args:
            
        """
        return [char for char in self.value]
    def get(self):
        """Example text.
        
        Args:
            
        """
        return self.value
    def set(self, word):
        """Example text.
        
        Args:
            
        """
        self.value = word