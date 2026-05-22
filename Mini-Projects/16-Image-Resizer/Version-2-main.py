from PIL import Image
import os
import threading
print_lock = threading.Lock()

# Instead of "for file in os.listdir("input"):" we use a function, this function will process one thread at a time
def resize_image(file):

    path = f"input/{file}"

    img = Image.open(path)

    img.thumbnail((800, 600))

    output_path = f"output/{file}"

    img.save(output_path)
    
    with print_lock:
        print(f"{file} resized successfully.")

# Creating threads 
threads = []

for file in os.listdir("input"):

    t = threading.Thread(target=resize_image, args=(file,))

    threads.append(t)

    t.start()

# Waiting for all threads
for t in threads:
    t.join()

print("\nAll images processed.")