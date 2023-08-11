"""
import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE

from pygame_ui_controls import UI, Button, Slider, CheckBox, Text, ImageButton
# https://github.com/ArthurLeFloch/PygameUI/blob/master/examples/everything.py

if __name__ == "__main__":
    pygame.init()

    UI.init()
    Button.CONFIRM_TEXT = "Confirm ?"

    WIDTH, HEIGHT = 600, 400
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("UI elements Tests")
    """

# Example file showing a basic pygame "game loop"
import pygame
from time import sleep
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

clock = pygame.time.Clock()
running = True


class Rect: # saving data of rects which was drawn
    def __init__(self, p1_, p2_, p3_, p4_):
        self.p1 = p1_
        self.p2 = p2_
        self.p3 = p3_
        self.p4 = p4_

    def draw(self):
        pygame.draw.rect(screen, white, pygame.Rect(self.p1, self.p2, self.p3, self.p4))

rentList = list()
first_click = True

while running:
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    mx, my = pygame.mouse.get_pos()
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    if first_click and pygame.mouse.get_pressed(3)[0]:
        sleep(0.2)
        xpos, ypos = mx, my
        first_click = False

    elif not first_click:
        if xpos > mx and ypos > my:
            p1, p2, p3, p4 = mx, my, (xpos - mx),  (ypos - my)
            pygame.draw.rect(screen, white, pygame.Rect(p1, p2, p3, p4))

        elif mx > xpos and ypos > my:
            p1, p2, p3, p4 = xpos, my, (mx - xpos), (ypos - my)
            pygame.draw.rect(screen, white, pygame.Rect(p1, p2, p3, p4))

        elif mx > xpos and my > ypos:
            p1, p2, p3, p4 = xpos, ypos, (mx - xpos), (my - ypos)
            pygame.draw.rect(screen, white, pygame.Rect(p1, p2, p3, p4))

        elif xpos > mx and my > ypos:
            p1, p2, p3, p4 = mx, ypos, (xpos - mx), (my - ypos)
            pygame.draw.rect(screen, white, pygame.Rect(p1, p2, p3, p4))


        if first_click == False and pygame.mouse.get_pressed(3)[0]:
            sleep(0.2)
            first_click = True
            sizeX, sizeY = mx, my
            rent = Rect(p1, p2, p3, p4)
            # rent = Rect(xpos, ypos, mx, my, sizeX, sizeY)
            rentList.append(rent)

    for eachRent in rentList:
        eachRent.draw()

    print(len(rentList))
    # print(f"mx = {mx}, my = {my}")
    print(pygame.mouse.get_pressed(3)[0])
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
