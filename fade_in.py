def fade_in(color, sec=0.01):
  np = color
  start = (0, 0, 0)
  mx = max(np[0], max(np[1], np[2]))
  r_inc = np[0]/mx
  g_inc = np[1]/mx
  b_inc = np[2]/mx
  r, g, b = start
  while r < np[0] and g < np[1] and b < np[2]:
    r += r_inc
    g += g_inc
    b += b_inc
    rgb.fill((int(r), int(g), int(b)))
    print('r - {}, g - {}, b - {}'.format(int(r), int(g), int(b)))
    rgb.show()
    time.sleep(sec)
