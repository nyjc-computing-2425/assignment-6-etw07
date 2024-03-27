from datetime import datetime
import time


# Part 1
def clock(n):
  # Your code here
  """returns the current time for n seconds"""
  for i in range(n):
    now = datetime.now()
    print(now.strftime('%H:%M:%S'),end = "\r")
    time.sleep(1)
  pass


# Part 2
def lcm(a, b):
  # Your code here
  """returns the lowest common multiple of a and b"""
  a_ori = a
  b_ori = b
  while a != b:
    if a < b:
      a += a_ori
    else:
      b += b_ori
  return a
  pass


# Part 3
def gcf(a, b):
  # Your code here
  """returns the greatest common factor of a and b"""
  while b != 0:
    r = a%b
    a = b
    b = r
  return a
  pass
