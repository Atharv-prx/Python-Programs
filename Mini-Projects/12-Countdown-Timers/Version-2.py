# Added daemon threads
# Added stop features 

import threading
import time

stop_event = threading.Event() # Creates an event with False so stop_event.is_set() returns false

def timer(timer_name, minutes):

    thread_name = threading.current_thread().name

    print(f"\n=====[{thread_name}] {timer_name} started=====")

    total_seconds = int(minutes*60)

    while total_seconds > 0 and not stop_event.is_set():  
    # This loop says that “Keep looping while time is still remaining and “Keep looping IF stop signal has NOT been triggered.”

        mins, secs = divmod(total_seconds, 60)

        print(f"\n{timer_name}: {mins:02}:{secs:02} remaining")

        time.sleep(1)

        total_seconds -= 1

    if stop_event.is_set(): # When main thread does this then stop_event.is_set() returns true
        print(f"\n Timer Stopped Early")
    else:
        print(f"\n=====[{thread_name}] {timer_name} finished======\n")

study_thread = threading.Thread(target = timer, args = ("Study Timer", 0.5), name = "Study Thread")

break_thread = threading.Thread(target=timer, args=("Break Timer", 0.5), name="BreakThread")

water_thread = threading.Thread(target=timer, args=("Water Reminder", 1), name="WaterThread", daemon=True)

study_thread.start()
break_thread.start()
water_thread.start()

time.sleep(5)
print("\nStopping all timers...\n")

stop_event.set() # Raise the stop event to signal threads to stop after 5 seconds 
                 # All threads will check for this event and stop accordingly. Daemon thread will stop immediately when main program ends.

study_thread.join()
break_thread.join()

print("Main program ended")