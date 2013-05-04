import unittest
from datetime import date
from reminder.average_days_between import AverageDaysBetween, InvalidDateError

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

  def testDatesIsNotSortedInPlace(self):
    self.dates.append(date(2013, 1, 2))
    self.dates.append(date(2013, 1, 1))
    self.dates.append(date(2012, 12, 31))
    self.averageDaysBetween.calculate(self.dates)
    self.assertEqual(date(2013, 1, 2), self.dates[0])
    self.assertEqual(date(2013, 1, 1), self.dates[1])
    self.assertEqual(date(2012, 12, 31), self.dates[2])

