import os

from icarousell import ICarousell, Picture


class RandomCarousell(ICarousell):
  def __init__(self, folder):
    self.files = os.listdir(folder)

  def next(self) -> Picture:
    p = "TODO"  # TODO: randomly pick a file
    return Picture(p)
