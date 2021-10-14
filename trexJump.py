import math

WIDTH = 400
HEIGHT = 250

trex = Actor('trex')
trex.pos = trex.width*2, HEIGHT-trex.height//2
pumpkin = Actor('pumpkin')
pumpkin.pos = WIDTH-pumpkin.width//2, HEIGHT-pumpkin.height//2

score = 0
GROUND = HEIGHT-trex.height//2
RADIAN = math.pi/64
nextRadian = 1
isJumping = False
game_over = False


def draw():
    screen.clear()
    screen.blit("graveyard.png", (0,0))
    
    if not game_over:
      trex.draw()
      pumpkin.draw()
      screen.draw.text("SCORE: " + str(score), (5, 10), color="orange")
    else:
      screen.draw.text("GAME OVER :(((((", (125, 100), color="orange")
      reset()

def update():
  update_trex()
  update_pumpkin()

def update_trex():
  global nextRadian, isJumping

  if keyboard.up and not isJumping:
    isJumping = True
    jump()
  elif trex.y < GROUND and isJumping:
    jump()
  else:
    isJumping = False
    nextRadian = 1

def update_pumpkin():
  global score, game_over

  pumpkin.x -= 2

  if pumpkin.x <= 0:
    score += 1
    pumpkin.x = WIDTH-pumpkin.width//2
  
  if pumpkin.colliderect(trex):
    game_over = True

def reset():
  global score, nextRadian, isJumping, game_over
  if keyboard.space:
    trex.pos = trex.width*2, HEIGHT-trex.height//2
    pumpkin.pos = WIDTH-pumpkin.width//2, HEIGHT-pumpkin.height//2
    score = 0
    nextRadian = 1
    isJumping = False
    game_over = False

def jump():
  global nextRadian
  trex.y = -90*math.sin(nextRadian*RADIAN) + GROUND
  nextRadian = nextRadian + 1
