import threading
import queue
import time
import random

q = queue.Queue()

def producer():

    for i in range(1, 11):

        item = f"Task-{i}"

        print(f"[Produced] {item}")

        q.put(item)

        time.sleep(random.uniform(0.5, 1.5))

def consumer():

    while True:

        item = q.get()

        print(f"[Consumed] {item}")

        time.sleep(random.uniform(1, 2))

        q.task_done()

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer, daemon=True)

producer_thread.start()
consumer_thread.start()

producer_thread.join()

q.join()

print("\nAll tasks completed")

# q.put(item) - Adds item to queue, Producer creates work.

# q.get() - Consumer takes item from queue.
# If queue is empty, consumer automatically WAITS, no CPU wastage, no crash. This is why Queue is powerful.

# q.task_done() - Indicates that a formerly enqueued task is complete. This is used by consumer to signal that it has finished processing an item.
# Without this: q.join() never finishes, 

# q.join() - Main thread waits until: all queue tasks are completed
# Meaning: every put() must have matching task_done() for q.join() to finish.