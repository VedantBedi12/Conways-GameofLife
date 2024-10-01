

# Conway's Game of Life in Python

This repository contains a Python implementation of Conway's Game of Life, a cellular automaton devised by the British mathematician John Horton Conway in 1970. The Game of Life simulates the evolution of cells in a grid, following simple rules that determine the survival or death of each cell.

## Introduction
Conway's Game of Life is a zero-player game, meaning it requires no further input from human players once the initial state of the cells has been set. The grid of cells evolves through multiple generations based solely on its initial configuration.

In this Python implementation using the Pygame library, you can set up an initial configuration of live and dead cells on a grid and observe how the patterns evolve over time based on the game's rules.

## Game Rules
The Game of Life operates on a grid of square cells, each of which can be in one of two states:
- **Alive (1)**
- **Dead (0)**

The evolution of the grid is determined by these simple rules applied to each cell at every step (generation):

1. **Underpopulation**: A live cell with fewer than two live neighbors dies.
2. **Overpopulation**: A live cell with more than three live neighbors dies.
3. **Reproduction**: A dead cell with exactly three live neighbors becomes a live cell.
4. **Survival**: A live cell with two or three live neighbors continues to live.

Cells are considered to have up to 8 neighbors, located horizontally, vertically, and diagonally adjacent.

### Example Patterns:
- **Still Life**: A pattern that does not change between generations (e.g., block, beehive).
- **Oscillators**: A pattern that repeats itself after a fixed number of generations (e.g., blinker, toad).
- **Spaceships**: Patterns that translate themselves across the grid (e.g., glider).

## Installation
To run this implementation of Conway's Game of Life, you'll need Python and Pygame installed.

1. **Clone the repository**:
   ```bash
   git clone https://github.com/VedantBedi12/Conways-GameofLife.git
   cd conways-game-of-life
   ```

2. **Install dependencies**:
   ```bash
   pip install pygame
   ```

## Usage
Once installed, you can start the game by running the following command:
```bash
python game_of_life.py
```

### Controls:
- **Left-click**: Toggle cells between alive and dead before the simulation starts.
- **Spacebar**: Start/stop the simulation.
- **R key**: Reset the grid to an empty state.
- **C key**: Clear the grid and stop the simulation.
- **ESC key**: Exit the game.

## Customization
You can customize the grid size, speed of the simulation, and cell size by modifying the constants at the top of the `game_of_life.py` file. This allows for larger grids or faster/slower evolution of the cells.

### Example Customization:
```python
GRID_SIZE = 50  # Number of cells in both width and height
CELL_SIZE = 10  # Size of each cell in pixels
FPS = 10        # Frames per second (speed of the game)
```



---

