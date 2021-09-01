import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg',3)
for color in colors:
    rgb_colors.append(color.rgb)

print(rgb_colors)