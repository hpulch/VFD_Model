import math
import pygame


def make_sine_points(panel_width, panel_height):
    coordinates = []
    length = panel_width
    amplitude = 120
    number_of_waves = 5
    center_coordinate = panel_height/2
    for x_coordinate in range(length):
        radians = x_coordinate / length * 2 * math.pi
        y_coordinate = amplitude * math.sin(number_of_waves * radians)
        coordinates.append((x_coordinate, y_coordinate + center_coordinate))
    return coordinates


pygame.init()
width = 800
height = 640
screen = pygame.display.set_mode((width, height))
screen.fill((250, 250, 250))

running = True
while running:
    sine_wave = make_sine_points(width, height)
    pygame.draw.lines(screen, (0, 0, 0), False, sine_wave)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.time.Clock().tick(60)
pygame.quit()
