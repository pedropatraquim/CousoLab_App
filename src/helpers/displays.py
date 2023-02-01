def display_attributes():
    # Create a new window with size (640, 640)
    attribute_window = pygame.display.set_mode((640, 640))
    attribute_window.fill((255, 255, 255))

    # Create a font object to render the text
    font = pygame.font.Font(None, 30)

    # Create a surface containing the text of each attribute
    strength_text = font.render("Strength: " + str(attributes['strength']), True, (0, 0, 0))
    charisma_text = font.render("Charisma: " + str(attributes['charisma']), True, (0, 0, 0))
    wisdom_text = font.render("Wisdom: " + str(attributes['wisdom']), True, (0, 0, 0))
    # etc. for all attributes

    # Draw the text surface on the new window
    attribute_window.blit(strength_text, (50, 50))
    attribute_window.blit(charisma_text, (50, 100))
    attribute_window.blit(wisdom_text, (50, 150))
    # etc. for all attributes

    # Update the window with the new attributes
    pygame.display.update()
