import pygame, sys
from src.helpers.button import Button
import random
from window_3 import Window_3
from src.helpers.drawtext import drawText
import src.helpers.attributes
from src.helpers.attributes import Attributes


pygame.init()

pygame.display.set_caption("Praying")

SCREEN = pygame.display.set_mode((640, 640))

#Define variables
textAlignLeft = 0
textAlignRight = 1
textAlignCenter = 2
textAlignBlock = 3

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("./assets/graphic/font/joystix.ttf", size)

followers = 0
font = get_font(24)
followers_text = font.render(str(followers), True, (0, 0, 0))

def Pray():
    pygame.display.set_caption('Prophet Simulator: Divine Ascension - The Quest for Faith')
    MENU_MOUSE_POS = pygame.mouse.get_pos()

    font = font=get_font(24)
    # Draw the text on the rectangle surface
    BG = pygame.transform.scale(pygame.image.load("./assets/graphic/story/cure.jpeg"), (640,640))
    SCREEN.blit(BG, (0, 0))

    msg = "Praying worked! You get +2 Belief."

    # Create a white rectangle surface
    rect_surface = pygame.Surface((150, 250))
    rect_surface.fill((255, 255, 255))

    print(Attributes['Strength'])
    print(Attributes['Intelligence'])
    print(Attributes['Charisma'])
    print(Attributes['Followers'])
    print(Attributes['Strength'])
    print(Attributes['Disciples'])

    # Create a pygame.Rect object
    rect = pygame.Rect(150, 300, 250, 200)
    SCREEN.blit(rect_surface, rect)

    textRect = pygame.Rect(150, 300, 250, 200)

    # Draw the rectangle on the screen

    pygame.draw.rect(SCREEN, (0, 0, 0), textRect, 1)
    drawTextRect = textRect.inflate(-5, -5)
    drawText(SCREEN, msg, (1, 1, 1), drawTextRect, font, textAlignBlock, True)
    pygame.display.update()

def ze():
    while True:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("./assets/graphic/menu/main_menu/rectangle.png"),(180,70)), pos=(320, 600),
                            text_input="CONTINUE", font=get_font(24), base_color="#fcea6F", hovering_color="White")

        for button in [PLAY_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Window_3()

        pygame.display.update()



if __name__ == '__main__':
    Window_2()
    ze()
	#window_0 = Window_0()
