from serial_rgb import RGB, SerialRGB

if __name__ == '__main__':
    arduino = SerialRGB("COM4")
    test_rgb = RGB(255, 255, 0)
    
    arduino.write_rgb(test_rgb)
