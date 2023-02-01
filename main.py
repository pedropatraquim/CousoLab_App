import pygame, sys
from src.helpers.button import Button

pygame.init()

SCREEN = pygame.display.set_mode((640, 640))
pygame.display.set_caption("Main Menu")

BG = pygame.transform.scale(pygame.image.load("./assets/graphic/menu/main_menu/Background.png"), (640,640))

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("./assets/graphic/font/twoweekendssans_regular.otf", size)

def fasta():
    while True:
        fasta_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")

        fasta_TEXT = get_font(24).render("FASTA Handling Menu: soon!", True, "White")
        fasta_RECT = fasta_TEXT.get_rect(center=(320, 320))
        SCREEN.blit(fasta_TEXT, fasta_RECT)

        fasta_BACK = Button(image=None, pos=(320, 500),
                            text_input="BACK", font=get_font(22), base_color="White", hovering_color="Green")

        fasta_BACK.changeColor(fasta_MOUSE_POS)
        fasta_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if fasta_BACK.checkForInput(fasta_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def databases():
    while True:
        databases_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        databases_TEXT = get_font(24).render("Databases Menu: soon!", True, "Black")
        databases_RECT = databases_TEXT.get_rect(center=(320, 320))
        SCREEN.blit(databases_TEXT, databases_RECT)

        databases_BACK = Button(image=None, pos=(320, 400),
                            text_input="BACK", font=get_font(22), base_color="Black", hovering_color="Green")

        databases_BACK.changeColor(databases_MOUSE_POS)
        databases_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if databases_BACK.checkForInput(databases_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("./assets/graphic/menu/main_menu/pattern_back_3.png"),(600,70)), pos=(322, 50),
                            text_input="Couso Lab App", font=pygame.font.Font("./assets/graphic/font/title/Aegis-1BKg.ttf", 56), base_color="#000000", hovering_color="White")
        FASTA_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("./assets/graphic/menu/main_menu/rectangle.png"),(260,70)), pos=(320, 300),
                            text_input="FASTA Handling", font=get_font(26), base_color="#000000", hovering_color="White")
        DATABASES_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("./assets/graphic/menu/main_menu/rectangle.png"),(260,70)), pos=(320, 375),
                            text_input="Databases", font=get_font(26), base_color="#000000", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("./assets/graphic/menu/main_menu/rectangle.png"),(260,70)), pos=(320, 450),
                            text_input="QUIT", font=get_font(26), base_color="#000000", hovering_color="White")

        for button in [FASTA_BUTTON, DATABASES_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if FASTA_BUTTON.checkForInput(MENU_MOUSE_POS):
                    fasta()
                if DATABASES_BUTTON.checkForInput(MENU_MOUSE_POS):
                    databases()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
