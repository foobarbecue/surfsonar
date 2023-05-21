from PIL import Image, ImageDraw, ImageFont
canvas = Image.new("1", (122, 250), 255)
draw = ImageDraw.Draw(canvas)
font_big = ImageFont.truetype("/home/aaron/surfsonar/src/ConsolaMonoBold-A9Am.ttf", 35)
font_medium = ImageFont.truetype("/home/aaron/surfsonar/src/ConsolaMonoBold-A9Am.ttf", 20)
font_small = ImageFont.truetype("/home/aaron/surfsonar/src/ConsolaMonoBold-A9Am.ttf", 15)

draw.text((0, -5), "depth", font=font_small)
draw.text((0, 10), " 5.2m", font=font_big, fill=0)

draw.text((0, 45), "confidence", font=font_small)
draw.text((0, 60), " 28%", font=font_big, fill=0)

draw.text((0, 95), "battery", font=font_small)
draw.text((0, 110), " 33%", font=font_big, fill=0)

draw.text((0, 145), "gps", font=font_small)

draw.text((0, 160), "6 fix\n11S 444699\n   3696019", font=font_medium)

canvas.show()