import pygame
import sys
from pytmx.util_pygame import load_pygame
import random
import pygame.mixer
import sys
import math
import random
import pygame.font
import main

class Intro:
	def __init__(self):
		# general setup
		pygame.init()

		WIDTH = 1280
		HEIGHT = 720
		self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
		pygame.display.set_caption('Dæsolåte')

		size = (1280, 720)
		screen = pygame.display.set_mode(size)
		clock = pygame.time.Clock()

		# Create a font object
		font = pygame.font.Font("./assets/graphics/font/twoweekendssans_regular.otf", 28)

		# Create a starting position for the text
		x, y = 50, 175

		# Set the text to be displayed
		text = "Cuando desperté, me encontré en un lugar desconocido, desorientado y confundido. El suelo debajo de mí era rocoso y el aire estaba seco, y mi visión era borrosa. Miré a mi alrededor, pero todo lo que pude ver fue tierra estéril que se extendía hasta donde alcanzaba la vista. Sentí que me invadía una sensación de temor y confusión cuando me di cuenta de que estaba completamente sola, varada en un planeta desierto. No podía entender por qué mi visión estaba borrosa y la luz parecía tenue. Traté de parpadear para alejar la niebla de mis ojos, pero no se aclaraba. No fue hasta que noté el extraño color naranja del cielo y el sol rojo intenso que entendí que no eran mis ojos los que estaban nublados, sino el sol el que estaba débil. Las rocas y la arena eran de un gris oscuro, y mi mente se aceleró mientras trataba de comprender cómo era posible."

		# Set the background color of the text
		background_color = (0, 0, 0)

		# Create a surface to render the text on
		text_surface = font.render(text[0], True, (255, 255, 255), background_color)

		# Load the MP3 file and start playing it
		# COMMENT JAMES: Heartbeat maybe?
		pygame.mixer.init()
		pygame.mixer.music.load("./assets/audio/sounds/Hard-Breathing-Medium-Pace-www.fesliyanstudios.com.mp3")
		pygame.mixer.music.play(-1)

		# Blit the text to the screen one character at a time
		for i in range(0, len(text)):
		    if text[i] == " " and x + text_surface.get_width() > size[0] - 100:
		        x = 50 + random.randint(-20,10)
		        y += font.get_height()
		    text_surface = font.render(text[i], True, (255, 255, 255), background_color)
		    text_rect = text_surface.get_rect()
		    text_rect.x = x + text_rect.width
		    text_rect.x, text_rect.y = x, y
		    screen.blit(text_surface, text_rect)
		    pygame.display.update()
		    if text[i] == ",":
		        pygame.time.wait(90+random.randint(-30,40))
		    elif text[i] == ".":
		        pygame.time.wait(75+random.randint(-50,20))
		    else:
		        pygame.time.wait(50+random.randint(-10,10))
		    x += text_rect.width

		pygame.display.update()

		pygame.time.wait(10)

		# play mp3
		pygame.mixer.music.load("./assets/audio/sounds/Hard-Breathing-Medium-Pace-www.fesliyanstudios.com.FASTER.mp3")
		pygame.mixer.music.play(-1)

		# Fade out the text
		for i in range(255, 0, -5):
		    text_color = (255, 255, 255, i)
		    text_surface.fill((0,0,0,0))
		    text_surface = font.render(text, True, text_color)
		    screen.blit(text_surface, text_rect)
		    pygame.display.update()

		    #Fade in the image
		    alpha = i * 2 #adjust the alpha value of the image
		    # Load the image
		    image = pygame.image.load("./assets/graphics/menus/main_menu/thursday.jpg")
		    # Get the rect of the image
		    image_rect = image.get_rect()
		    image.set_alpha(alpha)
		    # Position the rect of the image
		    image_rect.x = (size[0] - image_rect.width) // 2
		    image_rect.y = size[1] - image_rect.height - 100
		    screen.blit(image, image_rect)
		    pygame.display.update()
		    pygame.time.wait(50)

		# play mp3
		pygame.mixer.music.load("./assets/audio/music/epic-magic-13965.mp3")
		pygame.mixer.music.play(-1)

		    # Fade out the text
		for i in range(255, 0, -5):
		    text_color = (255, 255, 255, i)
		    text_surface.fill((0,0,0,0))
		    text_surface = font.render(text, True, text_color)
		    screen.blit(text_surface, text_rect)
		    pygame.display.update()

		    #Fade in the image
		    alpha = i * 2 #adjust the alpha value of the image
		    # Load the image
		    image = pygame.image.load("./assets/graphics/menus/main_menu/thursday.jpg")
		    # Get the rect of the image
		    image_rect = image.get_rect()
		    image.set_alpha(alpha)
		    # Position the rect of the image
		    image_rect.x = ((size[0] - image_rect.width) // 2) + 10
		    image_rect.y = size[1] - image_rect.height - 40
		    screen.blit(image, image_rect)
		    pygame.display.update()
		    pygame.time.wait(10)

		    # Create a font object
		    screen.fill((255, 255, 255))
		    font = pygame.font.Font("./assets/graphics/font/MontserratAlt1-Bold.otf", 50)
		    text_surface = font.render("Dæsolåte", True, (0, 0, 0))
		    text_rect = text_surface.get_rect()
		    text_rect.center = (size[0] // 2, size[1] // 2)
		    screen.blit(text_surface, text_rect)
		    pygame.display.update()

		pygame.time.wait(5000)
		pygame.display.update()
		main.Game()


	def run(self):
			self.level.run()
			pygame.display.update()
			self.clock.tick(FPS)

if __name__ == '__main__':
	intro = Intro()
	intro.run()
