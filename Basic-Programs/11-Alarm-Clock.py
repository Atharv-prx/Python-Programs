import time
import datetime
# Next 2 lines so that pygame doesn't print the support prompt when imported
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")

    sound_file = "Basic-Programs/11-Music-For-Alarm.mp3"

    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("Wake up!")

            # Playing the alarm sound
            # mixer module is used to load and play sounds in pygame

            pygame.mixer.init()  
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            # To continue playing the sound until the user stops it
            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False

        time.sleep(1)

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)