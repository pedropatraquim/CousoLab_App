import pygame, sys
import subprocess
from src.button import Button

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

        pygame.display.set_caption("FASTA Handling")


        #fasta_TEXT = get_font(24).render("FASTA Handling Menu: soon!", True, "White")
        #fasta_RECT = fasta_TEXT.get_rect(center=(320, 320))
        #SCREEN.blit(fasta_TEXT, fasta_RECT)

        LOAD_FASTA = Button(image=pygame.transform.scale(pygame.image.load("./assets/graphic/menu/main_menu/rectangle.png"),(260,70)), pos=(320, 300),
							text_input="Load FASTA", font=get_font(26), base_color="White", hovering_color="Red")
        FASTA_OPERATIONS = Button(image=pygame.transform.scale(pygame.image.load("./assets/graphic/menu/main_menu/rectangle.png"),(300,70)), pos=(320, 375),
							text_input="FASTA Operations", font=get_font(26), base_color="White", hovering_color="Red")

        fasta_BACK = Button(image=None, pos=(320, 500),
                            text_input="BACK", font=get_font(22), base_color="White", hovering_color="Green")

        for button in [LOAD_FASTA, FASTA_OPERATIONS, fasta_BACK]:
            button.changeColor(fasta_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if fasta_BACK.checkForInput(fasta_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def genor():
    while True:
        genor_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        genor_TEXT = get_font(24).render("GENOR Menu: soon!", True, "Black")
        genor_RECT = genor_TEXT.get_rect(center=(320, 320))
        SCREEN.blit(genor_TEXT, genor_RECT)

        genor_BACK = Button(image=None, pos=(320, 400),
                            text_input="BACK", font=get_font(22), base_color="Black", hovering_color="Green")

        genor_BACK.changeColor(genor_MOUSE_POS)
        genor_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if genor_BACK.checkForInput(genor_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def venn():
    while True:
        venn_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        venn_TEXT = get_font(24).render("VENN Menu: soon!", True, "Black")
        venn_RECT = venn_TEXT.get_rect(center=(320, 320))
        SCREEN.blit(venn_TEXT, venn_RECT)

        venn_BACK = Button(image=None, pos=(320, 400),
                            text_input="BACK", font=get_font(22), base_color="Black", hovering_color="Green")

        venn_BACK.changeColor(venn_MOUSE_POS)
        venn_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if venn_BACK.checkForInput(venn_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("./assets/graphic/menu/main_menu/pattern_back_3.png"),(600,70)), pos=(322, 50),
                            text_input="Couso Lab App", font=pygame.font.Font("./assets/graphic/font/title/Aegis-1BKg.ttf", 56), base_color="#000000", hovering_color="White")
        VENN_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("./assets/graphic/menu/main_menu/rectangle.png"),(260,70)), pos=(320, 245),
                            text_input="Make Venn", font=get_font(26), base_color="#000000", hovering_color="White")
        FASTA_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("./assets/graphic/menu/main_menu/rectangle.png"),(260,70)), pos=(320, 320),
                            text_input="FASTA Handling", font=get_font(26), base_color="#000000", hovering_color="White")
        DATABASES_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("./assets/graphic/menu/main_menu/rectangle.png"),(260,70)), pos=(320, 395),
                            text_input="Databases", font=get_font(26), base_color="#000000", hovering_color="White")
        GENOR_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("./assets/graphic/menu/main_menu/rectangle.png"),(260,70)), pos=(320, 470),
                            text_input="GENOR", font=get_font(26), base_color="#000000", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("./assets/graphic/menu/main_menu/rectangle.png"),(260,70)), pos=(320, 545),
                            text_input="QUIT", font=get_font(26), base_color="#000000", hovering_color="White")

        for button in [VENN_BUTTON, FASTA_BUTTON, DATABASES_BUTTON, GENOR_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if VENN_BUTTON.checkForInput(MENU_MOUSE_POS):
                	subprocess.call(["streamlit", "run", "./src/venn.py"])
                if FASTA_BUTTON.checkForInput(MENU_MOUSE_POS):
                    fasta()
                if DATABASES_BUTTON.checkForInput(MENU_MOUSE_POS):
                	subprocess.call(["streamlit", "run", "./src/databases.py"])
                if GENOR_BUTTON.checkForInput(MENU_MOUSE_POS):
                    genor()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
