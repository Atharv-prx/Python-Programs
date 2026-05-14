# Direct upgrade of countdown timer program from Multithreading folder.
# Improved on code repetition
# Live countdown display

import threading
import time

def timer(timer_name, minutes):

    thread_name = threading.current_thread().name

    print(f"\n=====[{thread_name}] {timer_name} started=====")

    total_seconds = int(minutes*60)

    while total_seconds > 0:

        mins, secs = divmod(total_seconds, 60)

        print(f"\n{timer_name}: {mins:02}:{secs:02} remaining")

        time.sleep(1)

        total_seconds -= 1
    
    print(f"\n=====[{thread_name}] {timer_name} finished======\n")

study_thread = threading.Thread(target = timer, args = ("Study Timer", 0.3), name = "Study Thread")

break_thread = threading.Thread(target=timer, args=("Break Timer", 0.2), name="BreakThread")

water_thread = threading.Thread(target=timer, args=("Water Reminder", 0.1), name="WaterThread")

study_thread.start()
break_thread.start()
water_thread.start()

study_thread.join()
break_thread.join()
water_thread.join()

print("All timers completed")