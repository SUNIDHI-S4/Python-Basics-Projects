import math
import random
import game

class Player :
    def __init__(self,letter):
        #letter is 'x' or 'o'
        self.letter = letter
    
    #we want all players to get their next move
    def get_move(self,game) :
        pass

class RandomComputerPlayer(Player) :
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        square = random.choice(game.available_moves())

class HumanPlayer(Player) :
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False



