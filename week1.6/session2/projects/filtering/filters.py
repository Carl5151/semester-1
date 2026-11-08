from image import Image

def blur(original_file):
    img = Image() # create image object
    img.read_pgm(f"images/{original_file}.pgm") # puts file data into image object

    # checking all pixels in img
    for row in range(1, img.height - 1):
        for col in range(1, img.width - 1):
            # finding average (blur value) of pixel in 3x3 window
            sum = 0
            for r in range(row - 1, row + 2):
                for c in range(col - 1, col + 2):
                    sum += img.get(r, c) # getting pixel at index [r][c]
            blur_val = round(sum / 9)
            img.set(row, col, blur_val) # setting pixel value at index [r][c] to blur value

    return img # returns the blurred image 
