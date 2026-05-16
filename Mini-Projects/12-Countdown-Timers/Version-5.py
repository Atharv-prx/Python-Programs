# Added a feature to stop the timer by user input while program is running.

import threading
import time

stop_event = threading.Event() 
print_lock = threading.Lock() # Create a lock for synchronizing print statements

def timer(timer_name, minutes):

    thread_name = threading.current_thread().name
    
    with print_lock:
        print(f"\n=====[{thread_name}] {timer_name} started=====")

    total_seconds = int(minutes*60)

    while total_seconds > 0 and not stop_event.is_set():  

        mins, secs = divmod(total_seconds, 60)

        with print_lock:
            print(f"\n{timer_name}: {mins:02}:{secs:02} remaining")

        time.sleep(1)

        total_seconds -= 1

    with print_lock:

        if stop_event.is_set(): 
            print(f"\n[{thread_name}] {timer_name} Stopped Early")

        else:
            print(f"\n=====[{thread_name}] {timer_name} finished======\n")

def stop_command():

    while True:
        command = input("\nType 'stop' to stop all timers: ").strip().lower()

        if command == "stop":
            stop_event.set()

            with print_lock:
                print("\nStopping all timers...")
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

# =============
# Main Program
# =============
def main():

    threads = []

    choice = get_int("How many timers do you want to add? ")

    for _ in range (choice):

        timer_name = get_name("Enter timer name: ")
        timer_minutes = get_int("Enter timer duration in minutes: ")

        thread = threading.Thread(target=timer,
                                  args=(timer_name, timer_minutes), 
                                  name=f"{timer_name} Thread")

        threads.append(thread)

    # If we combine start and join into one loop, then timers would run one by one.
    for thread in threads:
        thread.start()

    input_thread = threading.Thread(target=stop_command, name="Input Thread", daemon=True)
    input_thread.start()
    # Using daemon cuz if all timers finish naturally, program should exit without waiting for user input.

    for thread in threads:
        thread.join()
    
    print("\nAll timers finished.")

if __name__ == "__main__":
    main()