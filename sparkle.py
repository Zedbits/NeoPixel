def sparkle(color1, color2, loop = 10, delay=0.1):
  for outer in range(loop):
    np.fill(color1)
    for i in range(np.n / 4):
      np[random.randint(0, np.n-1)] = color2
    np.show()
    time.sleep(delay)
