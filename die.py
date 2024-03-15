import random
class Dice:
  def __init__(self, sides=6):
    """Set the logic of the Dice with 2 attributes.\n
      _sides Int -> Represent the numbers of side the dice got\n
      _value Int -> Actual value of the dice

      Args:
          sides (int, optional): Side of the dice. Defaults to 6.
      """
    self._sides = sides
    self._value = 0

  def roll(self):
    """Get a random number between 1, _sides, and set the attribe _value the res

      Returns:
          Int: Value of the dice
      """
    res_dice = random.randint(1, self._sides)
    self._value = res_dice
    return res_dice

  def __str__(self):
    """Format the attribute _value to a String

      Returns:
          String: Attribute value
      """
    return str(self._value)

  def __lt__(self, other):
    """ Compare if the attribute _value of the current object is lesser than the other Dice 

      Args:
          other (Dice): Other Object dice

      Returns:
          Boolean: if current Dice is lesser than the other dice return True else False
      """
    return self._value < other._value

  def __eq__(self, other):
    """Compare the equality of the attribute _value of the current object and the other Dice

      Args:
          other (Dice): Other Object dice

      Returns:
          Boolean: if current Dice is equal to the other dice return True else False
      """
    return self._value == other._value

  def __sub__(self, other):
    """Substract the attribute _value of the current object and the other Dice

      Args:
          other (Dice): Other Object dice

      Returns:
          Int: Result of substraction between current object and the other one
      """
    return self._value - other._value
