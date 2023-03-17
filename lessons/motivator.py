import random

a = "You're doing great. "
b = "You've been awesome today. "
c = "You're on a roll. "

x = "Keep up the good work!"
y = "Keep pushing!"
z = "Let's keep at it!"

def motivate() -> str:
  """Returns a string with a randomly chosen motivator."""
  s = random.choice([a, b, c]) + random.choice([x, y, z])
  return s
