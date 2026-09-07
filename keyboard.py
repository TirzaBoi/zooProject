import pygame

pressedKeys = []

def getInput(events:pygame.event):
    import main
    global pressedKeys
    pressedKeys = []
    for event in events:
        if event.type == pygame.QUIT:
            main.running = False
        if event.type == pygame.KEYDOWN:
            if event.unicode == "\x08" or event.unicode == "\x7f":
                pressedKeys = ["back"]
                return
            pressedKeys.append(event.unicode)
            #print(pressedKeys)