import pyautogui
import time
import sys
from PIL import Image, ImageDraw, ImageFont
import random
import os
import re 


while True:
    image = pyautogui.screenshot()
    timestamp = int(time.time())
    # screenshot.save(f"./output/{timestamp}.png")

    # image = Image.open(f"./output/{timestamp}.png")

    # Define bounding box coordinates (x1, y1, x2, y2)
    x_midpoint, y_midpoint = image.size[0] / 2, image.size[1] / 2

    # crop by random amount
    random_number_x1 = random.randint(0, int(image.size[0] / 4))
    random_number_x2 = image.size[0] - random.randint(0, int(image.size[0] / 4))
    random_number_y1 = random.randint(0, int(image.size[1] / 4))
    random_number_y2 = image.size[1] - random.randint(0, int(image.size[1] / 4))
    # image = image.crop((random_number_x1, random_number_y1, random_number_x2, random_number_y2))
    print(random_number_x1, random_number_y1, random_number_x2, random_number_y2)
    # bbox = (image.size[0] / 2 - 50, image.size[1] / 2 - 50, image.size[0] / 2 + 50, image.size[1] / 2 + 50)

    # Create a drawing context
    # draw = ImageDraw.Draw(image)

    # Draw the rectangle
    # draw.rectangle(bbox, outline="red", width=25)
    # Optional: Adding a label inside the bounding box
    # font = ImageFont.truetype("arial.ttf", size=15)  # Adjust the font and size as needed
    # label = "Label"
    # label_position = (left, top - 20)  # Position the label above the bounding box
    # draw.text(label_position, label, fill="red", font=font)

    # Save or display the image
    x_loc = int(x_midpoint - random_number_x1 + 25)
    y_loc = int(y_midpoint - random_number_y1 - 25)
    print("old midpoint x: ", x_midpoint, "left crop: ", random_number_x1, "right crop: ", random_number_x2, "new midpoint x: ", x_loc)
    image.save(f"../yolov5/inference/images/{timestamp}_{x_loc}_{y_loc}_.png", "PNG")

    
    # file_path = f"./output/{timestamp}_{x_loc}_{y_loc}_.png"
    # a, x, y, b = file_path.split("_")
    # x = int(x)
    # y = int(y)
    # # rebuild the image to a red square
    # image = Image.open(file_path)
    # draw = ImageDraw.Draw(image)
    # draw.rectangle([x, y, x + 100, y + 100], outline="red", width=15)
    # image.save(f"./output/rebuilt/{x}_{y}.png", "PNG")
    time.sleep(1)

    
# output_dir = "./output"
# for filename in os.listdir(output_dir):
#     if filename.endswith(".png"):
#         file_path = os.path.join(output_dir, filename)
#         im = Image.open(file_path)
#         filename_no_ext = filename.split('.')[0]
#         _, x, y, _ = filename_no_ext.split("_")
#         x = int(x)
#         y = int(y)
#         with open('./output/' + filename_no_ext + '.txt', 'w') as f:
#             f.write(f"0 {x / im.size[0]} {x / im.size[1]} {100 / im.size[0]} {100 / im.size[1]}")
#             f.close()
#         im.close()
#                 # draw = ImageDraw.Draw(im)
#                 # draw.rectangle([1657, 1603, 1757, 1703], outline="red", width=25)
#                 # im.save("./output/rebuilt/1_1657_1603.png", "PNG")
