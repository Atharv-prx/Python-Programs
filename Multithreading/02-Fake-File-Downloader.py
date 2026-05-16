import threading
import time
import random

stop_event = threading.Event() 
print_lock = threading.Lock()

def download_file(file_name, file_size):
    
    speed = random.randint(50, 100)
    downloaded_mb = 0
    percent_loaded = 0
    
    with print_lock:
        print(f"\n====={file_name} download started=====")
        print(f"File Size: {file_size}MB, Download Speed: {speed}MB/s")
    
    while downloaded_mb < file_size and not stop_event.is_set():
        with print_lock:
            print(f"\n {file_name} Loading....{downloaded_mb}MB loaded ({percent_loaded:.1f}%)")
        
        time.sleep(1)

        downloaded_mb  = min(downloaded_mb + speed, file_size) # Prevents overshooting the file size
        percent_loaded = (downloaded_mb / file_size) * 100

    with print_lock:

        if stop_event.is_set(): 
            print(f"\n{file_name} stopped Downloading!")

        else:
            print(f"\n====={file_name} Downloaded======\n")

def stop_command():

    while True:
        command = input("\nType 'stop' to stop all files to load: ").strip().lower()

        if command == "stop":
            stop_event.set()

            with print_lock:
                print("\nStopping downloading...")
            break
# ===============
# Helper function
# ===============

def get_int(prompt):

    while True:

        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Enter a positive number.")

        except ValueError:
            print("Invalid number.")

def get_name(prompt):

    while True:

        value = input(prompt).strip()

        if not value:
            print("Name cannot be empty.")
            continue

        return value.title()

def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Enter a positive number.")
        except ValueError:
            print("Invalid number.")

def main():
    
    threads = []
    number_of_files = get_int("How many files do you want to download? ")

    for _ in range(number_of_files):

        file_name = get_name("Enter the file name to download: ")
        file_size = get_float("Enter the file size in MB: ")

        thread = threading.Thread(target=download_file, 
                                  args=(file_name, file_size), 
                                  name=f"{file_name} Thread")
        
        threads.append(thread)

    for thread in threads:
        thread.start()
    
    input_thread = threading.Thread(target = stop_command, name = "Input Thread", daemon=True)
    input_thread.start()

    for thread in threads:
        thread.join()

    print("\nMain Program Finished.")

if __name__ == "__main__":
    main()