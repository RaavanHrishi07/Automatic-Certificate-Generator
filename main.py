# importing packages & modules
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

# Implementation to generate certificate
df = pd.read_csv('list.csv')
font = ImageFont.truetype('arial.ttf', 60)
for index, j in df.iterrows():
    img = Image.open('certificate.png')
    draw = ImageDraw.Draw(img)
    name = '{}'.format(j['name'])

# Center the name horizontally
bbox = draw.textbbox((0, 0), name, font=font)
text_width = bbox[2] - bbox[0]

x = (img.width - text_width) // 2
y = 410

draw.text(
    (x, y),
    name,
    fill=(0, 0, 0),
    font=font
)  # customization
img.save('pictures/{}.png'.format(j['name']))
