import unittest
import WorkTime
 
class FocusTimer(unittest.TestCase):
    def test_WorkTime_default_time(self):
        ob = WorkTime.WorkTime()
        #time is default set to 1200 seconds or 20 min
        self.assertEqual(ob.time, 1200)

    def test_WorkTime_get_time(self):
        ob = WorkTime.WorkTime()
        time = ob.get_time()
        #default time is 20 min
        self.assertEqual(time, 20)

if __name__ == '__main__':
    unittest.main()
