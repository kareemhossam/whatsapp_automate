from threading import Timer
import pyautogui
import pywhatkit as w
import csv
import time

csvreader = csv.reader(open('./broadcast.csv', encoding="utf8"))

header = []
header = next(csvreader)
# print(header)

rows = []

for row in csvreader:
    if len(row[1]) != 0:
        rows.append(row)

for row in rows:
    print("Sending message to: " + row[0] + "on Phone number: " + row[1])
    w.sendwhatmsg_instantly(row[1], """
يرجي الانضمام اي جروب فريق اشبال البحر المتوسط:
link
                            """,20)
    pyautogui.click(1050, 950)
    pyautogui.press("enter")
    time.sleep(10)
