from PIL import Image
import os
import threading
import queue

def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Enter a positive number.")
        except ValueError:
            print("Invalid number.")

q = queue.Queue()
print_lock = threading.Lock()

# Ask user for target format
target_format = input("Enter output format (png/jpg/jpeg/webp): ").lower()

# Allowed formats
allowed_formats = ["png", "jpg", "jpeg", "webp"]

if target_format not in allowed_formats:
    print("Unsupported format.")
    exit()

width = get_int(input("Enter width: "))
height = get_int(input("Enter height: "))

# Process one image
def resize_image(file):

    path = f"input/{file}"

    img = Image.open(path)

    # Resize image
    img.thumbnail((width, height))

    # Split filename and extension
    filename, old_extension = os.path.splitext(file)

    # JPG/JPEG doesn't support transparency
    if target_format in ["jpg", "jpeg"]:
        img = img.convert("RGB")

    # Create new output path
    output_path = f"output/{filename}.{target_format}"

    # Save converted image
    img.save(output_path)

    with print_lock:
        print(
            f"{file} converted to "
            f"{target_format} successfully."
        )

# Worker thread
def worker():

    while not q.empty():

        file = q.get()

        resize_image(file)

        q.task_done()

# Add jobs to queue
for file in os.listdir("input"):
    q.put(file)

# Create worker threads
threads = []

for i in range(4):

    t = threading.Thread(target=worker)

    threads.append(t)

    t.start()

# Wait for all queue tasks
q.join()

# Wait for all threads
for t in threads:
    t.join()

print("\nAll images processed.")