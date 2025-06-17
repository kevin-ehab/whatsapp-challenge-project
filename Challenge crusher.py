import pyautogui as pag
import datetime

def check_time():
    now = datetime.datetime.now()
    if (now.hour == 0  and now.minute == 0 and now.second == 0) or (now.hour == 0 and now.minute == 0 and now.second == 1) or (now.hour == 23 and now.minute == 59 and now.second == 59):
        pag.write("First")
        pag.press("enter")
        print("Done")

if __name__ == "__main__":
    print("Challenge crusher running. Press Ctrl+C to exit.")
    while True:
        check_time()