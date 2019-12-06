# Summary #

This project is the opposite side of one of these:
* [Arduino RGBDriver](https://bitbucket.org/rgb_leds/ardunio-rgbdriver).
* [PIC16F1825 RGBDriver](https://bitbucket.org/rgb_leds/pic16f1825-rgbdriver)

# How to set it up?
## Dependencies ##

* OS: This basic example was tested on Windows and on a Raspberry Pi 2B. 
* Python: Testd on Python 3.4 and Python 3.6 and Python 3.8
* PythonPackages: pyserial: `python -m pip install pyserial`

## How to call?

Taken from the example in `example.py`:

``` python

from serial_rgb import RGB, SerialRGB

if __name__ == '__main__':
    arduino = SerialRGB("COM4")
    test_rgb = RGB(255, 255, 0)
    
    arduino.write_rgb(test_rgb)


```

# Known bug
`get_amount_rgbs()` is unfortunatelly currently not working since when initiatilization of COM-Port some traffic to Arduino occurres. This bug i only necessary for the new Protocol (differnt colors for every LED). If you want to bypass that problem just manually set the `amount_rgbs` attribute.


