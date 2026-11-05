from pixel_rep import Image

blank_image = Image.create(5, 6, 1, 20)
print(blank_image)

img = Image()
img.read_pgm("test.pgm")
print(f"dimension - height: {img.height}, width: {img.width}")
print(f"max gray: {img.max_value}")
