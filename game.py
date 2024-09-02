import os, sys, math, pygame, game_objects, settings, ui, physics

# initializing colors
black = settings.black
white = settings.white
blue = settings.blue
water_blue = settings.water_blue

# initializing display
screen = settings.screen
# initializing clock object
clock = settings.clock
# show title
pygame.display.set_caption("KNOCKOUT")

# initializing the ice surface
ice = game_objects.ice(screen)

# initializing the start phase
current_phase = settings.PHASE_PLAYER1_SETUP

# Defining frame rate and run status
fps_limit = settings.fps_limit

running = True
while running:
    clock.tick(fps_limit)

    ui.display_game(current_phase)

    if current_phase == settings.PHASE_PLAYER1_SETUP:
        for puck in game_objects.p1_pucks:
            if puck.drawing_arrow:
                # puck.arrow.set_arrow(pygame.mouse.get_pos())
                # puck.arrow.set_arrow((min(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[0] + ((pygame.mouse.get_pos()[0]-puck.x)/ puck.arrow.get_length())), min(pygame.mouse.get_pos()[1], pygame.mouse.get_pos()[1] + ((pygame.mouse.get_pos()[1]-puck.y)/ puck.arrow.get_length()))))
                if math.sqrt((pygame.mouse.get_pos()[0] - puck.x)**2 + (pygame.mouse.get_pos()[1] - puck.y)**2) <= 200:
                    puck.arrow.set_arrow(pygame.mouse.get_pos())
                else:
                    puck.arrow.set_arrow(
                        (puck.x + 200*((pygame.mouse.get_pos()[0]-puck.x) / (math.sqrt((puck.x - pygame.mouse.get_pos()[0])**2 + (puck.y - pygame.mouse.get_pos()[1])**2))), 
                         puck.y + 200*((pygame.mouse.get_pos()[1]-puck.y) / (math.sqrt((puck.x - pygame.mouse.get_pos()[0])**2 + (puck.y - pygame.mouse.get_pos()[1])**2)))))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                print(ui.launch_button.clicked((x, y)))
                for puck in game_objects.p1_pucks:
                    if puck.drawing_arrow:
                        puck.arrow.set_arrow((puck.arrow.end_x, puck.arrow.end_y))
                    # if a puck is clicked on
                    if (x - puck.x)**2 + (y - puck.y)**2 < puck.size**2:
                        puck.drawing_arrow = True
                    else:
                        puck.drawing_arrow = False
                if game_objects.all_arrows_drawn(game_objects.p1_pucks) and ui.launch_button.clicked((x, y)):
                    for puck in game_objects.p1_pucks:
                        puck.set_velo((puck.arrow.dx, puck.arrow.dy))
                    current_phase = settings.PHASE_PLAYER2_SETUP
    if current_phase == settings.PHASE_PLAYER2_SETUP:
        for puck in game_objects.p2_pucks:
            if puck.drawing_arrow:
                # puck.arrow.set_arrow(pygame.mouse.get_pos())
                # puck.arrow.set_arrow((min(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[0] + ((pygame.mouse.get_pos()[0]-puck.x)/ puck.arrow.get_length())), min(pygame.mouse.get_pos()[1], pygame.mouse.get_pos()[1] + ((pygame.mouse.get_pos()[1]-puck.y)/ puck.arrow.get_length()))))
                if math.sqrt((pygame.mouse.get_pos()[0] - puck.x)**2 + (pygame.mouse.get_pos()[1] - puck.y)**2) <= 200:
                    puck.arrow.set_arrow(pygame.mouse.get_pos())
                else:
                    puck.arrow.set_arrow(
                        (puck.x + 200*((pygame.mouse.get_pos()[0]-puck.x) / (math.sqrt((puck.x - pygame.mouse.get_pos()[0])**2 + (puck.y - pygame.mouse.get_pos()[1])**2))), 
                         puck.y + 200*((pygame.mouse.get_pos()[1]-puck.y) / (math.sqrt((puck.x - pygame.mouse.get_pos()[0])**2 + (puck.y - pygame.mouse.get_pos()[1])**2)))))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                print(ui.launch_button.clicked((x, y)))
                for puck in game_objects.p2_pucks:
                    if puck.drawing_arrow:
                        puck.arrow.set_arrow((puck.arrow.end_x, puck.arrow.end_y))
                    # if a puck is clicked on
                    if (x - puck.x)**2 + (y - puck.y)**2 < puck.size**2:
                        puck.drawing_arrow = True
                    else:
                        puck.drawing_arrow = False
                if game_objects.all_arrows_drawn(game_objects.p2_pucks) and ui.launch_button.clicked((x, y)):
                    for puck in game_objects.p2_pucks:
                        puck.set_velo((puck.arrow.dx, puck.arrow.dy))
                    current_phase = settings.PHASE_SIMULATION
    if current_phase == settings.PHASE_SIMULATION:
        if game_objects.pucks_stationary(game_objects.p1_pucks + game_objects.p2_pucks):
            for puck in game_objects.p1_pucks + game_objects.p2_pucks:
                puck.arrow.reset_arrow()
            current_phase = settings.PHASE_PLAYER1_SETUP
        physics.move()
 

    
pygame.quit()
sys.exit()

