import pygame

import keyboard

zooName = ""
zooNameRight = 0

def draw_init_text(screen:pygame.window):
    ### TODO: Use JSON files to handle UI views rather than manual python to make the project more expandable

    global zooName, zooNameRight
    import main
    # init
    nextHeight = 0 # determines where the next part of the init UI should be rendered vertically
    borderHorizontal = 50 # How many pixels should be left empty on the left and right sides


    # Welcome to ZooManager!
    fontSize = 70
    font = pygame.font.Font("fonts/Outfit.ttf", fontSize)
    text = font.render("Welcome to ZooManager!", True, "white")

    text_rect = text.get_rect(center=(screen.width/2, fontSize)) # Where to render text
    screen.blit(text, text_rect) # Render text
    nextHeight = fontSize * 2 + 10


    ### seperating line
    pygame.draw.line(
                screen, 
                "white", 
                (borderHorizontal, fontSize * 2), 
                (screen.width - borderHorizontal, fontSize * 2), 
                1
    )


    # Lets create a zoo:
    fontSize = 50
    font = pygame.font.Font("fonts/Outfit.ttf", fontSize)
    text = font.render("Lets create a zoo:", True, "white")

    text_rect = (borderHorizontal + 10, nextHeight) # Where to render text
    screen.blit(text, text_rect) # Render text
    nextHeight += fontSize + 30


    if keyboard.pressedKeys != []: 
        if keyboard.pressedKeys[0] != "back":
            zooName += keyboard.pressedKeys[0]
        elif len(zooName) != 0:
            zooName = zooName[:-1]

    # *Zoo name:
    fontSize = 30
    font = pygame.font.Font("fonts/Outfit.ttf", fontSize)
    text = font.render("*Zoo name:", True, "white")

    text_rect = (borderHorizontal + 10, nextHeight) # Where to render text
    screen.blit(text, text_rect) # Render text
    # *Zoo names input field
    pygame.draw.rect(
                screen, 
                "#0d0c1e", 
                (text.get_rect().right + text_rect[0] + 10, nextHeight, # To the right of *Zoo name:
                 16 + zooNameRight, text.get_rect().height),
                0, 7
    )
    # Writing
    if main.frame % 60 < 30:
        pygame.draw.line(
                    screen,
                    "white",
                    (text.get_rect().right + text_rect[0] + 20 + zooNameRight, nextHeight + 9),
                    (text.get_rect().right + text_rect[0] + 20 + zooNameRight, nextHeight + fontSize - 5),
        )
    # Zoo name input text
    fontSize = 30
    font = pygame.font.Font("fonts/Outfit.ttf", fontSize)
    text = font.render(zooName, True, "white")

    text_rect = (230, nextHeight - 2) # Where to render text
    screen.blit(text, text_rect) # Render text
    zooNameRight = text.get_rect().width
    nextHeight += fontSize + 50

def draw(screen:pygame.window):
    screen.fill("#1d1c1e")
    draw_init_text(screen)