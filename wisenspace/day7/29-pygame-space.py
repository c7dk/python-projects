import pygame

pygame.init()

screen_width = 400
screen_height = 300

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Spaceship")

# ---------------------

white = (255, 255, 255)

font = pygame.font.SysFont("monospace", 75)
pic = pygame.image.load("../dat/crazy_smile.bmp")

str = 'hello world'
score_text = font.render(str, 1, white)
keep_going = True

# ---------------------

while keep_going:
    pressed = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False

    if pressed[pygame.K_ESCAPE]:
        keep_going = False

    # --------------------

    screen.blit(score_text, (screen_width / 2 - score_text.get_width() / 2, 10))
    screen.blit(pic, (100, 100))

    pygame.display.update()
