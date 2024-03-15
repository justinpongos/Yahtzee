#  Name: Louis Pavlovsky & Justin Pongos
#  Date: 02/26/24
#  Desc: This program is the game Yahtzee. It is a game where the user rolls three dice and tries to get a Yahtzee. Yahtzee being if the number is three of the same kind or there is a pair or the numbers are a series(acending numbers). The user get a certain amount of points for each category one to three. The player can play as many time as they want until they decice they dont wanna play and will be shown their final score from all the games.

from player import Player
import check_input

def take_turn(player):
  """ Use the method of the Ojject Player to determine if the user won or not
  Args:
      player (Player): Object that hold the information of the player
  """
  player.roll_dice()
  print(player)
  if player.has_three_of_a_kind() == True:
    print("You got 3 of a kind!")
  elif player.has_pair() == True:
    print("You got a pair!")
  elif player.has_series() == True:
    print("You got a series of 3!")
  else:
    print("Aww. Too Bad.")
  print(f"Score = {player.get_points()}")

def main():
  player = Player()
  isPlaying = True
  print("-Yahtzee-\n")
  while isPlaying:
    take_turn(player)
    if (check_input.get_yes_no("Play again? (Y/N): ") == False):
      isPlaying = False
    print("")
  print(f"Game Over.\nFinal Score = {player.get_points()}")

main()
