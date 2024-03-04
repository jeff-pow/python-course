import sys


class P3image:
    @property
    # Pixel list getter
    def pixels(self):
        return self._pixels

    @pixels.setter
    # Pixel list setter
    def pixels(self, pixels):
        self._pixels = pixels

    @property
    # Image type getter
    def img_type(self):
        return self._img_type

    @img_type.setter
    # Image type setter
    def img_type(self, img_type):
        self._img_type = img_type

    @property
    # Returns max color code
    def max_color_code(self):
        return self._max_color_code

    @max_color_code.setter
    # Changes max color code
    def max_color_code(self, max_color_code):
        self._max_color_code = max_color_code

    @property
    # Returns height
    def height(self):
        return self._height

    @height.setter
    # Sets height
    def height(self, height):
        self._height = height

    @property
    # Returns width
    def width(self):
        return self._width

    @width.setter
    # Sets width
    def width(self, width):
        self._width = width

    @property
    # Returns description
    def description(self):
        return self._description

    @description.setter
    # Sets description
    def description(self, description):
        self._description = description

    # Overridden method that allows the object to be implicitly
    # converted to a string by python
    def __str__(self):
        ret = ""
        ret += str(self.description) + "\n"
        ret += 'Type: ' + str(self.img_type) + "\n"
        ret += 'Width: ' + str(self.width) + ' Height: ' + str(self.height)
        return ret

    # Constructor for the image class
    def __init__(self, img_type, description, width, height, max_color_code):
        self.img_type = img_type
        self.description = description
        self.width = width
        self.height = height
        self.max_color_code = max_color_code
        self.pixels = []

    @staticmethod
    # Creates an instance of an image object from a ppm file
    def load_image(filename):
        with open(filename, "r") as file:
            data = file.readlines()
            comment = ''
            img_desc = data[0:4]
            for line in img_desc:
                if line.strip().startswith('#'):
                    comment = line.strip()
            x = [line for line in data[0:4] if not (line.strip().
                                                    startswith('#'))]
            img_type = x[0].strip()
            print(img_type)
            if img_type != 'P3':
                print('Invalid image type')
                sys.exit()

            (width, height) = tuple([int(x) for x in x[1].split()])
            max_color_code = int(x[2])
            img = P3image(img_type, comment, width, height, max_color_code)
            data = data[4:]
            for x in range(width * height):
                pixels = data[3 * x: 3 * x + 3]
                pixels = tuple([int(x) for x in pixels])
                img.pixels.append(pixels)
            return img

    # Writes an image to a file in the ppm format, where it can be read by
    # another program
    def output_image(self, file_name):
        with open(file_name, 'w') as file:
            file.write(str(self.description) + "\n")
            file.write(str('P3') + '\n')
            file.write(str(self.width).strip() + ' ' +
                       str(self.height).strip() + '\n')
            file.write('\n')
            file.write(str(self.max_color_code))
            file.write('\n')
            for (r, g, b) in self.pixels:
                file.write(str(r))
                file.write('\n')
                file.write(str(g))
                file.write('\n')
                file.write(str(b))
                file.write('\n')
