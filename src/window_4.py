import pygame, sys
from src.helpers.button import Button

pygame.init()

SCREEN = pygame.display.set_mode((640, 640))
pygame.display.set_caption("Menu")

BG = pygame.transform.scale(pygame.image.load("./assets/graphic/menu/main_menu/0aca73bf-e628-49e0-b3d3-b9b33d788bb2.jpg"), (640,640))

pygame.mixer.init()
pygame.mixer.music.load("./assets/audio/sounds/liquid-gold-glbml-21983.mp3")
pygame.mixer.music.play(-1)

Faith = 10
Wisdom = 10
Charisma= 10
Wealth= 10
Health= 10
Power= 10
Influence= 10
Reputation= 10
Knowledge= 10
Devotion= 10


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("./assets/graphic/font/joystix.ttf", size)

def Window_1():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(38).render("Prophet Simulator", True, "#db330f")
        MENU_RECT = MENU_TEXT.get_rect(center=(320, 200))

        OPTION_1_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("./assets/graphic/menu/main_menu/Play Rect.png"),(180,70)), pos=(320, 325),
                            text_input="PLAY", font=get_font(24), base_color="#fcea6F", hovering_color="White")
        OPTION_2_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("./assets/graphic/menu/main_menu/Play Rect.png"),(180,70)), pos=(320, 400),
                            text_input="OPTIONS", font=get_font(24), base_color="#fcea6F", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [OPTION_1_BUTTON, OPTION_2_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTION_1_BUTTON.checkForInput(MENU_MOUSE_POS):
                    window_2()
                if OPTION_2_BUTTON.checkForInput(MENU_MOUSE_POS):
                    window_3()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
