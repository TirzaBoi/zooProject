import pygame

import draw
import keyboard

# Variables
frame = 0

# classes
class Zoo:
    def __init__(self, name:str, founded:str, address:str):
        self.name = name,
        self.founded = founded,
        self.address = address

# pygame setup
pygame.init()
screen = pygame.display.set_mode((960, 720), pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True

pygame.key.set_repeat(550, 50)

def keep_screen_minimum_resolution(w=960, h=720):
    """Ensures that the window is kept at the minimum resolution or bigger when resizing it"""
    global screen
    if screen.width < w: screen = pygame.display.set_mode((w, screen.height), pygame.RESIZABLE)
    if screen.height < h: screen = pygame.display.set_mode((screen.width,h), pygame.RESIZABLE)

while running:
    keyboard.getInput(pygame.event.get())

    draw.draw(screen)
    keep_screen_minimum_resolution()

    pygame.display.flip()
    clock.tick(60)  # 60 fps is enough
    frame += 1

pygame.quit()