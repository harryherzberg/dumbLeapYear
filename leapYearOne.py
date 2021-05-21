import unittest
import pytest
import coverage

class leaper:
  def __init__(self):
    self.year = 0
  def takeYear(self):
    filler = input ( "sentance: ")
    self.year = int(filler)
  def LeapyearChecker(self):
    if self.year%4 == 0: 
      if self.year%400 == 0:
        print(str(self.year) + " is leap year")
        return True
      if self.year%100 == 0:
        print(str(self.year) +" is not leap year")
        return False
      print(str(self.year) +" is leap year")
      return True
    print(str(self.year) +" is not leap year")
    return False


class myTest(unittest.TestCase):

    #tests to see if your leap year is not false
    def testEmpt(self):
        print("testing to see if either can be empty")
        name = leaper()
        name.takeYear()
        self.assertNotEqual(name.LeapyearChecker(), True)

    #tests to see if it works in normal condition
    def testNorm(self):
        print("testing to see if it counts correctly")
        name = leaper()
        name.year = "j"
        name.LeapyearChecker()
        self.assertEqual(3, 3)



try:
  if __name__ == '__main__':
    unittest.main()
except:
  print("error")
