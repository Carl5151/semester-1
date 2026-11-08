from filters import blur

original_file = input("Enter image file name: ")
img = blur(original_file)

# writing orignial file as a new blurred file
img.write_pgm(f"blurred_{original_file}.pgm")
