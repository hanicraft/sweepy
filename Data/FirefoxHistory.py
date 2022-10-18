#!/usr/bin/python

import sqlite3

sqlite_file = '/home/homework/.mozilla/firefox/<profile>/places.sqlite'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

c.execute('SELECT * from moz_places')
all_rows = c.fetchall()


print(" ____                           ____                                ______                                           ")
print("/\  _`\   __                   /\  _`\                             /\__  _\                                          ")
print("\ \ \L\_\/\_\    _ __     __   \ \ \L\_\  ___    __  _             \/_/\ \/   _ __     __       ___      __    _ __  ")
print(" \ \  _\/\/\ \  /\`'__\ /'__`\  \ \  _\/ / __`\ /\ \/'\               \ \ \  /\`'__\ /'__`\    /'___\  /'__`\ /\`'__|")
print("  \ \ \/  \ \ \ \ \ \/ /\  __/   \ \ \/ /\ \L\ \\/>  </                \ \ \ \ \ \/ /\ \L\.\_ /\ \__/ /\  __/ \ \ \/ ")
print("   \ \_\   \ \_\ \ \_\ \ \____\   \ \_\ \ \____/ /\_/\_\                \ \_\ \ \_\ \ \__/.\_\\ \____\\ \____\ \ \_\ ")
print("    \/_/    \/_/  \/_/  \/____/    \/_/  \/___/  \//\/_/                 \/_/  \/_/  \/__/\/_/ \/____/ \/____/  \/_/ ")                                                                                                                                                                                                                                          
print("\nVisited Webpages:\n")

for item in all_rows:
        print(item[1])