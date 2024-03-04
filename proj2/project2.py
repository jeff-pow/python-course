# CSC295
# 10/17/23
# Jeff Powell
# Program reads in file names from the user for ppm files, and then blends the
# pixels in a user specified amount before creating a file for the blended
# image


import p3image
import sys
import os


# Function takes in two image class instances, and handles asking the user for
# the blend they would like. Errors if the images are not compatible for
# blending
def blend_images(img1: p3image.P3image, img2: p3image.P3image):
    if img1.max_color_code != img2.max_color_code:
        print('Max color codes differ')
        sys.exit()
    if len(img1.pixels) != len(img2.pixels):
        print('Differing number of pixels in images')
        sys.exit()
    if img1.width != img2.width or img1.height != img2.height:
        print('Image dimensions differ')
        sys.exit()

    while True:
        first_weight = float(input(
            'Enter a percentage weighting for the first image to blend: '))
        if 0 <= first_weight <= 100:
            break
    first_percentage = first_weight
    second_percentage = 100 - first_weight
    first_weight /= 100
    second_weight = 1 - first_weight
    comment = f"# blended image {first_percentage:.1f}% / {second_percentage:.1f}%"
    new_img: p3image.P3image = p3image.P3image("P3", comment, img1.width,
                                               img1.height,
                                               img1.max_color_code)
    for count in range(len(img1.pixels)):
        (r1, g1, b1) = img1.pixels[count]
        (r2, g2, b2) = img2.pixels[count]
        r = int(r1 * first_weight + r2 * second_weight)
        g = int(g1 * first_weight + g2 * second_weight)
        b = int(b1 * first_weight + b2 * second_weight)
        new_img.pixels.append((r, g, b))

    print('Output image in imageBlend.ppm')
    print(str(new_img))
    new_img.output_image('imageBlend.ppm')


# Starting point of the program. Responsible for getting file names from the
# user
def main():
    while True:
        file_name = str(input('Input file name of the first image: '))
        if os.path.isfile(file_name):
            img1 = p3image.P3image.load_image(file_name)
            break
        print('Invalid file name, please try again')

    while True:
        file_name = str(input('Input file name of the second image: '))
        if os.path.isfile(file_name):
            img2 = p3image.P3image.load_image(file_name)
            break
        print('Invalid file name, please try again')

    blend_images(img1, img2)


if __name__ == "__main__":
    main()
