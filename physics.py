import pygame, settings, game_objects

friction_coeff = 5

def move():
    for puck in game_objects.p1_pucks + game_objects.p2_pucks:
        puck.x += puck.x_velo / 3
        puck.y += puck.y_velo / 3
        x_velo = puck.x_velo
        y_velo = puck.y_velo

        print(puck.x_velo)

        if puck.x_velo > 0:
            x_velo = max(0, puck.x_velo - friction_coeff)
        elif puck.x_velo < 0:
            x_velo = min(0, x_velo + friction_coeff)
        if puck.y_velo > 0:
            y_velo = max(0, puck.y_velo - friction_coeff)
        elif puck.y_velo < 0:
            y_velo = min(0, y_velo + friction_coeff)
        
        
        # slow the puck down with the friction_coeff
        puck.set_velo((x_velo, y_velo))