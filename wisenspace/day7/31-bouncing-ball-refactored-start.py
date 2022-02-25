import pygame

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