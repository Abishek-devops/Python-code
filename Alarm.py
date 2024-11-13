import time
import datetime
import pygame


def set_alarm(Alarm_time):
    print("Times up!!")

Alarm_time=input("Enter the Alarm time in (HH:MM:SS) :")
print(f"Alarm set for {Alarm_time}")
is_running=True

while is_running:
    current_time=datetime.datetime.now().strftime("%H:%M:%S")
    target_time=Alarm_time
    print(current_time)
    time.sleep(1)
    if target_time==current_time:
        set_alarm(Alarm_time)
        sound = "my_music.mp3.mp3"
        pygame.mixer.init()
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(1)

        is_running=False