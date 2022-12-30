class Picture:
  def __init__(self, path):
    self.path = path


class ICarousell:
  """
  Interface describing picture carousells.
  """

  def next(self) -> Picture:
    """picks the next picture to display"""
    raise "not implemented"
