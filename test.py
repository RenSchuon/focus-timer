import unittest
import WorkTime
 
class TestTicTacToeMethod(unittest.TestCase):
    def test_WorkTime_default_time(self):
        ob = WorkTime.WorkTime()
        self.assertEqual(ob.time, 1200)


if __name__ == '__main__':
    unittest.main()
