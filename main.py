#!/usr/bin/env python3

from argparse import ArgumentParser, ArgumentTypeError
from hashlib import sha256
from color import is_hex_valid, hash_to_color, DEFAULT_COLOR, DEFAULT_BG_COLOR
from avatar import hash_to_grid, draw_avatar

def hash_input(str):
    return sha256(bytes(str, "utf-8")).hexdigest()

def validate_hex_color(value):
    if not is_hex_valid(value):
        raise ArgumentTypeError("Invalid hex color format. Valid format example: #a1b2c3")
    return value

def is_grid_boring(grid):
    first_element = grid[0][0]
    for row in grid:
        for element in row:
            if element != first_element:
                return False
    return True

def main():
    parser = ArgumentParser(prog="GenerateAvatar")

    # required arg
    parser.add_argument("input", help=(
        "Any text (if multiple words must be between quotes) to be used "
        "as seed to generate an avatar (e.g. my@email.com, 'some cool username')"))

    # optional args
    parser.add_argument("-c", "--color", type=validate_hex_color,
                        help="Block color in hex format (e.g. -c '#a1b2c3'; -c=#a1b2c3)")
    parser.add_argument("-bg", "--background", type=validate_hex_color,
                        help="Background color in hex format (e.g. -bg '#a1b2c3'; -bg=#a1b2c3)")
    parser.add_argument("-f", "--file",
                        help="File name of the output image (e.g. myavatar.png)")
    
    args = parser.parse_args()

    hash = hash_input(args.input)

    # generate a grid to represent the avatar
    grid = hash_to_grid(hash)

    # if the grid is all "1" or all "0" re-hash and try again
    while is_grid_boring(grid):
        hash = hash_input(hash)
        grid = hash_to_grid(hash)

    print("Hash generated from seed:\n" + hash)

    bgcolor = DEFAULT_BG_COLOR
    if args.background != None:
        bgcolor = args.background

    if args.color != None:
        color = args.color
    else:
        color = hash_to_color(hash)
        # handle color conflict if same as background
        if color == bgcolor:
            color = DEFAULT_COLOR

    img = draw_avatar(grid, color, bgcolor)
    
    # save it if file arg was given, otherwise show
    if args.file != None:
        img.save(args.file)
        print("Avatar image saved as:\n" + args.file)
    else:
        img.show()

if __name__ == "__main__":
    main()
