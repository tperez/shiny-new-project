import unittest
from datetime import date

class AverageDaysBetween:
  def __init__(self, today):
    self.today = today

  def calculate(self, dates):
    if len(dates) < 2:
      return None

    dates.sort()

    for d in dates:
      if (d - self.today).days > 0:
        raise InvalidDateError("purchase dates must be prior to today")

    days = []
    for x in range(1, len(dates)):
      days.append((dates[x] - dates[x-1]).days)

    average = sum(days) / float(len(days))
    return average


class InvalidDateError(Exception):
  def __init__(self, value):
    self.value = value

  def __str__(self):
    return repr(self.value)


class AverageDaysBetweenTest(unittest.TestCase):
  def setUp(self):
    self.averageDaysBetween = AverageDaysBetween(date.today())
    self.dates = []

  def testNoDateReturnsNone(self):
    actual = self.averageDaysBetween.calculate(self.dates)
    self.assertEqual(None, actual)

  def testOneDateReturnsNone(self):
    self.dates.append(date.today())
    actual = self.averageDaysBetween.calculate(self.dates)
    self.assertEqual(None, actual)

  def testTwoDatesReturnsTimeBetween(self):
    self.dates.append(date(2012, 12, 31))
    self.dates.append(date(2013, 1, 1))
    actual = self.averageDaysBetween.calculate(self.dates)
    self.assertEqual(1, actual)

  def testThreeDatesReturnsAverageTimeBetween(self):
    self.dates.append(date(2012, 12, 31))
    self.dates.append(date(2013, 1, 1))
    self.dates.append(date(2013, 1, 2))
    actual = self.averageDaysBetween.calculate(self.dates)
    self.assertEqual(1, actual)

  def testOrderDoesntMatterForDates(self):
    self.dates.append(date(2013, 1, 2))
    self.dates.append(date(2013, 1, 1))
    self.dates.append(date(2012, 12, 31))
    actual = self.averageDaysBetween.calculate(self.dates)
    self.assertEqual(1, actual)

  def testFutureDateThrowsException(self):
    a = AverageDaysBetween(date(2013,1,1))
    self.dates.append(date(2013, 1, 2))
    self.dates.append(date(2013, 1, 1))
    with self.assertRaises(InvalidDateError):
      a.calculate(self.dates)


if __name__ == "__main__":
  unittest.main()


