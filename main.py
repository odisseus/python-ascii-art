#!/bin/python
import os
import sys
import getopt
from itertools import zip_longest
from statistics import mean
from PIL import Image, ImageDraw, ImageFont

# Chars to be used in ascii art
chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM,;'[]<>?:{}\\1234567890-=!@#$%^&*()_+"

# Dict that that maps characters to their 'lightness' value
char_dict = {}


# I got this from stack overflow, partitions a sequence and fills in a value when there are no values left to take
def partition_with_padding(iterable, n, pad=None):
    """grouper(3, 'abcdefg', 'x') --> ('a','b','c'), ('d','e','f'), ('g','x','x')"""
    return list(zip_longest(*[iter(iterable)] * n, fillvalue=pad))


def write_alphabet():
    for c in chars:
        img = Image.new('RGB', (45, 75), (255, 255, 255))
        fnt = ImageFont.truetype("roboto mono.ttf", 75)
        d = ImageDraw.Draw(img)
        d.text((0, -16), c, fill="black", font=fnt)
        img.save("image/" + c + ".png")


def encode_image(image, square):
    width, _ = image.size
    # Get pixels
    pixels = [pixel[0] for pixel in image.getdata()]
    # Offset lowest pixel lightness by lowest character lightness
    lowest = min(int(x) for x in list(char_dict))
    # This might be a bad idea idk
    pixels = [lowest + lightness for lightness in pixels]
    # Group the continuous list into rows using image width
    grouped_rows = partition_with_padding(pixels, width)
    # Group columns into slices according to our square
    rows_with_grouped_columns = [partition_with_padding(row, square, pad=lowest) for row in grouped_rows]
    # Pad for grouping in case the image's dimensions are not a factor of our square
    pad_row = [[lowest for _ in range(square)] for _ in range(int(width / square))]
    # Group the rows of slices according to square
    grouped_square_slices = partition_with_padding(rows_with_grouped_columns, square, pad=pad_row)
    # Zip the different slices of each row together
    squares = [list(zip(*row)) for row in grouped_square_slices]
    # Average the value of each slice
    squares_slices_averaged = [[[mean(s) for s in row] for row in sq] for sq in squares]
    # Average the value of each square
    squares_averaged = [[mean(sq) for sq in row] for row in squares_slices_averaged]
    return squares_averaged


def get_char_for_point(point):
    char = char_dict[min(list(char_dict), key=lambda x: abs(x - point))]
    return char + char


def image_to_string(image, square):
    encoded = encode_image(image, square)
    return "\n".join(["".join([get_char_for_point(point) for point in row]) for row in encoded])


def print_usage():
    print("main.py -c <compression factor> -i <input file> -o <output file>")


def convert_to_ascii(input_path, output_path, compression_factor):
    # Make character images if they don't exist
    if not os.path.exists("image"):
        os.mkdir("image")
        write_alphabet()

    # Read characters into dict
    for c in chars:
        img = Image.open("image/" + c + ".png").convert('L')
        avg = mean(img.getdata())
        char_dict[avg] = c

    # Convert specified file with specified compression factor
    image = Image.open(input_path).convert("LA")
    ascii_art = image_to_string(image, compression_factor)

    # If output file is not empty, write the result to it
    if output_path != "":
        with open(output_path, "w") as output_file:
            output_file.write(ascii_art)

    # Print result to terminal
    print(ascii_art)


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hi:o:c:")
        input_file = ""
        output_file = ""
        compression_factor = 0
        for opt, arg in opts:
            if opt == "-h":
                print_usage()
            elif opt == "-i":
                input_file = arg
            elif opt == "-o":
                output_file = arg
            elif opt == "-c":
                compression_factor = int(arg)
        convert_to_ascii(input_file, output_file, compression_factor)
    except getopt.GetoptError:
        print_usage()


if __name__ == "__main__":
    main(sys.argv[1:])
