import unittest
from app.main.Controller.Root.ActiveRootFinder import *

class DriveTestCase(unittest.TestCase):

	def testactiveRootFinder(self):
		self.assertEqual(drive(),['C:', 'D:', 'E:'])

if __name__ == '__main__':
	unittest.main()