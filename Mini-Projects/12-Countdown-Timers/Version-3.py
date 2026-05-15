# Added synchronized printing to avoid jumbled output
# with lock ne thread fully completes its print section before another thread prints.

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

study_thread = threading.Thread(target = timer, args = ("Study Timer", 0.5), name = "Study Thread")

break_thread = threading.Thread(target=timer, args=("Break Timer", 0.5), name="BreakThread")

water_thread = threading.Thread(target=timer, args=("Water Reminder", 1), name="WaterThread", daemon=True)

study_thread.start()
break_thread.start()
water_thread.start()

time.sleep(5)
print("\nStopping all timers...")

stop_event.set() # Raise the stop event to signal threads to stop after 5 seconds 

study_thread.join()
break_thread.join()

print("\nMain program ended")
