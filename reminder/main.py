import fileinput
from datetime import datetime, date
from reminder import Reminder

dates = []

for line in fileinput.input():
  line = line.rstrip('\n')
  date = datetime.strptime(line, '%m/%d/%Y')
  dates.append(date)

reminder = Reminder(date.today())

if reminder.shouldRemind(dates):
  print 'Reminder should be sent'
else:
  print 'A reminder should not be sent'
