def sparkle(background, foreground, loop = 10, delay=0.1):
  for outer in range(loop):
    np.fill(background)
    for i in range(np.n / 4):
      np[random.randint(0, np.n-1)] = foreground
    np.show()
    time.sleep(delay)
