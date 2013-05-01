import unittest
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

#    dates.sort()
    lastDate = dates[-1] 
    checkDate = lastDate + timedelta(days=averageDays)
    if checkDate <= self.today:
      return True
    else:
      return False


class ReminderTest(unittest.TestCase):
  def setUp(self):
    self.reminder = Reminder(date.today())
    self.dates = []

  def testNoPurchaseDatesShouldNotRemind(self):
    actual = self.reminder.shouldRemind(self.dates)
    self.assertEqual(False, actual)

  def testSinglePreviousPurchaseDoesNotRemind(self):
    self.dates.append(date(2010, 1, 1))
    actual = self.reminder.shouldRemind(self.dates)
    self.assertEqual(False, actual)

  def testRemindsIfOlderThanLastDatePlusAverageDays(self):
    self.reminder = Reminder(date(2013, 1, 10))
    self.dates.append(date(2013, 1, 1))
    self.dates.append(date(2013, 1, 5))
    actual = self.reminder.shouldRemind(self.dates)
    self.assertEqual(True, actual)

  def testRemindsIfEqualToLastDatePlusAverageDays(self):
    self.reminder = Reminder(date(2013, 1, 9))
    self.dates.append(date(2013, 1, 1))
    self.dates.append(date(2013, 1, 5))
    actual = self.reminder.shouldRemind(self.dates)
    self.assertEqual(True, actual)

  def testDoesntRemindIfGreaterThanLastDatePlusAverageDays(self):
    self.reminder = Reminder(date(2013, 1, 8))
    self.dates.append(date(2013, 1, 1))
    self.dates.append(date(2013, 1, 5))
    actual = self.reminder.shouldRemind(self.dates)
    self.assertEqual(False, actual)

  def testRemindsIfDatesOutOfOrder(self):
    self.reminder = Reminder(date(2013, 1, 5))
    self.dates.append(date(2013, 1, 4))
    self.dates.append(date(2013, 1, 1))
    actual = self.reminder.shouldRemind(self.dates)
    self.assertEqual(False, actual)


if __name__ == "__main__":
  unittest.main()


