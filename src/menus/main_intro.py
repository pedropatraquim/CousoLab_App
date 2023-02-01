import pygame, sys
import random
from ..helpers.button import Button
from ..main.game import Game

pygame.init()

pygame.display.set_caption("Intro")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("./assets/graphic/font/joystix.ttf", size)

SCREEN = pygame.display.set_mode((640, 640))

def Main_intro():
	pygame.mixer.init()
	pygame.display.set_caption('Wanax')
	pygame.mixer.music.load("./assets/audio/music/let-the-mystery-unfold-122118.mp3")
	pygame.mixer.music.play(-1)

	size = (640, 640)
	screen = pygame.display.set_mode(size)
	clock = pygame.time.Clock()

	# Create a font object
	font = font=get_font(16)

	# Create a starting position for the text
	x, y = 10, 30

	# Initializing surface
	surface = pygame.display.set_mode((640, 640))

	# Initializing RGB Color
	color = ("#cc4b33")

	# Changing surface color
	surface.fill(color)
	pygame.display.flip()

	# Set the text to be displayed
	text = "The land of Pylos is in a state of unrest. The city-state is facing challenges from within and without, as neighboring kingdoms seek to expand their power and influence. At the same time, the crops are failing, the nobles are plotting, and whispers of rebellion can be heard in the streets. The people are calling out for a strong leader, someone who can bring stability and prosperity back to the kingdom. That leader is you. You are the Wanax, the ruler of Pylos, the most #powerful man in the land, inheriting the mantle from your well-respected late father. His recent death has left many questions unanswered and rumors of foul play abound. It is up to you to discover the truth, solidify your position as Wanax, and ensure the prosperity and security of Pylos. You must navigate the complex political landscape of the Mycenaean world, balancing the demands of the people, the nobles, the military, and the merchants. Will you be able to restore order, or will #Pylos fall into chaos? The choice is yours. The fate of the kingdom rests in your hands."

	# Set the  dummytext to be displayed
	#text = "The"

	# Set the background color of the text
	background_color = ("#f6efd6")

	# Create a surface to render the text on
	text_surface = font.render(text[0], True, background_color, background_color)

	# Blit the text to the screen one character at a time
	for i in range(0, len(text)):
	    if text[i] == " " and x + text_surface.get_width() > size[0] - 100:
	        x = 50 + random.randint(-20,10)
	        y += font.get_height()
	    text_surface = font.render(text[i], True, "#f6efd6", "#cc4b33")
	    text_rect = text_surface.get_rect()
	    text_rect.x = x + text_rect.width
	    text_rect.x, text_rect.y = x, y
	    screen.blit(text_surface, text_rect)
	    pygame.display.update()
	    if text[i] == ",":
	        pygame.time.wait(90+random.randint(-30,40))
	    elif text[i] == ".":
	        pygame.time.wait(75+random.randint(-50,20))
	    elif text[i] == " ":
	        pygame.time.wait(10+random.randint(-0,0))
	    else:
	        pygame.time.wait(20+random.randint(-0,0))
	    x += text_rect.width

	MENU_MOUSE_POS = pygame.mouse.get_pos()

	PLAY_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("./assets/graphic/menu/main_menu/rectangle.png"),(180,70)), pos=(320, 600),
                               text_input="CONTINUE", font=get_font(24), base_color="#fcea6F", hovering_color="White")

	for button in [PLAY_BUTTON]:
		button.changeColor(MENU_MOUSE_POS)
		button.update(SCREEN)

	pygame.display.update()


def main_intro_button():
	display_surface = pygame.display.get_surface()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				game = Game(display_surface)
				game.run()

		pygame.display.update()
