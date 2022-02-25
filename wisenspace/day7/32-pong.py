import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# color globals
red = (255, 0, 0)
orange = (255, 127, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
violet = (127, 0, 255)
brown = (102, 51, 0)
black = (0, 0, 0)
white = (255, 255, 255)

class Paddle:
    def __init__(self, name, x, y, screen, upkey, downkey):
        print('paddle init')
        self.screen = screen
        self.name = name
        self.x = x
        self.y = y
        self.w = 25
        self.h = 100
        self.upkey = upkey
        self.downkey = downkey
        self.score = 0

    
    def update(self, pressed):
        print('paddle update')
        if pressed[self.upkey] and self.y > 0:
            self.y -= 5
        elif pressed[self.downkey] and self.y < SCREEN_HEIGHT - 100:
            self.y += 5

        pygame.draw.rect(self.screen, white, (self.x, self.y, self.w, self.h), 0)

class Ball:
    def __init__(self, screen, name, x, y):
        print('ball init')
        self.screen = screen
        self.x = x
        self.y = y
        self.pic = pygame.image.load('../dat/crazy_smile.bmp')

    
    def update(self):
        print('ball update')
        self.screen.blit(self.pic, (self.x, self.y))
    

class MyGame():
    def __init__(self, screen):
        print('<<< setup >>>')
        self.keep_going = True
        self.screen = screen

        self.font = pygame.font.SysFont("monospace", 75)
        self.ctry = int(SCREEN_HEIGHT / 2) - 50

        self.ball = Ball(screen, 'ball', int(SCREEN_WIDTH / 2) - 50, self.ctry)
        self.leftpaddle = Paddle('left', 20, self.ctry, screen, pygame.K_w, pygame.K_s)
        self.rightpaddle = Paddle('Right', SCREEN_WIDTH - 20 - 25, self.ctry, screen, pygame.K_UP, pygame.K_DOWN)

    def update(self):
         # print('<<< update >>>')
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_ESCAPE]:
            print('<<< esc pressed >>>')
            self.keep_going = False

        score_text = self.font.render(str(self.leftpaddle.score) + "  " + str(self.rightpaddle.score), 1, violet)

        net = pygame.draw.line(self.screen, yellow, (SCREEN_WIDTH/2, 5), (SCREEN_WIDTH/2, SCREEN_HEIGHT - 5))
        self.screen.blit(score_text, (SCREEN_WIDTH / 2 - score_text.get_width() / 2, 10))


        self.leftpaddle.update(pressed)
        self.rightpaddle.update(pressed)

        self.ball.update()

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
        for event in pygame.event.get():
            mygame.event(event)

        screen.fill((0, 0, 0))

        mygame.update()

        timer.tick(60)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()