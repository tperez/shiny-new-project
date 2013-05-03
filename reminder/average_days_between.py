from datetime import date

class AverageDaysBetween:
  def __init__(self, today):
    self.today = today

  def calculate(self, dates):
    if len(dates) < 2:
      return None

    sortedDates = sorted(dates)

    for d in sortedDates:
      if (d - self.today).days > 0:
        raise InvalidDateError("purchase dates must be prior to today")

    days = []
    for x in range(1, len(sortedDates)):
      days.append((sortedDates[x] - sortedDates[x-1]).days)

    average = sum(days) / float(len(days))
    return average


class InvalidDateError(Exception):
  def __init__(self, value):
    self.value = value

  def __str__(self):
    return repr(self.value)

