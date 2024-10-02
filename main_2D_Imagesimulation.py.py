import pygame, sys
from simulation import Simulation
import numpy as np
from PIL import Image



pygame.init()

GREY = (29, 29, 29)
WINDOW_WIDTH = 750
WINDOW_HEIGHT = 750
CELL_SIZE = 25
FPS = 12
gen = 0

im = Image.open('dino.jpg')

grid_size = (WINDOW_WIDTH // CELL_SIZE, WINDOW_HEIGHT // CELL_SIZE)  # (30, 30)
down_sampled = im.resize(grid_size, resample=Image.NEAREST)


bw_image = down_sampled.convert('L')
threshold = 200
binary_image = bw_image.point(lambda x: 255 if x > threshold else 0, '1')


binary_array = np.array(binary_image)


game_of_life_state = np.where(binary_array == 0, 1, 0)





#binary_image.save('new_image_bw_binary.jpg')


window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Game of Life, Generation:" + str(gen))




clock = pygame.time.Clock()


simulation = Simulation(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)
for row in range(len(game_of_life_state)):
    for column in range(len(game_of_life_state[0])):
        if game_of_life_state[row][column] == 1:
            simulation.toggle_cell(row, column)

# Simulation loop
while True:
    # 1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            row = pos[1] // CELL_SIZE
            column = pos[0] // CELL_SIZE
            simulation.toggle_cell(row, column)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                simulation.start()
                pygame.display.set_caption("Game of Life is running, Generation:" + str(gen))
            elif event.key == pygame.K_SPACE:
                simulation.stop()
                pygame.display.set_caption("Game of Life has stopped, Generation:" + str(gen))
            elif event.key == pygame.K_f:
                FPS += 2
            elif event.key == pygame.K_s:
                if FPS > 5:
                    FPS -= 2
            elif event.key == pygame.K_r:
                simulation.create_random_state()
            elif event.key == pygame.K_c:
                simulation.clear()

    # 2. Updating State
    gen+=1
    simulation.update()

    # 3. Drawing
    window.fill(GREY)
    simulation.draw(window)

    pygame.display.update()
    clock.tick(FPS)
