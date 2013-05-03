from datetime import date, timedelta
from average_days_between import AverageDaysBetween

class Reminder:
  def __init__(self, today):
    self.today = today
    self.averageDaysBetween = AverageDaysBetween(self.today)

  def shouldRemind(self, dates):
    if len(dates) < 2:
      return False

    averageDays = self.averageDaysBetween.calculate(dates)

    sortedDates = sorted(dates)
    lastDate = sortedDates[-1] 
    checkDate = lastDate + timedelta(days=averageDays)
    if checkDate <= self.today:
      return True
    else:
      return False
