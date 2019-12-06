import serial
import time


class RGB(object):
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __copy__(self):
        return self.__class__(self.r, self.g, self.b)

    def __eq__(self, other):
        try:
            return self.r == other.r and self.g == other.g and self.b == other.b
        except AttributeError:
            return False


class SerialRGB(object):
    def __init__(self, comport):
        self.serial = serial.Serial()
        self.serial.baudrate = 115200
        self.serial.port = comport
        self.serial.bytesize = serial.EIGHTBITS
        self.serial.parity = "N"
        self.serial.stopbits = 1
        self.serial.open()
        time.sleep(2)
        
        if not self.serial.is_open:
            raise Exception("Could not open comport %s" % comport)
            
        self.amount_rgbs = self.get_amount_rgbs()

        self.perc = 100

    def dim_values(self, perc):
        self.perc -= perc

    def get_amount_rgbs(self):
        return 0  # TODO wait for amount_rgbs

    def write_rgb(self, rgb_value: RGB):
        #            (   r            ,   g            ,   b            )  Could maybe also use ord('(') but that returns Unicode
        rgb_array = [40, rgb_value.r, 44, rgb_value.g, 44, rgb_value.b, 41]
        return self.serial.write(bytearray(rgb_array))

    def write_rgbs(self, rgb_values: []):
        if len(rgb_values) != self.amount_rgbs:
            raise Exception("Given amount RGBs %d != Device amount RGBs %d" % (len(rgb_values), self.amount_rgbs))
        rgb_array = [40]
        for rgb_value in rgb_values:
            rgb_array += [int(rgb_value.r / 100 * self.perc), int(rgb_value.g / 100 * self.perc), int(rgb_value.b / 100 * self.perc)]
        rgb_array.append(41)
        return self.serial.write(bytearray(rgb_array))

