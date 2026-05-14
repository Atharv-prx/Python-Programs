import threading
import time

def Study_timer(name, minutes):
    print(f"{name} starts studying")
    time.sleep(minutes*60)
    print(f"{name} finished studying")

def Break_timer(minutes):
    print(f"Break starts")
    time.sleep(minutes*60)
    print(f"Break finished")

def Water_timer(minutes):
    print(f"Water timer starts")
    time.sleep(minutes*60)
    print(f"Water timer finished")

study = threading.Thread(target=Study_timer, args=("Alice", 0.10))
break_time = threading.Thread(target=Break_timer, args=(0.3,))
water_time = threading.Thread(target=Water_timer, args=(0.6,))

study.start()
break_time.start()
water_time.start()

study.join()
break_time.join()
water_time.join()

print("All timers are finished")