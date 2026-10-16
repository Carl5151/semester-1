# Week 1.3, Session 2: Validate image

# Open a pgm image
# You could handle file errors with try/except
file = input("Enter file name: ")

try:
    with open(f"images/{file}", "r") as pgm:
        # Read the file content
        data = pgm.readlines()
        clean_data = []
        for line in data:
            clean_data.append(line.strip().split())
        pixel_start = 0
        # Store the width, the height, and the maximum gray value
        if clean_data[1][0] == "#":
            pixel_start = 4
            width = int(clean_data[2][0])
            height = int(clean_data[2][1])
            max = int(clean_data[3][0])
        else:
            pixel_start = 3
            width = int(clean_data[1][0])
            height = int(clean_data[1][1])
            max = int(clean_data[2][0])
        # For each pixel, check if the pixel value is between 0 and the maximum gray value inclusive
        valid_pixels = True
        # iterates through each line of pixels
        for line in range(pixel_start, len(clean_data)):
            # check if invalid pixel found
            if valid_pixels:
                # check each individual pixel
                for gray_value in range(len(clean_data[line])):
                    if int(clean_data[line][gray_value]) > max:
                        valid_pixels = False
                        break
            # stop if invalid pixel found        
            else:
                break
        # Check if the widths and heights are the same as specified
        valid_width = True
        valid_height = True
        if len(clean_data[pixel_start]) != width:
            valid_width = False
        if len(clean_data) - pixel_start != height:
            valid_height = False

    # 4. Print the final verdit.
    #  Print `Valid image` if the widths, the heights are the same, and all pixel values between 0 and the maximum gray value inclusive
    #  Print `Invalid width` if the widths are different
    #  Print `Invalid height` if the heights are different
    #  Print `Invalid pixel values` if any pixel values is less than 0 and greater than the maximum gray value
    if valid_width and valid_height and valid_pixels:
        print("Valid Image")
    if not valid_width:
        print("Invalid Width")
    if not valid_height:
        print("Invalid Height")
    if not valid_pixels:
        print("Invalid Pixel Values")

except:
    print("Invalid File")