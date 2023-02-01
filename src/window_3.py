import pygame, sys
from src.helpers.button import Button
from game_over import Game_over

pygame.init()

SCREEN = pygame.display.set_mode((640, 640))

BG = pygame.transform.scale(pygame.image.load("./assets/graphic/game/window_1.jpg"), (640,640))

pygame.mixer.init()
pygame.mixer.music.load("./assets/audio/sounds/liquid-gold-glbml-21983.mp3")
pygame.mixer.music.play(-1)

textAlignLeft = 0
textAlignRight = 1
textAlignCenter = 2
textAlignBlock = 3

def drawText(surface, text, color, rect, font, align=textAlignLeft, aa=False, bkg=None):
    lineSpacing = -2
    spaceWidth, fontHeight = font.size(" ")[0], font.size("Tg")[1]

    listOfWords = text.split(" ")
    if bkg:
        imageList = [font.render(word, 1, color, bkg) for word in listOfWords]
        for image in imageList: image.set_colorkey(bkg)
    else:
        imageList = [font.render(word, aa, color) for word in listOfWords]

    maxLen = rect[2]
    lineLenList = [0]
    lineList = [[]]
    for image in imageList:
        width = image.get_width()
        lineLen = lineLenList[-1] + len(lineList[-1]) * spaceWidth + width
        if len(lineList[-1]) == 0 or lineLen <= maxLen:
            lineLenList[-1] += width
            lineList[-1].append(image)
        else:
            lineLenList.append(width)
            lineList.append([image])

    lineBottom = rect[1]
    lastLine = 0
    for lineLen, lineImages in zip(lineLenList, lineList):
        lineLeft = rect[0]
        if align == textAlignRight:
            lineLeft += + rect[2] - lineLen - spaceWidth * (len(lineImages)-1)
        elif align == textAlignCenter:
            lineLeft += (rect[2] - lineLen - spaceWidth * (len(lineImages)-1)) // 2
        elif align == textAlignBlock and len(lineImages) > 1:
            spaceWidth = (rect[2] - lineLen) // (len(lineImages)-1)
        if lineBottom + fontHeight > rect[1] + rect[3]:
            break
        lastLine += 1
        for i, image in enumerate(lineImages):
            x, y = lineLeft + i*spaceWidth, lineBottom
            surface.blit(image, (round(x), y))
            lineLeft += image.get_width()
        lineBottom += fontHeight + lineSpacing

    if lastLine < len(lineList):
        drawWords = sum([len(lineList[i]) for i in range(lastLine)])
        remainingText = ""
        for text in listOfWords[drawWords:]: remainingText += text + " "
        return remainingText
    return ""


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("./assets/graphic/font/joystix.ttf", size)

followers = 0
font = get_font(24)
followers_text = font.render(str(followers), True, (0, 0, 0))

def Window_3():
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
        drawText(SCREEN, msg, (1, 1, 1), drawTextRect, font, textAlignBlock, True)

        OPTION_1_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("./assets/graphic/menu/main_menu/Play Rect.png"),(1000,50)), pos=(320, 325),
                            text_input="Try to heal them with a prayer", font=get_font(16), base_color="#fcea6F", hovering_color="White")
        OPTION_2_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("./assets/graphic/menu/main_menu/Play Rect.png"),(1000,50)), pos=(320, 375),
                            text_input="Give them money to see a doctor", font=get_font(16), base_color="#fcea6F", hovering_color="White")
        OPTION_3_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("./assets/graphic/menu/main_menu/Play Rect.png"),(1000,50)), pos=(320, 425),
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
                    Game_over()
                if OPTION_2_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Game_over()
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
