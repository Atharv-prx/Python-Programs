# Instead of 1 thread per image, we create only 4 thread at a time to decrease overloading over massive amounts of photos
# Earlier version would work with low amount of photo but this would work even with huge amount of photos

from PIL import Image
import os
import threading
import queue

q = queue.Queue()
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

# Creating worker function
def worker():

    while q.empty():

        file = q.get()

        resize_image(file)

        q.task_done

# Put jobs into queue
for file in os.listdir("input"):
    q.put(file)

# Creating threads 
threads = []

for i in range(4):

    t = threading.Thread(target=worker)

    threads.append(t)

    t.start()

# Waiting for all threads
for t in threads:
    t.join()

print("\nAll images processed.")