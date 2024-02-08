from PIL import Image, ImageDraw
from math import ceil

GRID_SIZE = 5
CELL_SIZE = 40

def _create_background_image(bgcolor):
    # height = width since it's a square
    image_width = GRID_SIZE * CELL_SIZE
    
    return Image.new("RGB", (image_width, image_width), bgcolor)

def _draw_square(draw, pos_x, pos_y, color):
    start = (pos_x * CELL_SIZE, pos_y * CELL_SIZE)
    end = ((pos_x + 1) * CELL_SIZE, (pos_y + 1) * CELL_SIZE)
    draw.rectangle([start, end], fill=color)

def hash_to_grid(hash):
    """
    Create a grid to represent am avatar given a hash value
    """
    # create a grid of zeros to represent the avatar
    grid = [[0] * GRID_SIZE  for _ in range(GRID_SIZE)]

    # populate half of the grid with 1 for some positions based 
    # on the hash to int conversion (checking if it's even or odd)
    # the other half of the grid will be mirrored to create symmetry 
    for i in range(GRID_SIZE):
        for j in range(ceil(GRID_SIZE / 2)):
            hashed_flag = int(hash[i * GRID_SIZE + j], 16) % 2
            grid[i][j] = hashed_flag
            # mirror value
            grid[i][GRID_SIZE - j - 1] = hashed_flag

    return grid

def draw_avatar(grid, color, bgcolor):
    """
    Create and return an image given a grid
    """
    image = _create_background_image(bgcolor)
    draw = ImageDraw.Draw(image)
    
    for y, row in enumerate(grid):
        for x in range(len(row)):
            if grid[y][x] == 1:
                _draw_square(draw, x, y, color)

    return image
