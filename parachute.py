from random import random, randrange


import random

wordList = ["secret", "house", "hedgehog"]
#head = "O"
#parachute = ["___", "/___\\", "\\   /", "\\/", head, "/|\\", "/ \\"]


class Word:
    def __init__(self):
        self.value = "none"
    def random(self):
        self.value = wordList[randrange(0, len(wordList))]

class Board:
    def __init__(self):
        self.value = "none"
class Parachute:
    def __init__(self):
        self.head = "  O"
        self.parachute = [" ___", "/___\\", "\\   /", " \\ /", self.head, " /|\\", " / \\"]
    def display(self, misses):
        for i in range(misses, len(self.parachute)):
            print(self.parachute[i])



class Game:
    def __init__(self):
        self.misses = 0        

    def guess(self):
        return input("Guess a letter a-z:")
    def miss(self):
        self.misses += 1

def main():
    game = Game()
    parachute = Parachute()
    gameplay = True
    while (gameplay):
        randomWord = Word()
        randomWord.random()
        playerGuess = game.guess()
        if(playerGuess == randomWord.value):
            parachute.display(game.misses)
        else:
            game.miss()

if __name__ == "__main__":
    main()