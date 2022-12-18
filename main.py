import random
for i in range(10):
  # seed=random.seed(1.9999*int(input("seed")))
  n = random.randint(1, 2)
  if n == 1:
    print("Heads")
  else:
    print("Tails")
  print(n)
