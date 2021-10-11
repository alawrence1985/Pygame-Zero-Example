# Tutorial: https://pygame-zero.readthedocs.io/en/stable/introduction.html

alien = Actor('alien')
alien.pos = 100, 56

WIDTH = 500
HEIGHT = alien.height + 20

def draw():
    screen.clear()
    alien.draw()