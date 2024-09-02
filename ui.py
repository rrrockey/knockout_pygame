import pygame, settings, game_objects

class button:
    def __init__(self, text, x, y, width, height):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def display(self):
        pygame.draw.rect(settings.screen, settings.button_blue, pygame.Rect(self.x, self.y, self.width, self.height))

    # returns true if the given coordinates are within the bounds of the button
    def clicked(self, coords):
        return coords[0] >= self.x and coords[0] <= self.x+self.width and coords[1] >= self.y and coords[1] <= self.y+self.height 

launch_button = button("Hello", 300, 720, 200, 60)

# displays the current state of the game
def display_game(current_phase):
    # clear the screen
    settings.screen.fill(settings.water_blue)
    game_objects.ice(settings.screen).display()
    
    # display all the pucks
    for puck in game_objects.p1_pucks + game_objects.p2_pucks:
        puck.display()
        if puck.drawing_arrow:
            puck.arrow.display()

    # display arrows when player is setting up
    if current_phase == settings.PHASE_PLAYER1_SETUP:
        for puck in game_objects.p1_pucks:
            puck.arrow.display()
        if game_objects.all_arrows_drawn(game_objects.p1_pucks):
            launch_button.display()
    elif current_phase == settings.PHASE_PLAYER2_SETUP:
        for puck in game_objects.p2_pucks:
            puck.arrow.display()
        if game_objects.all_arrows_drawn(game_objects.p2_pucks):
            launch_button.display()


    # display everything on the screen
    pygame.display.flip()