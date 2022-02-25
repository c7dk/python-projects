import pygame

pygame.init()
screen = pygame.display.set_mode([800, 600])
keep_going = True
pic = pygame.image.load("../dat/crazy_smile.bmp")
colorkey = pic.get_at((0, 0))
pic.set_colorkey(colorkey)
picx = 0
picy = 0
GREEN = (0, 255, 0)
timer = pygame.time.Clock()
speedx = 10
speedy = 10

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
    
    picx += speedx
    picy += speedy

    if picx <= 0 or picx + pic.get_width() >= 800:
        speedx = -speedx
    if picy <= 0 or picy + pic.get_height() >= 600:
        speedy = -speedy

    screen.fill(GREEN)
    screen.blit(pic, (picx, picy))
    pygame.display.update()
    timer.tick(60)

pygame.quit()