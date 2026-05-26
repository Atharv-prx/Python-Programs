from PIL import Image
import os
import threading
import queue

# ==============
# Global Objects

q = queue.Queue()
print_lock = threading.Lock()

# ================
# Helper Functions

def get_int(prompt):

    while True:

        try:
            value = int(input(prompt))

            if value > 0:
                return value

            print("Enter a positive number.")

        except ValueError:
            print("Invalid number.")

def get_target_format():

    allowed_formats = ["png", "jpg", "jpeg", "webp"]

    while True:

        target_format = input("Enter output format--> (png/jpg/jpeg/webp): ").strip().lower()

        if target_format in allowed_formats:
            return target_format

        print("Unsupported format.")

# ================
# Image Processing

def resize_image(file, width, height, target_format):

    path = f"input/{file}"

    img = Image.open(path)

    # Thumbnail resizes while maintaining aspect ratio
    img.thumbnail((width, height))

    # Split filename and extension
    filename, old_extension = os.path.splitext(file)

    # JPG doesn't support transparency
    if target_format == "jpg":
        img = img.convert("RGB")

    # Create output path
    output_path = (f"output/{filename}.{target_format}")

    # Save image
    img.save(output_path)

    with print_lock:

        print(f"{file} converted to {target_format} successfully.")

# =============
# Worker Thread

def worker(width, height, target_format):

    while not q.empty():

        file = q.get()

        resize_image(
            file,
            width,
            height,
            target_format
            )

        q.task_done()

# =============
# Main Function

def main():

    target_format = get_target_format()

    width = get_int("Enter width: ")
    height = get_int("Enter height: ")

    # Add files to queue
    for file in os.listdir("input"):
        q.put(file)

    # Create worker threads
    threads = []

    for i in range(4):

        t = threading.Thread(
            target=worker,
            args=(
                width,
                height,
                target_format
            )
        )

        threads.append(t)

        t.start()

    # Wait for queue completion
    q.join()

    # Wait for all threads
    for t in threads:
        t.join()

    print("\nAll images processed.")

if __name__ == "__main__":
    main()