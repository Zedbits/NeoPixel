def chase(color1, color2, loop=10, delay=0.1):
  result = 0
  for outer in range(loop):
    np.fill(color1)
    for i in range(np.n):
      if i % 3 == result:
        np[i] = color2
    np.show()
    time.sleep(delay)
    result = (result + 1) % 3
