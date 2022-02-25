import pygame
"""
class MyGame():
    def __init__(self):
        print('<<< init >>>')
    
    def update(self):
        print('<<< update >>>')
    
    def event(self, event):
        print('<<< event >>>')

def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    mygame = MyGame()

    keep_going = True
    clock = pygame.time.Clock()
    while keep_going:
        # -----------------------
        # Event Processing
        for event in pygame.event.get():
            mygame.event(event)

        screen.fill((0, 0, 0))

        mygame.update()

        clock.tick(60)
        pygame.display.update()

    pygmae.quit()

if __name__ == "__main__":
    main()
"""

BLACK = (0, 0, 0)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class MyGame():
    def __init__(self, scr):
        print('<<< init >>>')
        self.x = 0
        self.y = 0
        self.speedx = 5
        self.speedy = 5
        self.screen = scr
        self.keep_going = True
        self.pic = pygame.image.load('../dat/crazy_smile.bmp')

    def update(self):
        # print('<<< update >>>')
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_ESCAPE]:
            print('<<< esc pressed >>>')
            self.keep_going = False

        self.x += self.speedx
        self.y += self.speedy

        if self.x <= 0 or self.x + self.pic.get_width() >= SCREEN_WIDTH:
            self.speedx = -self.speedx
        if self.y <= 0 or self.y + self.pic.get_height() >= SCREEN_HEIGHT:
            self.speedy = -self.speedy

        self.screen.blit(self.pic, (self.x, self.y))

    def event(self, evt):
        # print('<<< event >>>')
        if evt.type == pygame.QUIT:
            self.keep_going = False

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    mygame = MyGame(screen)

    timer = pygame.time.Clock()
    while mygame.keep_going:
        # --- Event Processing
        for evt in pygame.event.get():
            mygame.event(evt)

        screen.fill(BLACK)

        mygame.update()

        timer.tick(60)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
