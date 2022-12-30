import os

from icarousell import ICarousell, Picture


class SortedCarousell(ICarousell):
  def __init__(self, folder):
    files = os.listdir(folder)
    self.files = sorted(files)
    self.position = 0

  def next(self) -> Picture:
    p = self.files[self.position % len(self.files)]
    self.position += 1
    return Picture(p)
