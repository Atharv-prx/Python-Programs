from PIL import Image
import os

for file in os.listdir("input"):

    path = f"input/{file}"

    img = Image.open(path)

    img.thumbnail((800, 600))

    output_path = f"output/{file}"

    img.save(output_path)

    print(f"{file} resized successfully.")