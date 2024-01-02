import pygame
import sys
from settings import Settings

class AlienInvasion:
    """Overall class to manage game and behaviors"""
    
    def __INIT__(self):
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.bg_color = self.settings.bg_color
        pygame.display.set_caption(self.settings.screen_caption)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            #Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                
                #Redraw the screen during each pass through the loop
                self.screen.fill(self.bg_color)

                #Make most recent drawn screen visible
                pygame.display.flip()
                self.clock.tick(60)
    
if __name__ == '__main__':
    #Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()