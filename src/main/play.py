import pygame
import sys
from pytmx.util_pygame import load_pygame
import random
import pygame.mixer
import sys
import math
import random
import pygame.font
from src.helpers.settings import *
#from level import Level

class Game:
	def __init__(self):

		WIDTH = 1280
		HEIGHT = 720
		self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
		pygame.display.set_caption('Dæsolåte')

		size = (1280, 720)
		screen = pygame.display.set_mode(size)
		clock = pygame.time.Clock()

		# general setup
		# Load the tmx map
		tmx_data = load_pygame('/Users/pedropatraquim/Thursday_or_The_Desolate_Planet/dev/maps/108.tmx')

		# Create a new Surface to render the map on
		map_image = pygame.Surface((tmx_data.width * tmx_data.tilewidth, tmx_data.height * tmx_data.tileheight))

		# Create a map rect object and set its position
		map_rect = map_image.get_rect()

		# Iterate over all layers in the map
		for layer in tmx_data.visible_layers:
		    # Iterate over all tiles in the layer
		    for x, y, image in layer.tiles():
		        # Blit the tile image onto the map Surface
		        map_image.blit(image, (x * tmx_data.tilewidth, y * tmx_data.tileheight))

		# Set the caption for the game window
		pygame.display.set_caption("The Desolate Planet")

		# Create a player rect object and set its position
		player_rect = pygame.Rect(10, 10, 20, 20)
		player_rect.x = map_image.get_width() - player_rect.width
		player_rect.y = map_image.get_height() - player_rect.height

		player_image = pygame.image.load("/Users/pedropatraquim/Thursday_or_The_Desolate_Planet/assets/art/ze.png")

		###
		# Load the images for the sprite
		up_frames = [pygame.image.load("/Users/pedropatraquim/Thursday_or_The_Desolate_Planet/assets/art/player_sprites/ze/up.png"), pygame.image.load("/Users/pedropatraquim/Thursday_or_The_Desolate_Planet/assets/art/player_sprites/ze/up_stop.png"), pygame.image.load("/Users/pedropatraquim/Thursday_or_The_Desolate_Planet/assets/art/player_sprites/ze/up_walk.png")]
		down_frames = [pygame.image.load("/Users/pedropatraquim/Thursday_or_The_Desolate_Planet/assets/art/player_sprites/ze/down.png"), pygame.image.load("/Users/pedropatraquim/Thursday_or_The_Desolate_Planet/assets/art/player_sprites/ze/down_stop.png"), pygame.image.load("/Users/pedropatraquim/Thursday_or_The_Desolate_Planet/assets/art/player_sprites/ze/down_walk.png")]
		left_frames = [pygame.image.load("/Users/pedropatraquim/Thursday_or_The_Desolate_Planet/assets/art/player_sprites/ze/left.png"), pygame.image.load("/Users/pedropatraquim/Thursday_or_The_Desolate_Planet/assets/art/player_sprites/ze/left_stop.png"), pygame.image.load("/Users/pedropatraquim/Thursday_or_The_Desolate_Planet/assets/art/player_sprites/ze/left_walk.png")]
		right_frames = [pygame.image.load("/Users/pedropatraquim/Thursday_or_The_Desolate_Planet/assets/art/player_sprites/ze/right.png"), pygame.image.load("/Users/pedropatraquim/Thursday_or_The_Desolate_Planet/assets/art/player_sprites/ze/right_stop.png"), pygame.image.load("/Users/pedropatraquim/Thursday_or_The_Desolate_Planet/assets/art/player_sprites/ze/right_walk.png")]
		#
		# Scale down the images in the up_frames list
		for i in range(len(up_frames)):
		    up_frames[i] = pygame.transform.smoothscale(up_frames[i], (26, 42))

		# Scale down the images in the down_frames list
		for i in range(len(down_frames)):
		    down_frames[i] = pygame.transform.smoothscale(down_frames[i], (26, 42))

		# Scale down the images in the left_frames list
		for i in range(len(left_frames)):
		    left_frames[i] = pygame.transform.smoothscale(left_frames[i], (26, 42))

		# Scale down the images in the right_frames list
		for i in range(len(right_frames)):
		    right_frames[i] = pygame.transform.smoothscale(right_frames[i], (26, 42))

		# Create a variable to keep track of the current frame
		current_frame = 0

		# Create a variable to keep track of the zoom level
		zoom = 1
		zoom_on = False

		# Nudge the initial position of the player a little bit upwards and leftwards
		player_rect.x -= 10
		player_rect.y -= 10

	def run(self):
		running = True
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False

			# Clear the screen
			screen.fill((0, 0, 0))

			# Keep the player within the bounds of the map
			if player_rect.x < 0:
				player_rect.x = 0
			if player_rect.x + player_rect.width > map_image.get_width():
				player_rect.x = map_image.get_width() - player_rect.width
			if player_rect.y < 0:
				player_rect.y = 0
			if player_rect.y + player_rect.width > map_image.get_width():
				player_rect.y = map_image.get_height() - player_rect.height

			# Calculate the offset for the map so that it is centered on the player
			map_offset_x = -player_rect.x + screen.get_height()/2 + 100
			map_offset_y = -player_rect.y + screen.get_height()/2 + 100
			#pygame.draw.rect(screen, (255,255,255), (player_rect.x+player_rect.width//2 + map_offset_x, player_rect.y+player_rect.height//2 + map_offset_y, 32, 32))

			# Make sure the map doesn't go out of bounds
			if map_offset_x > 0:
				map_offset_x = 0
			if map_offset_x < -map_image.get_width() + screen.get_width():
				map_offset_x = -map_image.get_width() + screen.get_width()
			if map_offset_y > 0:
				map_offset_y = 0
			if map_offset_y < -map_image.get_height() + screen.get_height():
				map_offset_y = -map_image.get_height() + screen.get_height()

			# Handle player input
			keys = pygame.key.get_pressed()
			if keys[pygame.K_z]:
				zoom_on = not zoom_on
			if zoom_on:
				zoom = 2
			else:
				zoom = 1
				screen = pygame.display.set_mode((int(screen.get_width() * zoom), int(screen.get_height() * zoom)))
				pygame.display.set_caption("Zoom level: {}".format(zoom))
			if keys[pygame.K_UP]:
				player_rect.y -= 1
			if keys[pygame.K_DOWN]:
				player_rect.y += 1
			if keys[pygame.K_RIGHT]:
				player_rect.x += 1
			if keys[pygame.K_LEFT]:
				player_rect.x -= 1
			if map_rect.x < 0:
				map_rect.x = 0
			if map_rect.y < 0:
				map_rect.y = 0

			# Determine which direction the player is moving
			if keys[pygame.K_UP]:
				player_image = up_frames[current_frame]
			elif keys[pygame.K_DOWN]:
				player_image = down_frames[current_frame]
			elif keys[pygame.K_LEFT]:
				player_image = left_frames[current_frame]
			elif keys[pygame.K_RIGHT]:
				player_image = right_frames[current_frame]

			# Increment the current frame
			current_frame += 1
			# If the current frame is greater than the number of frames, set it back to 0
			if current_frame >= len(up_frames):
				current_frame = 0

			# Render the map on the screen, centered on the player
			screen.blit(map_image, (map_offset_x, map_offset_y))
			screen.blit(player_image,(player_rect.x+player_rect.width//2 + map_offset_x, player_rect.y+player_rect.height//2 + map_offset_y))
			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_m:
						self.level.toggle_menu()

			#self.screen.fill(WATER_COLOR)
			self.level.run()
			pygame.display.update()
			self.clock.tick(60)

if __name__ == '__main__':
	game = Game()
	game.run()
