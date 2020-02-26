'''
Created on Feb 26, 2020

@author: nicomp
'''
import random
from PIL import Image, ImageFilter, ImageDraw, ImageFont

default_color_red = 228
default_color_green = 150
default_color_blue = 150
def generate_random_string(length):
    random_string = ""
    for i in range(0,length):
        random_string = random_string + random.choice('1234567890ABCDEFGHIJKLMNOPQRSTUVQXYZ')
    return random_string

def draw_random_ellipse(draw):
    # A random circle on the image
    a = random.randrange(10, 300, 1)
    b = random.randrange(10, 275, 1)
    c = a + random.randrange(20, 30, 1)
    d = b + random.randrange(20, 30, 1)
    draw.ellipse((a,b,c,d), fill=(default_color_red + random.randrange(-100,100,1), 
                                  default_color_green + random.randrange(-100,100,1), 
                                  default_color_blue + random.randrange(-100,100,1), 255), 
                                  outline = "black")

def generate_captcha():
    captcha_string = generate_random_string(5)
    print(">" + captcha_string + "<")
    captcha_image = Image.new("RGBA", (400, 200), (default_color_red,default_color_green,default_color_blue))
    fontStyle = ImageFont.truetype("Aaargh.ttf", 48)     # font must be in the same folder as the .py file. 

    # Arbitrary starting co-ordinates for the text we will write
    x = 10 + random.randrange(0, 100, 1)
    y = 79
    draw = ImageDraw.Draw(captcha_image, "RGBA")
    for letter in captcha_string:
        print(letter)
        draw.text((x, y), letter, (0,0,0),font=fontStyle)    # Write in black
        x = x + 35
        y = y +  random.randrange(-10, 10, 1)
    
    for i in range(1,10):
        draw_random_ellipse(draw)
    return captcha_image
