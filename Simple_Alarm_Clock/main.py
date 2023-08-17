import time
import winsound

def set_alarm():
    alarm_time = input("HH:MM format: ")
    return alarm_time
def play_alarm():
    frequency = 2000
    duration = 1000
    winsound.Beep(frequency, duration)
def main():
    print("Simple Alarm Clock")
    alarm_time = set_alarm()

    while True:
        current_time = time.strftime("%H:%M")
        if current_time == alarm_time:
            print("Wake Up")
            play_alarm()
            break

        time.sleep(1)

if __name__ == "__main__":
    main()
            