import board
import neopixel
import time
import random
BRIGHTNESS = .5
num_pixels = 10
np = neopixel.NeoPixel(board.NEOPIXEL, num_pixels, brightness=BRIGHTNESS, auto_write=False)
"""
Function: sparkle
Description: a chosen foreground color flashes randomly on a chosen background color.
Parameters: color1&2(tuples) - color1 is background, color2 is foreground. delay(floating
point) - time between flashes. loop (int) is the time the light flashes
Return: none
"""
def sparkle(color1, color2, loop = 10, delay=0.1):
  for outer in range(loop):
    np.fill(background)
    for i in range(np.n / 4):
      np[random.randint(0, np.n-1)] = foreground
    np.show()
    time.sleep(delay)
'''
Function: chase
Description: The foreground color chases other instances of the foreground color on a
backdrop of
the background color
Parameters: color1&2(tuple) - color1 is background, color2 is foreground. loop(int) is how much
the
color moves around. count(int) is the space between chasing pixels. delay(floating
point)
is the time it takes to move color
Return value: none
'''
def chase(color1, color2, loop=20, count=3, delay=0.1):
  result = 0
  for outer in range(count*loop):
    np.fill(color1)
    for i in range(num_pixels):
      if i % count == result:
        np[i] = color2
  np.show()
  time.sleep(delay)
  result += 1
  result %= count
'''
Function: fade_in
Description: This function fades a color in from black.
Parameters: color(tuple) - the color that is being faded in, delay(floating point)
is the time it takes to start fading in
Return value: none
'''
def fade_in(color, delay=0.01):
  pix = color
  start = (0, 0, 0)
  mx = max(pix[0], max(pix[1], pix[2]))
  r_inc = pix[0]/mx
  g_inc = pix[1]/mx
  b_inc = pix[2]/mx
  r, g, b = start
  while r < pix[0] and g < pix[1] and b < pix[2]:
    r += r_inc
    g += g_inc
    b += b_inc
    np.fill((int(r), int(g), int(b)))
    print('r - {}, g - {}, b - {}'.format(int(r), int(g), int(b)))
    np.show()
    time.sleep(delay)
'''
Function: fade_out
Description: This function fades a color to black
Parameters: color(tuple) - the starting color that is being faded to black,
delay(floating point)
is the time needed to fade out
Return value: none
'''
def fade_out(color, delay=0.01):
  end = (0, 0, 0)
  pix = color
  mx = max(color[0], max(color[1], color[2]))
  r_inc = pix[0] / mx
  g_inc = pix[1] / mx
  b_inc = pix[2] / mx
  r, g, b = pix
  while r >= end[0] and g >= end[1] and b >= end[2]:
    r -= r_inc
    g -= g_inc
    b -= b_inc
    np.fill((int(r), int(g), int(b)))
    print('r - {}, g - {}, b - {}'.format(int(r), int(g), int(b)))
    np.show()
    time.sleep(delay)
while True:
# fades black to red
fade_in((255, 1, 1))
# starts sparkling with yellow color
sparkle((255, 0, 0), (255, 211, 0))
# fades to black
fade_out((255, 1, 1))
# fades in yellow
fade_in((255, 211, 1))
# chases with red
chase((255, 211, 1), (255, 1, 1), loop=10, count=4, delay=.1)
# fades to black
fade_out((255, 211, 1))
# fades in green
fade_in((103, 228, 1))
# sparkles with blue color
sparkle((103, 228, 1), (11, 68, 172))
# fades out
fade_out((103, 228, 1))
# fades in blue
fade_in((11, 68, 172))
# chases with green
chase((11, 68, 172), (103, 228, 1), loop=10, count=3, delay=.1)
# fades out
fade_out((11, 68, 172))
# fades in cyan
fade_in((1, 167, 130))
# sparkles with magenta
sparkle((1, 167, 130), (204, 1, 119))
# fades out
fade_out((1, 167, 130))
# fades in orange
fade_in((255, 116, 1))
# chases with red
chase((255, 116, 1), (255, 1, 1), loop=10, count=2, delay=.1)
# fades out
fade_out((255, 116, 1))
