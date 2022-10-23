# Choose your own adventure terminal game using python3 
# The player will be given prompts to move through the story, and each prompt will have a list of options to choose from. The options they choose will be stored in a list in the player object. The course of their adventure will be determined by the options they choose. To start there will be 2 endings, but the game will be built to allow for more branching and endings in the future.

class Player:
  def __init__(self, name):
    self.name = name
    self.decisions = {}
    self.current_scene = 0
  
  def __repr__(self):
    return "This is {name}, they have made these decisions {decisions}".format(name=self.name, decisions = self.decisions)
  
  def make_decision(self, decision):
    self.decisions[self.current_scene] = decision
    self.current_scene += 1

class Adventure:
  def __init__(self, player):
    self.player = player
    self.scenes = 5
    self.current_scene = 0
  
  def play(self):
    while self.current_scene < self.scenes:
      self.scenes[self.current_scene].play(self.player)
      self.current_scene += 1
    if self.current_scene == self.scenes:
      self.end_game(self.player.decisions)

  def end_game(self, decisions):
    if decisions == {0: "A", 1: "A", 2: "A", 3: "A", 4: "A"}:
      print("You win!")
    elif decisions == {0: "A", 1: "A", 2: "A", 3: "B", 4: "A"}:
      print("You win!")
    else:
      print("You lose!")

# mike = Player("Mike")
# mike.make_decision("left")
# mike.make_decision("right")

# print(mike)