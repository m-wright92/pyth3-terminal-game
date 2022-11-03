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

# Adventure class
class Adventure:
  def __init__(self, player):
    self.player = player
    self.scenes = 5
    self.current_scene = player.current_scene
  
  def play(self):
    while self.current_scene < self.scenes:
      self.current_scene = self.player.current_scene
    if self.current_scene == self.scenes:
      self.end_game(self.player.decisions)

  def end_game(self, decisions):
    if decisions == {0: "A", 1: "A", 2: "A", 3: "A", 4: "A"}:
      print("You win!")
    elif decisions == {0: "A", 1: "A", 2: "A", 3: "B", 4: "A"}:
      print("You win!")
    else:
      print("You lose!")

# Scene dictionary
scenes = {
  0: "You come to the front door of an abandoned house. All of the lights are off. Do you (A) go inside or (B) go back home?",
  1: "You are in a hallway. There is a door to your left and right, which one do you take?",
  2: "You are in a kitchen. There is a door to your left and right, which one do you take?",
  3: "You are in a bathroom. There is a door to your left and right, which one do you take?",
  4: "You are in a bedroom. There is a door to your left and right, which one do you take?",
  5: "You are in a living room. There is a door to your left and right, which one do you take?",
}

print("Please input your name and press enter to begin: ")
player = Player(input())
game = Adventure(player)
# game.play()

print("Welcome " + player.name + "!")
# print(player.current_scene)
print(scenes[player.current_scene])
player.make_decision(input())
if player.decisions[0] == ("B" or "b"):
  print("You have your wits about you and decide to go back home. You live to see another day.")
elif player.decisions[0] == ("A" or "a"):
  print("You enter the abandoned house.")

# mike = Player("Mike")
# mike.make_decision("left")
# mike.make_decision("right")

# print(mike)