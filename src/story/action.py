import pygame, sys
from src.helpers.button import Button
from src.helpers.drawtext import drawText
from src.helpers.displays import display_attributes
from src.helpers.attributes import Attributes
from game_over import Game_over
from pray import Pray
from pray import ze
import window_3

pygame.init()

# Use the attributes
print(Attributes['Strength'])
print(Attributes['Intelligence'])
print(Attributes['Charisma'])
print(Attributes['Followers'])
print(Attributes['Strength'])
print(Attributes['Disciples'])

SCREEN = pygame.display.set_mode((640, 640))
pygame.display.set_caption("Menu")
attributes = {"miracles": 50, "reputation": 8, "dexterity": 7}

BG = pygame.transform.scale(pygame.image.load("./assets/graphic/game/window_1.jpg"), (640,640))

pygame.mixer.init()
pygame.mixer.music.load("./assets/audio/sounds/liquid-gold-glbml-21983.mp3")
pygame.mixer.music.play(-1)

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("./assets/graphic/font/joystix.ttf", size)

followers = 0
font = get_font(24)
followers_text = font.render(str(followers), True, (0, 0, 0))

def Window_1():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        font = font=get_font(24)
        # Draw the text on the rectangle surface


        msg = "You are approached by a sick person asking for your help. Do you:"

        # Create a white rectangle surface
        rect_surface = pygame.Surface((400, 130))
        rect_surface.fill((255, 255, 255))

        # Create a pygame.Rect object
        rect = pygame.Rect(150, 50, 400, 130)
        SCREEN.blit(rect_surface, rect)

        textRect = pygame.Rect(150, 50, 400, 130)

        # Draw the rectangle on the screen

        pygame.draw.rect(SCREEN, (0, 0, 0), textRect, 1)
        drawTextRect = textRect.inflate(-5, -5)
        drawText(SCREEN, msg, (1, 1, 1), drawTextRect, font, 0, True)

        OPTION_1_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("./assets/graphic/menu/main_menu/rectangle.png"),(1000,50)), pos=(320, 325),
                            text_input="Try to heal them with a prayer", font=get_font(16), base_color="#fcea6F", hovering_color="White")
        OPTION_2_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("./assets/graphic/menu/main_menu/rectangle.png"),(1000,50)), pos=(320, 375),
                            text_input="Give them money to go see a doctor", font=get_font(16), base_color="#fcea6F", hovering_color="White")
        OPTION_3_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("./assets/graphic/menu/main_menu/rectangle.png"),(1000,50)), pos=(320, 425),
                            text_input="Ignore them and continue on your journey", font=get_font(16), base_color="#fcea6F", hovering_color="White")

        for button in [OPTION_1_BUTTON, OPTION_2_BUTTON, OPTION_3_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTION_1_BUTTON.checkForInput(MENU_MOUSE_POS):
                    if Attributes["Charisma"] < 5:
                        Attributes["Charisma"] -= 2
                    else:
                        Attributes["Followers"] += 1
                        Attributes["Charisma"] += 1
                    Pray()
                    ze()
                if OPTION_2_BUTTON.checkForInput(MENU_MOUSE_POS):
                    window_3()
                if OPTION_3_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Game_over()
            if event.type == pygame.KEYDOWN and event.unicode == 'f':
                text_surface = get_font(18).render(str(followers), True, (255, 255, 255))
                text_rect = text_surface.get_rect()
                text_rect.center = (100, 600)
                SCREEN.blit(text_surface, text_rect)
                pygame.display.update()
                pygame.time.wait(750)
            if event.type == pygame.KEYDOWN and event.unicode == 'a':
                text_surface = get_font(18).render(str(attributes), True, (255, 255, 255))
                text_rect = text_surface.get_rect()
                text_rect.center = (100, 600)
                SCREEN.blit(text_surface, text_rect)
                pygame.display.update()
                pygame.time.wait(750)

        pygame.display.update()
