"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

userInput = input("Insert the month and year in form, in commas:").split(",")
print(userInput)

def renderCalendar(month = 0, year = 0):
	print(month, year)
	print(calendar)
	if (month == 0 and year == 0):
		print(datetime.date)
	elif (month != 0 and year == 0):
		print(calendar.monthdatescalendar(datetime.year, month))
	elif (month != 0 and year != 0):
		print(calendar.monthdatescalendar(year, month))

renderCalendar(float(userInput[0]), float(userInput[1]))
