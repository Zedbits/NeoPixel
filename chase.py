def chase(background, foreground, loop=10, delay=0.1):
  result = 0
  for outer in range(loop):
    np.fill(background)
    for i in range(np.n):
      if i % 3 == result:
        np[i] = foreground
    np.show()
    time.sleep(delay)
    result = (result + 1) % 3
