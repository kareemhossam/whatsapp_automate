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
        # print(row)

print(rows[0])

for row in rows:
    w.sendwhatmsg_instantly(row[1], """
                            مساء الخير، يذكركم مجلس قيادة فريق الاشبال بعودة النشاط يوم الاربعاء القادم من الساعة 7م الي 9:30م علي ان يكون اجتماعات الموسم الصيفي يومي الاحد والاربعاء من كل اسبوع من الساعة 7م الي 9:30م
                            """,20)
    pyautogui.click(1050, 950)
    pyautogui.press("enter")
    time.sleep(10)
