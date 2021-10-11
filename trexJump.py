# Tutorial: https://pygame-zero.readthedocs.io/en/stable/introduction.html

WIDTH = 400
HEIGHT = 250

trex = Actor('trex')
trex.pos = trex.width*2, HEIGHT-trex.height//2
pumpkin = Actor('pumpkin')
pumpkin.pos = WIDTH-pumpkin.width//2, HEIGHT-pumpkin.height//2

score = 0

def draw():
    screen.clear()
    screen.fill("black")
    trex.draw()
    pumpkin.draw()

def update():
  move_pumpkin()

def move_pumpkin():
  global score
  pumpkin.x -= 2

  if pumpkin.x <= 0:
    score += 1
    pumpkin.x = WIDTH-pumpkin.width//2
