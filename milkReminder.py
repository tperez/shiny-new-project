import unittest


class MilkReminder:
	def shouldRemind(self, averageDaysBetweenPurchases, daysSinceLastPurchase):
		if daysSinceLastPurchase == None:
			return False

		if averageDaysBetweenPurchases == None:
			return False

		if daysSinceLastPurchase < averageDaysBetweenPurchases:
			return False

		return True


class MilkReminderTest(unittest.TestCase):
	def setUp(self):
		self.reminder = MilkReminder()
		self.averageDaysBetweenPurchases = None
		self.daysSinceLastPurchase = None

	def testNoAverageHistory(self):
		actual = self.reminder.shouldRemind(self.averageDaysBetweenPurchases, self.daysSinceLastPurchase)
		self.assertEqual( False, actual )
	
	def testWithOnePreviousPurchaseShouldNotReceiveAlert(self):
		self.daysSinceLastPurchase = 5
		actual = self.reminder.shouldRemind(self.averageDaysBetweenPurchases, self.daysSinceLastPurchase)
		self.assertEqual( False, actual )

	def testWithAverageEqualToDaysSinceLastPurchaseShouldReceiveAlert(self):
		self.averageDaysBetweenPurchases = 5
		self.daysSinceLastPurchase = 5
		actual = self.reminder.shouldRemind(self.averageDaysBetweenPurchases, self.daysSinceLastPurchase)
		self.assertEqual( True, actual )
	
	def testShouldNotReceiveAlertIfLessThanAverage(self):
		self.averageDaysBetweenPurchases = 6
		self.daysSinceLastPurchase = 5
		actual = self.reminder.shouldRemind(self.averageDaysBetweenPurchases, self.daysSinceLastPurchase)
		self.assertEqual( False, actual )
		
	def testShouldReceiveAlertIfGreaterThanAverage(self):
		self.averageDaysBetweenPurchases = 5
		self.daysSinceLastPurchase = 6
		actual = self.reminder.shouldRemind(self.averageDaysBetweenPurchases, self.daysSinceLastPurchase)
		self.assertEqual( True, actual )

if __name__ == "__main__":
	unittest.main()


