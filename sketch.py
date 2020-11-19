from click import getchar
from gfxhat import lcd,  fonts
from PIL import Image, ImageFont, ImageDraw

def clearScreen(lcd):
    lcd.clear()
    lcd.show()
    displayText('Etch Sketch', lcd, 25, 15)
    sketcher()

def displayText(text,lcd,x,y):
    lcd.clear()
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold, 24)
    w, h = font.getsize(text)
    draw.text((x,y), text, 1, font)
    for x1 in range(x,x+w):
        for y1 in range(y,y+h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)
    lcd.show()

def sketcher(x=0, y=0):
    while True:
        direction = getchar()
        lcd.set_pixel(x, y, 1)
        lcd.show()

        if (direction == '\x1b[A'): # UP
            y -= 1
            if (y < 0):
                y = 63
            lcd.set_pixel(x, y, 1)
            lcd.show()
        elif (direction == '\x1b[B'): # DOWN
            y += 1
            if (y > 63):
                y = 0
            lcd.set_pixel(x, y, 1)
            lcd.show()
        elif (direction == '\x1b[C'): # RIGHT
            x += 1
            if (x > 127):
                x = 0
            lcd.set_pixel(x, y, 1)
            lcd.show()
        elif (direction == '\x1b[D'): # LEFT
            x -= 1
            if (x < 0):
                x = 127
            lcd.set_pixel(x, y, 1)
            lcd.show()
        elif direction == 's':
            clearScreen(lcd)
        elif (direction == 'q'):
            break

displayText('Etch Sketch', lcd, 25, 15)
sketcher()

lcd.clear()
lcd.show()