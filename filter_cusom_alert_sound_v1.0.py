import re


pattern1 = r"\sPlayAlertSound\s[1]\s\d{3}"
pattern2 = r"\sPlayAlertSound\s[2]\s\d{3}"
pattern3 = r"\sPlayAlertSound\s[3]\s\d{3}"
pattern4 = r"\sPlayAlertSound\s[4]\s\d{3}"
pattern5 = r"\sPlayAlertSound\s[5]\s\d{3}"
pattern6 = r"\sPlayAlertSound\s[6]\s\d{3}"
pattern12 = r"\sPlayAlertSound\s[1][2]\s\d{3}"

custom_alert_music1 = "\tCustomAlertSound \"AlertSound_01.wav\""
custom_alert_music2 = "\tCustomAlertSound \"AlertSound_02.wav\""
custom_alert_music3 = "\tCustomAlertSound \"AlertSound_03.wav\""
custom_alert_music4 = "\tCustomAlertSound \"AlertSound_04.wav\""
custom_alert_music5 = "\tCustomAlertSound \"AlertSound_05.wav\""
custom_alert_music6 = "\tCustomAlertSound \"AlertSound_06.wav\""
custom_alert_music12 = "\tCustomAlertSound \"AlertSound_12.wav\""

with open("data.filter", "rt") as f:
    files = f.read()

files = re.sub(pattern1, custom_alert_music1, files)
files = re.sub(pattern2, custom_alert_music2, files)
files = re.sub(pattern3, custom_alert_music3, files)
files = re.sub(pattern4, custom_alert_music4, files)
files = re.sub(pattern5, custom_alert_music5, files)
files = re.sub(pattern6, custom_alert_music6, files)
files = re.sub(pattern12, custom_alert_music12, files)

new_filter = "New_test_filter.filter"
with open(new_filter, "wt") as n:
    n.write(files)

print("New custom alert sound filter {0}  has been generated".format(new_filter))
