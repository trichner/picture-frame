from random_carousell import SortedCarousell

if __name__ == "__main__":
  carousell = SortedCarousell("./photos")
  for i in range(20):
    print(f"{i}: {carousell.next().path}")
