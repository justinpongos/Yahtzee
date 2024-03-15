import die
class Player:
  def __init__(self):
    """Set the 2 attributes : \n
       _dice [Dice] -> define 3 dices for the Player\n
       _points Int -> represent the point of the player
    """
    self._dice = [die.Dice(), die.Dice(), die.Dice()]
    self._dice.sort()
    self._points = 0

  def get_points(self):
    """getter for the attribute _points
    
    Returns:
        Int: actual score of the player
    """
    return self._points

  def roll_dice(self):
    """Roll all the dice of the Player and sort them
    """
    for d in self._dice:
      d.roll()
    self._dice.sort()

  def has_pair(self):
    """Compare the dices of the player and increment by one his point, if there is a pair 
    
    Returns:
        Boolean: if one pair is found return True else False
    """
    if self._dice[0] == self._dice[1] or self._dice[0] == self._dice[2] or self._dice[1] == self._dice[2]:
      self._points += 1
      return True
    return False

  def has_three_of_a_kind(self):
    """Compare the dices of the player and increment by 3 his point, if there is a triple 
    
    Returns:
        Boolean: if one triple is found return True else False
    """
    if self._dice[0] == self._dice[1] == self._dice[2]:
      self._points += 3
      return True
    return False

  def has_series(self):
    """Compare the dices of the player and increment by 2 his point, if there is a series 

    Returns:
        Boolean: if one series is found return True else False
    """
    if self._dice[2] - self._dice[1] == 1 and self._dice[1] - self._dice[0] == 1:
      self._points += 2
      return True
    return False

  def __str__(self):
    """Return a string at a certain format\n
    Ex: "D1=3, D2=5, D3=6"

    Returns:
        String: Formatted string
    """
    return f"D1={self._dice[0]}, D2={self._dice[1]}, D3={self._dice[2]}"