import pygame

pressedKeys = []

def getInput(events:pygame.event):
    """Handles keyboard and misc input into variables"""
    import main
    global pressedKeys
    pressedKeys = []
    for event in events:
        if event.type == pygame.QUIT:
            main.running = False
        if event.type == pygame.KEYDOWN: # Can i make this be held (like hold for 1 second and then this runs automatically also?)
            if event.unicode == "\x08" or event.unicode == "\x7f":
                pressedKeys = ["back"]
                return
            pressedKeys.append(event.unicode)
            #print(pressedKeys)