import unittest
import Timer
 
class FocusTimer(unittest.TestCase):
    def test_Timer_default_time(self):
        ob = Timer.Timer()
        #time is default set to 1200 seconds or 20 min
        self.assertEqual(ob.time, 1200)

    def test_Timer_get_time(self):
        ob = Timer.Timer()
        time = ob.get_time()
        #default time is 20 min (1200 sec)
        self.assertEqual(time, 1200)

    def test_Timer_get_min_whole(self):
        ob = Timer.Timer()
        min = ob.get_min()
        #default time is 20 min
        self.assertEqual(min, 20)

    def test_Timer_get_min_part(self):
        ob = Timer.Timer()
        ob.time = 1195
        #this should be 19 min 55 sec
        time = ob.get_min()
        self.assertEqual(time, 19)



if __name__ == '__main__':
    unittest.main()
