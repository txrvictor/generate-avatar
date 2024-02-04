#!/usr/bin/env python3

from argparse import ArgumentParser, ArgumentTypeError
from hashlib import sha256
from color import is_hex_valid, hash_to_color, DEFAULT_BG_COLOR

def hash_input(str):
    return sha256(bytes(str, "utf-8")).hexdigest()

def validate_hex_color(value):
    if not is_hex_valid(value):
        raise ArgumentTypeError("Invalid hex color format. Valid format example: #a1b2c3")
    return value

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
    parser.add_argument("-f", "--file", help="File name of the output image")
    
    args = parser.parse_args()

    hash = hash_input(args.input)

    # TODO remote this
    print(args)
    print(hash)

    if args.color != None:
        color = args.color
    else:
        color = hash_to_color(hash)

    bgcolor = DEFAULT_BG_COLOR
    if args.background != None:
        bgcolor = args.background

    # TODO remote this
    print(color)
    print(bgcolor)

if __name__ == "__main__":
    main()
