import unittest
from datetime import date, timedelta
from reminder.reminder import Reminder
import reminder.average_days_between 

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

