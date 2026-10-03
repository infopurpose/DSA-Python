def eat_mangoes(count):
  if count == 0:
    print("Hand is empty. Done1")
    return
  print("I have {count} mangoes, eating one")

  eat_mangoes(count - 1)

eat_mangoes(3)
