# Choose your own adventure terminal game using python3 
# The player will be given prompts to move through the story, and each prompt will have a list of options to choose from. The options they choose will be stored in a list in the player object. The course of their adventure will be determined by the options they choose. To start there will be 2 endings, but the game will be built to allow for more branching and endings in the future.

class Player:
  def __init__(self, name):
    self.name = name
