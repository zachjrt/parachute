from posixpath import split
from random import random, randrange, sample
import os.path

# import the file, not class (YET)
from classes import word
from classes import board
from classes import parachute
Word = word.Word
Board = board.Board
Parachute = parachute.Parachute



class Game:
    """The class that directs the game. 
    
    The responsibility of a Game is to control the sequence of play, load the word the player will look for and end the game.


    Attributes:
        misses (int): number of times a person can enter a wrong word.
        words_list (str): the word that the player is tryign to guess. 
    """
    def __init__(self):
        """Constructs a new instance of Game.
        
        Args:
            self (Game): An instance of Game.
        """
        self.misses = 0        
        self.words_list = self._load_words()

    def guess(self):
        """Ask the player to enter a letter.
        
        Args:
            self (Game): An instance of Game.
        Returns:
            A string value.
        """
        return input("Guess a letter a-z: ")
    
    def _load_words(self):
        """Open the text file, read each line and create the output list of words.
        
        Args:
            self (Game): An instance of Game.
        Returns:
            A list with all the posible words to choose from.
        """
        # my_path is an abspath for the current dir
        my_path = os.path.abspath(os.path.dirname(__file__))
        # path = abspath + file name = abspath for the file
        # we got the first hundred five-letter words from words-by-frequency and created a new file
        # \n is 1 character - strip before comparison to find words of x length
        path = os.path.join(my_path, "./first_hundred_five_letter_words.txt")
        output = []
        with open(path, "r") as f:
            for each_ln in f:
                output.append(each_ln.strip())
        return output

    def miss(self):
        """Increment the variable misses by one every time an incorrect letters has been chosen.
        
        Args:
            self (Game): An instance of Game.
        """
        print('Missed.')
        self.misses += 1

    def win(self):
        """Display a message if the player has won the game.
        
        Args:
            self (Game): An instance of Game.
        """
        print("You win!")
        quit()
        

    def lose(self):
        """Display a message if the player has lost the game.
        
        Args:
            self (Game): An instance of Game.
        """
        print("You lose!")
        quit()
  

    def start(self):
        """Main loop of the game, choose a ramdom word and determine if the player enter a correct letter, 
            display the board, and parachute state, and finalize the game.
        
        Args:
            self (Game): An instance of Game.
        Attributes:
            our_parachute (Parachute): an instance of Parachute
            gameplay (boolean): Whether the game continue or not.
            random_word(string): random word to be guess by the player.
            our_word (Word): an instance of Word.
            our_letters(list): Takes the word, splits it into an array so the guess can be tested against each letter.
            our_board (list): A list of hidden or guessed letters.
        """
        our_parachute = Parachute()
        gameplay = True

        random_word = sample(self.words_list, 1)[0]
        #print random word for testing bel
        #print('random_word', random_word)

        # Passing the random word to our new instance of Word
        our_word = Word()
        our_word.set(random_word)
        our_letters = our_word.split()
        our_board = Board(our_word.get())
        while gameplay:
            our_board.display()
            our_parachute.display(self.misses)
            playerGuess = self.guess()
            if playerGuess in our_word.get():
                our_board.reveal_letter(playerGuess, our_letters)
                if (our_board.board == our_letters):
                    our_parachute.display(self.misses)
                    self.win()
            else:
                self.miss()
                if (self.misses >= 4):
                    our_parachute.display(self.misses)
                    self.lose()