from image import Image

lut = list(range(256))

file = input("Enter file name: ")
img = Image() # create Image object
img.read_pgm(f"images/{file}.pgm") # read file data into Image object

# inverting image pixels
for row in range(img.height):
    for col in range(img.width):
        print(img.get(row, col))
        inverted = lut[255 - img.get(row, col)] # process invert value of pixel through LUT
        img.set(row, col, inverted)

img.write_pgm(f"Inverted_{file}.pgm") # writing new inverted image to pgm
