def fade_out(color, sec=0.01):
  end = (0, 0, 0)
  np = color
  mx = max(color[0], max(color[1], color[2]))
  r_inc = np[0] / mx
  g_inc = np[1] / mx
  b_inc = np[2] / mx
  r, g, b = np
  while r >= end[0] and g >= end[1] and b >= end[2]:
    r -= r_inc
    g -= g_inc
    b -= b_inc
    rgb.fill((int(r), int(g), int(b)))
    print('r - {}, g - {}, b - {}'.format(int(r), int(g), int(b)))
    rgb.show()
    time.sleep(sec)
